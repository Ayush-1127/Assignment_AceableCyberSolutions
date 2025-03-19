from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import sqlite3
import time

@csrf_exempt
def search_logs(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            search_query = data.get("query", "")
            start_time = int(data.get("start_time", 0))
            end_time = int(data.get("end_time", float("inf")))

            print(f"start_time type: {type(start_time)}, value: {start_time}")  
            print(f"end_time type: {type(end_time)}, value: {end_time}")  

            conn = sqlite3.connect("db.sqlite3")
            cursor = conn.cursor()

            start = time.time()

            
            cursor.execute("""
                SELECT * FROM logs 
                WHERE (srcaddr = ? OR dstaddr = ? OR action = ?) 
                AND (starttime BETWEEN ? AND ?)
            """, (search_query, search_query, search_query, start_time, end_time))

            matching_logs = [
                dict(zip([column[0] for column in cursor.description], row)) 
                for row in cursor.fetchall()
            ]

            conn.close()
            end = time.time()
            search_time = round(end - start, 4)

            return JsonResponse({
                "results": matching_logs,
                "search_time": search_time
            }, safe=False)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    return JsonResponse({"message": "Use POST request"}, status=405)


