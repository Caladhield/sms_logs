import pandas as pd
import mysql.connector

# Load CSV
df = pd.read_csv("filtered_messages.csv")

# Rename columns to match the table
df.rename(columns={"to": "receiver_phone", "from": "sender"}, inplace=True)

# Connect to MySQL
conn = mysql.connector.connect(
    host="duplicated-for-testing-12-feb-2025.c0z9w132qdby.eu-central-1.rds.amazonaws.com",
    user="master",
    password="tyz5jFygKXGQLJ8n",
    database="db_djurensratt"
)
cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO db_djurensratt.temp_data (receiver_phone, sender, message, created, parts)
        VALUES (%s, %s, %s, %s, %s)
    """, (row["receiver_phone"], row["sender"], row["message"], row["created"], row["parts"]))

conn.commit()
cursor.close()
conn.close()
