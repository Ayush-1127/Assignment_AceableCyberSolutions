import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from events.models import Event

def load_data(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split()
            if len(data) != 14:
                continue  

            event = Event(
                serialno=int(data[0]),
                version=int(data[1]),
                account_id=data[2],
                instance_id=data[3],
                srcaddr=data[4],
                dstaddr=data[5],
                srcport=int(data[6]),
                dstport=int(data[7]),
                protocol=int(data[8]),
                packets=int(data[9]),
                bytes=int(data[10]),
                starttime=int(data[11]),
                endtime=int(data[12]),
                action=data[13],
                log_status=data[14]
            )
            event.save()

    print("Data loaded successfully!")

# Run the script
if __name__ == "__main__":
    file_path = "path/to/your/logfile.log"  
    load_data(file_path)
