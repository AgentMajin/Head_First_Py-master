import csv
import glob
import os
from datetime import date, datetime
import shutil

# Global:
working_directory = "/Users/vuphitruong/Desktop/  /Head_First_Py-master/csv converted/"


# This function return a list of csv file in the directory that user input, or the csv file of a specific Store
def get_filenames(directory, storename = ''):
    filenames = glob.glob(directory + storename + '*.csv')

    for i in range(len(filenames)):
        filenames[i] = filenames[i].replace(directory, '')
    return filenames


# This function categorizing files and return a dictionary that include 3 element, each element stand for a category
# and include a list of .csv file that belong to the category. For ex: file Binh Tan 2 - HMP would be categorized into
# the category 'HMP'.
def categorized_filename(filename_list, category_1='HMP', category_2='TPCN', category_3='DD', master_data1=None,
                         master_data2=None, other='All'):
    categories = {category_1: [], category_2: [], category_3: [], 'All': []}
    master_data = [master_data2, master_data1]

    for filename in filename_list:
        if filename.find(category_1) != -1:
            categories[category_1].append(filename)
        if filename.find(category_2) != -1:
            categories[category_2].append(filename)
        if filename.find(category_3) != -1:
            categories[category_3].append(filename)
        if filename.find(category_1) == -1 and filename.find(category_2) == -1 and filename.find(category_3) == -1:
            categories[other].append(filename)

    categories[other] = [files for files in categories[other] if files not in master_data]

    return categories


# This function take the list of SKU as input and divide it into 3 array which stand for 3 category
def get_categorized_skus(SKU_directory, category_1='HMP', category_2='TPCN', category_3='DD'):
    SKU = {category_1: [], category_2: [], category_3: []}
    with open(SKU_directory + 'SKU_NH-added.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row['NH']) == 3:
                SKU[category_1].append(row['ITEM'])
            elif int(row['NH']) == 2:
                SKU[category_2].append(row['ITEM'])
            elif int(row['NH']) == 4:
                SKU[category_3].append(row['ITEM'])

    return SKU


def get_storeid(store_name, data_direc):
    store_name = 'Co.opMart ' + store_name.replace(" - HMP", '').replace(" - TPCN", '').replace(" - DD", '').replace('.csv', '')
    with open(data_direc,'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['STRNAM'] == store_name:
                return row['STRNUM']
        return "Can't get StoreID"
# This function create a folder for saving output, the rule for setting output name is: output + mmddyy hh:mm
def make_output_folder(directory, filename = ''):
    now = datetime.now().strftime("%m%d%y")
    output_folder = directory + ' output ' + str(now) + '/'
    if os.path.exists(output_folder):
        pass
    else:
        os.mkdir(output_folder)

    if filename == '':
        return output_folder
    else:
        store_folder = output_folder + 'Co.opMart ' + filename.replace(" - HMP", '').replace(" - TPCN", '').replace(" - DD", '').replace('.csv', '') + '/'
        if os.path.exists(store_folder):
            pass
        else:
            os.mkdir(store_folder)
        return store_folder


# This function check and return the array of SKUs that have matching category with the file we input
def check_sku_array(category, SKU, category_1='HMP', category_2='TPCN', category_3='DD'):
    categories = [category_1, category_2, category_3]
    for element in categories:
        if category == element:
            check_array = SKU[element]
            return check_array
    check_array = SKU[category_1] + SKU[category_2] + SKU[category_3]
    return check_array


# This function return the name for output file, the output file would be as follows: 'Co.op Mart' + StoreName + StoreID
# + .csv
# def make_output_filename(input_filename,StoreID_directory):
#     input_filename = 'Co.opMart ' + input_filename.replace(" - HMP", '').replace(" - TPCN", '').replace(" - DD", '').replace('.csv', '')
#     storeid = get_storeid(input_filename,StoreID_directory)
#     input_filename = input_filename + ' ' + storeid + '.csv'
#     return input_filename


if __name__ == '__main__':
    if os.path.exists(working_directory + ' output ' + str(datetime.now().strftime("%m%d%y"))):
        shutil.rmtree(working_directory + ' output ' + str(datetime.now().strftime("%m%d%y")))
    processing_stores_path = {}
    files_dictionary = categorized_filename(get_filenames(working_directory),master_data1='SKU_NH-added.csv',master_data2='StoreID.csv')
    SKU_dictionary = get_categorized_skus(working_directory)
    for keys in files_dictionary:
        if len(files_dictionary[keys])>0:
            check_array = check_sku_array(keys,SKU_dictionary)
        for files in files_dictionary[keys]:
            # Convert filename to include Store name only. Used for output name later.
            output_folder = make_output_folder(working_directory,files)
            storeid = get_storeid(files,working_directory + 'StoreID.csv')
            output_filename_path = output_folder + storeid +'.csv'
            try:
                with open(working_directory + files, 'r', encoding='ISO-8859-1') as input_files, open(output_filename_path, 'a', newline='',
                        encoding='ISO-8859-1') as output_files:
                    reader = csv.DictReader(input_files)
                    writer = csv.DictWriter(output_files, fieldnames=reader.fieldnames)
                    writer.writeheader()
                    for row in reader:
                        if row['ITEM'] in check_array:
                            writer.writerow(row)
                if storeid in processing_stores_path:
                    pass
                else:
                    processing_stores_path.update({storeid: output_filename_path})
            except IOError as err:
                print("Error in opening files" + str(err))

    # for store in processing_stores_path:
    #     with open(working_directory + 'sourcing/sourcing_discontinued_sku.csv','r',encoding = 'ISO-8859-1') as sourcing_original, open(processing_stores_path[store],'r',encoding = 'ISO-8859-1') as store_data,open(processing_stores_path[store].replace(store,'') + 'sourcing output','a',encoding = 'ISO-8859-1') as sourcing_output:
    #         reader1 = csv.DictReader(sourcing_original)
    #         reader2 = csv.DictReader(store_data)
    #         writer = csv.DictWriter(sourcing_output,fieldnames=reader1.fieldnames)
    #         writer.writeheader()
    #         for store_data_row in reader2:
    #             if store_data_row['STATUS'] == 'N':
    #                 sourcing_original.seek(0)
    #                 for sourcing_data_row in reader1:
    #                     if sourcing_data_row['*Item'] == store_data_row['ITEM'] and sourcing_data_row['*Dest'] == store:
    #                         writer.writerow(sourcing_data_row)

    for store_output in processing_stores_path:
        with open(working_directory + 'sourcing/sourcing_discontinued_sku.csv','r',encoding='ISO-8859-1') as sourcing_file, open(processing_stores_path[store_output].replace(store_output+'.csv','' )+'sourcing.csv', 'a',encoding='ISO-8859-1') as sourcing_store:
            reader = csv.DictReader(sourcing_file)
            writer = csv.DictWriter(sourcing_store,fieldnames=reader.fieldnames)
            writer.writeheader()
            for source_rows in reader:
                if source_rows['*Dest'] == store_output:
                    writer.writerow(source_rows)

        with open(processing_stores_path[store_output], 'r', encoding='ISO-8859-1') as store_data, open(
                    processing_stores_path[store_output].replace(store_output + '.csv', '') + 'sourcing.csv', 'r',
                    encoding='ISO-8859-1') as sourcing_store, open(working_directory + 'sourcing/' +'sourcing-output.csv', 'a',encoding='ISO-8859-1') as output_source:
            reader1 = csv.DictReader(store_data)
            reader2 = csv.DictReader(sourcing_store)
            writer = csv.DictWriter(output_source,fieldnames=reader2.fieldnames)
            writer.writeheader()
            for store_data_rows in reader1:
                if store_data_rows['STATUS'] == 'N':
                    sourcing_store.seek(0)
                    for sourcing_rows in reader2:
                        if sourcing_rows['*Item'] == store_data_rows['ITEM'] and sourcing_rows['Disc'] == '':
                            sourcing_rows['Disc'] = str(datetime.now().strftime("%m/%d/%y")) + ' 12:00 AM'
                            sourcing_rows['UDC_NOTE_DISC'] = 'KHONG THUOC DANH MUC CM KINH DOANH'
                            writer.writerow(sourcing_rows)


