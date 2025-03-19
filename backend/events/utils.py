import os

DATA_FOLDER = "data"

def load_data():
    """Loads all log files from the data folder"""
    events = []
    
    print(f"Checking files in: {DATA_FOLDER}")  

    for filename in os.listdir(DATA_FOLDER):
        file_path = os.path.join(DATA_FOLDER, filename)

       
        print(f"Reading file: {filename}")  

        with open(file_path, "r") as file:
            for line in file:
                print(f"Raw line: {line}")  

                parts = line.strip().split()
                if len(parts) != 15:  
                    print(f"Skipping invalid line: {parts}")  
                    continue  
                
                event = {
                    "serialno": int(parts[0]),
                    "version": int(parts[1]),
                    "account_id": int(parts[2]),
                    "instance_id": parts[3],
                    "srcaddr": parts[4],
                    "dstaddr": parts[5],
                    "srcport": int(parts[6]),
                    "dstport": int(parts[7]),
                    "protocol": int(parts[8]),
                    "packets": int(parts[9]),
                    "bytes": int(parts[10]),
                    "starttime": int(parts[11]),
                    "endtime": int(parts[12]),
                    "action": parts[13],
                    "log_status": parts[14],
                    "filename": filename
                }
                
                events.append(event)

    print(f" Total logs loaded: {len(events)}")  
    print(f"Data folder path: {DATA_FOLDER}")
    print(f"Exists: {os.path.exists(DATA_FOLDER)}")

    return events
