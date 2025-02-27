import pandas as pd
import mysql.connector
import json

df = pd.read_csv("filtered_messages_situation.csv")

df.rename(columns={"to": "telephone"}, inplace=True)

df["parts"] = df["parts"].astype(int)

df["report_download_email"] = df["parts"].apply(lambda x: json.dumps({"parts": x, "cost": None}))

json_data = json.loads(df.to_json(orient="records"))

conn = mysql.connector.connect(
    host="rds-prod-1.c0z9w132qdby.eu-central-1.rds.amazonaws.com",
    user="master",
    password="tyz5jFygKXGQLJ8n",
    database="db_situationsthlm"
)
cursor = conn.cursor()

insert_query = """
    INSERT INTO participant (campaign_id, telephone, created, report_download_email, coupon_send)
    VALUES (%s, %s, %s, %s, %s)
"""

for row in json_data:
    cursor.execute(insert_query, (11, row["telephone"], row["created"], row["report_download_email"], 1))

conn.commit()
cursor.close()
conn.close()
