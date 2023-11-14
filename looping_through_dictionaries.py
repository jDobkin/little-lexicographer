import pandas as pd
import os
import subprocess
import re
import glob

# Read the CSV file
data = pd.read_csv("C:\\Users\\jdobkin\\Documents\\GitHub\\little-lexicographer\\out.csv", encoding='windows-1252')

# Get the unique values in the column that will be used to separate the data
unique_values = data['resource_id'].unique()

## Loop through the unique values and create a CSV file for each one
for value in unique_values:
    # Create a new DataFrame containing only the rows with the current unique value, without the 'resource_id' column
    filtered_data = data[data['resource_id'] == value].drop(columns=['resource_id'])
    
    # Export the filtered DataFrame to a new CSV file
    filename = f'{value}.csv'
    filtered_data.to_csv(filename, index=False)

    # Print the file path of the exported CSV file
    print(f'{os.getcwd()}/{filename} created')

folder_path = "C:\\Users\\jdobkin\\Documents\\GitHub\\little-lexicographer\\tp_dicts"
script_path = "C:\\Users\\jdobkin\\Documents\\GitHub\\little-lexicographer\\upload_data_dictionary.py"

csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
for f in csv_files:
      
    # read the csv file
    df = pd.read_csv(f)
      
    # print the location and filename
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])

    resource_id = os.path.splitext(os.path.basename(f))[0]  
    # print the content
    print('Resource id:')
    print(resource_id)
    subprocess.run(['python', script_path, f"{f}", f'{resource_id}'])