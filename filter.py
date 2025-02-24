import pandas as pd

df = pd.read_csv("adoveo20250214.csv", delimiter=";", skiprows=2)

keywords = "Swisha en hälsning idag på Alla hjärtans dag så får mottagaren du väljer ett fint gåvokort med din personliga hälsning via SMS. En omtanke för någon du bryr dig om – och för djuren."

filtered_df = df[df["from"] == "DjurensRatt"]
filtered_df = df[df["message"].str.contains(keywords, case=False, na=False)]

# Save to a new CSV file
filtered_df.to_csv("filtered_messages.csv", index=False)

print("Filtered CSV file created successfully!")