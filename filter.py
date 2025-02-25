import pandas as pd

# Load the CSV file
df = pd.read_csv("adoveo20250214.csv", delimiter=";", skiprows=2)

# Define the message keywords
keywords = "Swisha en hälsning idag på Alla hjärtans dag så får mottagaren du väljer ett fint gåvokort med din personliga hälsning via SMS. En omtanke för någon du bryr dig om – och för djuren."

# Filter messages from "DjurensRatt"
filtered_df = df[df["from"] == "DjurensRatt"]

# Further filter messages containing the keywords
filtered_df = filtered_df[filtered_df["message"].str.contains(keywords, case=False, na=False)]

# Filter for each link
df_link1 = filtered_df[filtered_df["message"].str.contains("https://bit.ly/4jXGRMg", na=False)]
df_link2 = filtered_df[filtered_df["message"].str.contains("https://bit.ly/3WWQeSL", na=False)]

# Save to separate CSV files
df_link1.to_csv("filtered_messages_link1.csv", index=False)
df_link2.to_csv("filtered_messages_link2.csv", index=False)

print("Filtered CSV files created successfully!")
