import sqlite3
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'events'))
# from utils import load_data  # Import function from utils.py
from events.utils import load_data


# Connect to SQLite database
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# Ensure the table exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        serialno INTEGER,
        version INTEGER,
        account_id INTEGER,
        instance_id TEXT,
        srcaddr TEXT,
        dstaddr TEXT,
        srcport INTEGER,
        dstport INTEGER,
        protocol INTEGER,
        packets INTEGER,
        bytes INTEGER,
        starttime INTEGER,
        endtime INTEGER,
        action TEXT,
        log_status TEXT,
        filename TEXT
    )
''')

# Load data using utils.py
events = load_data()

# Insert data into SQLite
for event in events:
    cursor.execute('''
        INSERT INTO logs (serialno, version, account_id, instance_id, srcaddr, dstaddr, srcport, dstport, 
                          protocol, packets, bytes, starttime, endtime, action, log_status, filename)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        event["serialno"], event["version"], event["account_id"], event["instance_id"], event["srcaddr"], 
        event["dstaddr"], event["srcport"], event["dstport"], event["protocol"], event["packets"], 
        event["bytes"], event["starttime"], event["endtime"], event["action"], event["log_status"], 
        event["filename"]  
    ))

# Commit and close connection
conn.commit()
conn.close()

print(f"✅ {len(events)} records inserted into the database successfully.")
