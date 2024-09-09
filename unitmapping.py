import pandas as pd
from datetime import datetime

# Load the CSV files into DataFrames
df1 = pd.read_csv('new2023unitsexport.csv')  # The file containing "OPTION3_Manager_ID" and "UnitName"
df2 = pd.read_csv('2024 unit export.csv')  # The file containing "UnitID" and "UnitName"

# Merge the DataFrames on the "UnitName" column
merged_df = pd.merge(df1, df2, on='UnitName', how='inner')

# Specify the output filename with a timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Format: YYYYMMDD_HHMMSS
output_filename = f'Unit_mapping_mix_{timestamp}.csv'

# Save the merged DataFrame to a new CSV file
merged_df.to_csv(output_filename, index=False)

print(f'Merged DataFrame saved as: {output_filename}')