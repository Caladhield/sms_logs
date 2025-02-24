import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("filtered_messages.csv")
engine = create_engine("your_database_connection_string")

existing_numbers = pd.read_sql("SELECT phone FROM table", engine)

new_records = df[~df["phone"].isin(existing_numbers["phone"])]

if not new_records.empty:
    new_records.to_sql("table", engine, if_exists="append", index=False)
    print("New rows inserted")
else:
    print("No new data")
