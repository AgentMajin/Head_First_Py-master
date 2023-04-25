import csv
import glob


# Create an array for saving all .csv file directory
directory_path = "/Users/vuphitruong/Desktop/  /Head_First_Py-master/csv converted/"
filenames = glob.glob(directory_path + '/*.csv')

# Create arrays for categorizing file, a file would be in at least 1 array and can be in more than 1 array
Nganh_Hang = {'HMP':[],'DD':[],'TPCN':[],'All':[]}

# Categorizing Files
for filename in filenames:
    if filename.find("HMP") != -1:
        Nganh_Hang['HMP'].append(filename)
    if filename.find("TPCN") != -1:
        Nganh_Hang['TPCN'].append(filename)
    if filename.find("DD") != -1:
        Nganh_Hang['DD'].append(filename)
    if filename not in Nganh_Hang:
        Nganh_Hang['All'].append(filename)

for category in Nganh_Hang:
    for files in Nganh_Hang[category]:
        output = files.replace(" - HMP",'').replace(" - TPCN",'').replace(" - DD",'')
        with open(files) as input_files, open(output) as ouput_files:
            reader = csv.DictReader(input_files)
            writer = csv.DictWriter(output)
            for row in reader:
                if row['SKU']
