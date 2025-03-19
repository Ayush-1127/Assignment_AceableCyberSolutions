import sqlite3

# Connect to SQLite database (creates a new file if it doesn't exist)
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# Create table (modify this based on your file structure)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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

# Commit and close
conn.commit()
conn.close()

print(" Database and table created successfully.")
