import sqlite3
import pandas as pd

DB_file = 'Test_DB'
conn = sqlite3.connect(DB_file)
df = pd.read_sql_query("SELECT * FROM production", conn)

# Assessment:
# 1. Print top 3 rows
print("Top 3 rows:")
print(df.head(3))

# 2. Print latest record per day
df['record_update'] = pd.to_datetime(df['record_update'])
df_latest_record_per_day = df.loc[df.groupby('Date')['record_update'].idxmax()]
print("\nLatest record per day:")
print(df_latest_record_per_day)

# 3. Save dataframe to csv file "production_output.csv"
print("\nSave data to csv file: 'production_output.csv'")
df_latest_record_per_day.to_csv('production_output.csv')

# 4. Total number of the output
total_output = df['output'].sum()
print("\nTotal output:", total_output)



