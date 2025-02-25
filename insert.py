import pandas as pd
import mysql.connector
import json

# Load CSV
df = pd.read_csv("filtered_messages_182.csv")

# Rename column "to" to match MySQL column name
df.rename(columns={"to": "telephone"}, inplace=True)

# Convert "parts" to integer
df["parts"] = df["parts"].astype(int)

# Create JSON string for report_download_email column
df["report_download_email"] = df["parts"].apply(lambda x: json.dumps({"parts": x, "cost": None}))

# Convert DataFrame to JSON
json_data = json.loads(df.to_json(orient="records"))

# Connect to MySQL
conn = mysql.connector.connect(
    host="rds-prod-1.c0z9w132qdby.eu-central-1.rds.amazonaws.com",
    user="master",
    password="tyz5jFygKXGQLJ8n",
    database="db_djurensratt"
)
cursor = conn.cursor()

# Fixed SQL query (corrected column names and values)
insert_query = """
    INSERT INTO participant (campaign_id, telephone, created, report_download_email)
    VALUES (%s, %s, %s, %s)
"""

# Insert data (hardcoding campaign_id as 12)
for row in json_data:
    cursor.execute(insert_query, (182, row["telephone"], row["created"], row["report_download_email"]))

# Commit and close
conn.commit()
cursor.close()
conn.close()
