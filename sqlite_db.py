import sqlite3
import pandas as pd

DB_file = 'Test_DB'

conn = sqlite3.connect(DB_file)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS production (
    output int,
    Date date,
    record_update datetime
    )
''')

cursor.execute('''
    INSERT OR IGNORE INTO production (output, Date, record_update) 
    VALUES
        (230, '2025-01-01', '2025-01-01 17:30:00'),
		(250, '2025-01-01', '2025-01-01 19:30:00'),
		(230, '2025-01-02', '2025-01-02 17:30:00'),
		(235, '2025-01-02', '2025-01-02 19:30:00'),
		(260, '2025-01-03', '2025-01-03 17:30:00'),
		(275, '2025-01-04', '2025-01-04 19:35:00'),
		(277, '2025-01-05', '2025-01-05 19:35:00')
''')

df = pd.read_sql_query("SELECT * FROM production", conn)

print(df)
conn.commit()
conn.close()