# About this program:
## - Take .csv files in the path: D:\P.Truong\Master Data\Masterdata\SKU\SKU - Store Update\csv converted as input

## - Categorizing file based on the file name, if HMP, or DD or TPCN exist in the file name, it would be put in equivalent category

## - Save SKU into arrays to check later, take the SKU file with category information and save each category

## - Open every input files, check every SKU in each row, ignore if it's not in the category, otherwise write into an output file.

import csv
import glob
import os
from datetime import date
import shutil

today = date.today()

# Create an array for saving all .csv file directory
directory_path = "C:\\Users\\Admins\\PycharmProjects\\Head_First_Py-master\\csv converted\\"
filenames = glob.glob(directory_path + '*.csv')
for i in range(len(filenames)):
    filenames[i] = filenames[i].replace(str(directory_path),'')

output_path = directory_path + 'output' + str(today) + '\\'
if os.path.exists(output_path):
    shutil.rmtree(output_path)
os.mkdir(output_path)

# Create arrays for categorizing file, a file would be in at least 1 array and can be in more than 1 array
Category = {'HMP': [], 'DD': [], 'TPCN': [], 'All': []}

# Create 3 array to categorizing SKUs:
SKU_HMP = []
SKU_TPCN = []
SKU_DD = []
with open(directory_path + 'SKU_NH-added.csv', 'r') as input_SKUs:
    reader = csv.DictReader(input_SKUs)
    for row in reader:
        if int(row['NH']) == 2:
            SKU_TPCN.append(row['ITEM'])
        elif int(row['NH']) == 3:
            SKU_HMP.append(row['ITEM'])
        elif int(row['NH']) == 4:
            SKU_DD.append(row['ITEM'])

# Categorizing Files
for filename in filenames:
    if filename.find("HMP") != -1:
        Category['HMP'].append(filename)
    if filename.find("TPCN") != -1:
        Category['TPCN'].append(filename)
    if filename.find("DD") != -1:
        Category['DD'].append(filename)
    if filename.find("HMP") == -1 and filename.find("TPCN") == -1 and filename.find("DD") == -1:
        Category['All'].append(filename)

master_data_file = ['SKU_NH-added.csv', 'StoreID.csv']
Category['All'] = [files for files in Category['All'] if files not in master_data_file]


# Open file and write an output to save result
for categories in Category:
    if categories == 'HMP':
        check_array = SKU_HMP
    elif categories == 'TPCN':
        check_array = SKU_TPCN
    elif categories == 'DD':
        check_array = SKU_DD
    else:
        check_array = SKU_DD + SKU_HMP + SKU_TPCN
    for files in Category[categories]:
        # Convert filename to include Store name only. Used for output name later.
        output_filename = 'Co.opMart ' + files.replace(" - HMP", '').replace(" - TPCN", '').replace(" - DD", '').replace('.csv','')
        with open(directory_path + "StoreID.csv", 'r') as StoreID_file:
            reader = csv.DictReader(StoreID_file)
            for row in reader:
                if row['STRNAM'] == output_filename:
                    output_filename = output_filename + ' ' + row['STRNUM'] + '.csv'
        # Open input and output file
        try:
            with open(directory_path + files, 'r', encoding='ISO-8859-1') as input_files, open(output_path + output_filename, 'a', newline='',
                                                                              encoding='ISO-8859-1') as output_files:
                reader = csv.DictReader(input_files)
                writer = csv.DictWriter(output_files, fieldnames=reader.fieldnames)
                for row in reader:
                    if row['ITEM'] in check_array:
                        writer.writerow(row)
        except IOError as err:
            print("Error in opening files" + str(err))
