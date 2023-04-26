import csv
import glob
import os
from datetime import date
import shutil

# Global:
working_directory = "C:\\Users\\Admins\\PycharmProjects\\Head_First_Py-master\\csv converted\\"


def get_filenames(directory):
    filenames = glob.glob(directory + '*.csv')

    for i in range(len(filenames)):
        filenames[i] = filenames[i].replace(directory, '')
    return filenames


def categorizing_filename(filename_list, category_1=None, category_2=None, category_3=None, master_data1=None,
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
            categories['All'].append(filename)

    categories['All'] = [files for files in categories['All'] if files not in master_data]

    return categories


def get_categorized_skus(directory, category_1=None, category_2=None, category_3=None)
if __name__ == '__main__':
    A = get_filenames(working_directory)
    print(categorizing_filename(A, 'HMP', 'DD', 'TPCN', 'SKU_NH-added.csv'))
