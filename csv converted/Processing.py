#-*-coding: utf-8-*-
import csv
import glob
import chardet


# Create an array for saving all .csv file directory
directory_path = "/Users/vuphitruong/Desktop/  /Head_First_Py-master/csv converted/"
filenames = glob.glob(directory_path + '/*.csv')

# Create arrays for categorizing file, a file would be in at least 1 array and can be in more than 1 array
Nganh_Hang = {'HMP':[],'DD':[],'TPCN':[],'All':[]}


# Create 3 array to categorizing SKUs:
SKU_HMP = []
SKU_TPCN = []
SKU_DD = []
with open(directory_path + 'SKU_NH-added.csv','r') as input_SKUs:
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
        Nganh_Hang['HMP'].append(filename)
    if filename.find("TPCN") != -1:
        Nganh_Hang['TPCN'].append(filename)
    if filename.find("DD") != -1:
        Nganh_Hang['DD'].append(filename)
    if filename.find("HMP") == -1 and filename.find("TPCN") == -1 and filename.find("DD") == -1:
        Nganh_Hang['All'].append(filename)

Nganh_Hang['All'].remove(directory_path+'SKU_NH-added.csv')
# for NH in Nganh_Hang:
#     print(NH)
#     for filenames in Nganh_Hang[NH]:
#         print(filenames)


# Open file and write an output to save result
for category in Nganh_Hang:
    if category == 'HMP':
        check_array = SKU_HMP
    elif category == 'TPCN':
        check_array = SKU_TPCN
    elif category == 'DD':
        check_array = SKU_DD
    else:
        check_array = SKU_DD + SKU_HMP + SKU_TPCN
    for files in Nganh_Hang[category]:
        # Convert filename to include Store name only. Used for output name later.
        output = files.replace(" - HMP",'').replace(" - TPCN",'').replace(" - DD",'').replace('csv converted/','csv converted/output/')
        # Open input and output file
        try:
            with open(files,'r',encoding='ISO-8859-1') as input_files, open(output,'w',newline='',encoding='ISO-8859-1') as output_files:
                reader = csv.DictReader(input_files)
                writer = csv.DictWriter(output_files,fieldnames=reader.fieldnames)
                for row in reader:
                    if row['ITEM'] in check_array:
                        writer.writerow(row)
        except IOError as err:
            print("Error in opening files" + str(err))


