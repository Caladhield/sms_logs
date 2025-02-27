import pandas as pd

df = pd.read_csv("adoveo20250214.csv", delimiter=";", skiprows=2)

keywords = "Tack för ditt engagemang för Situation Sthlm. Tack vare ditt stöd har fler hemlösa människor kunnat förändra sin livssituation. Här kan du skicka en hälsning till någon på allas hjärtans dag. Ditt stöd gör skillnad. Skicka en hälsning här"

filtered_df = df[df["from"] == "SituationS"]

filtered_df = filtered_df[filtered_df["message"].str.contains(keywords, case=False, na=False)]

df_1 = filtered_df[filtered_df["message"].str.contains("bit.ly/situationsthlmkort", na=False)]


df_1.to_csv("filtered_messages_situation.csv", index=False)


print("Filtered CSV files created successfully!")
