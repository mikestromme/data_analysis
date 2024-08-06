from zipfile import ZipFile
import os
import numpy as np
from datetime import datetime
import pandas as pd

# Path of the zip file
zip_path = "O2Ring_20230724203820.zip"
unzip_folder = "unzipped/"

# Create a folder to unzip the files into
os.makedirs(unzip_folder, exist_ok=True)

# Unzip the file
with ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(unzip_folder)

# List the files in the unzipped folder
unzipped_files = os.listdir(unzip_folder)
unzipped_files


# Load the first CSV file as a sample
sample_file_path = os.path.join(unzip_folder, unzipped_files[0])
sample_data = pd.read_csv(sample_file_path)

# Display the first few rows of the sample data
sample_data.head()

# Initialize an empty DataFrame
all_data = pd.DataFrame()

# Load all the data from all the CSV files
for file in unzipped_files:
    file_path = os.path.join(unzip_folder, file)
    data = pd.read_csv(file_path)
    
    # Add the data from this file to all_data
    all_data = pd.concat([all_data, data])

# Display the size of all_data and the first few rows
#print(f"Size of all data: {all_data.shape}")
all_data.head()


# Remove data with an Oxygen Level of 255
filtered_data = all_data[all_data['Oxygen Level'] != 255]

# Display the size of filtered_data and the first few rows
#print(f"Size of filtered data: {filtered_data.shape}")
filtered_data.head()

# Calculate the baseline oxygen level
baseline_oxygen_level = filtered_data['Oxygen Level'].median()

# Identify the dips in oxygen level that are greater than 4% from the baseline
dips = (filtered_data['Oxygen Level'] < baseline_oxygen_level - 4)

# Display the baseline oxygen level and the first few values of dips
baseline_oxygen_level, dips.head()

# Count the number of dips
num_dips = np.sum((dips.diff() == 1) & dips)

# Calculate the total duration of sleep in hours
# First, convert the 'Time' column to datetime using .loc to avoid SettingWithCopyWarning
filtered_data.loc[:, 'Time'] = pd.to_datetime(filtered_data['Time'], format='%H:%M:%S %b %d %Y')
# Then calculate the duration from the first to the last timestamp
total_duration_hours = (filtered_data['Time'].max() - filtered_data['Time'].min()).total_seconds() / 3600

# Calculate the Oxygen Desaturation Index (ODI)
ODI = num_dips / total_duration_hours

# Display the number of dips, total duration in hours, and the ODI
num_dips, total_duration_hours, ODI



print(f"\n\nNumber of Dips: {num_dips}")
print('Total Duration of sleep in Hours: ' + str(total_duration_hours))
print(f"Oxygen Desaturation Index (ODI): {ODI} \n\n")



# Delete all files in the unzipped folder
# for filename in os.listdir(unzip_folder):
#     file_path = os.path.join(unzip_folder, filename)
#     # Make sure the file is not a directory
#     if os.path.isfile(file_path):
#         os.remove(file_path)


