import pandas as pd
import os
import subprocess
import re
import glob

data = pd.read_csv("C:\\Users\\jdobkin\\Downloads\\Data_Catalog_Data_Dictionary (1).csv", encoding='windows-1252')
newid = pd.read_csv("C:\\Users\\jdobkin\\Documents\\GitHub\\little-lexicographer\\new_data_dicts.csv", encoding='windows-1252')

data2 = pd.merge(data, newid, on=['dataset_id', 'dataset_id'])

data2.to_csv("C:\\Users\\jdobkin\\Documents\\GitHub\\little-lexicographer\\out.csv")