import pandas as pd
from pathlib import Path

# Path to data folder
data_path = Path("data")

# Read all CSV files
all_files = data_path.glob("*.csv")

df_list = []
for file in all_files:
    df = pd.read_csv(file)
    df_list.append(df)

# Combine all CSVs
combined_df = pd.concat(df_list, ignore_index=True)

# Keep only Pink Morsels
combined_df = combined_df[combined_df["product"] == "Pink Morsels"]

# Create sales column
combined_df["sales"] = combined_df["quantity"] * combined_df["price"]

# Select required columns
final_df = combined_df[["sales", "date", "region"]]

# Save output
final_df.to_csv("output.csv", index=False)

print("✅ Data processing complete. Output saved as output.csv")
