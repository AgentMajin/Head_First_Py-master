import pickle
import sys


def print_lol(lst, indent = False, level=0, fh=sys.stdout):
    for each_item in lst:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1, fh)
        else:
            if indent:
                for levels in level:
                    print('\t', end='', file=fh)
            print(each_item, file=fh)

with open('output_man.txt','rb') as man_file, open('output_other.txt','rb') as other_file:
    try:
        man = pickle.load(man_file)
        other = pickle.load(other_file)
    except IOError:
        print('IOError')
print_lol(man)
print_lol(other)