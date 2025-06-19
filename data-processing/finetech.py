import pandas as pd
import os

# Directory containing the TXT files
directory = r'C:\Users\alex.letwin\Desktop\Fab\Finetech\20250617'

# Loop through all TXT files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        txt_file = os.path.join(directory, filename)
        try:
            df = pd.read_csv(txt_file, sep='\s+', encoding='ISO-8859-1')
        except UnicodeDecodeError:
            print(f"Error reading file: {filename}")
            continue

        # Ensure relevant columns are properly named
        cchm_col = 'Temp[°C]'
        hp_col = 'Temp[°C]'
        time_col = 'Time[ms]'

        # Filter CCHM and HP data
        cchm_df = df[df['Box'] == 'CCHM']
        hp_df = df[df['Box'] == 'HP']

        # Find the highest CCHM Temp and HP Temp
        highest_cchm_temp = cchm_df[cchm_col].max()
        highest_hp_temp = hp_df[hp_col].max()

        # Calculate the total time CCHM Temp is above 217°C
        temp_above_217 = hp_df[hp_df[hp_col] > 217]
        total_time_above_217 = 0

        # Calculate the actual duration above 217°C
        if not temp_above_217.empty:
            time_above_217 = temp_above_217[time_col].values
            total_time_above_217 = (time_above_217[-1] - time_above_217[0]) / 1000  # Convert to seconds

        # Output the results
        print(f"File: {filename}")
        # print(f"Highest CCHM Temp: {highest_cchm_temp}")
        print(f"Highest HP Temp: {highest_hp_temp}")
        print(f"Total Time HP Temp > 217°C: {total_time_above_217} seconds")
        print("---------------------------------")