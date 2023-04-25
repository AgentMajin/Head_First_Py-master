import pickle
import sys
man = []
other = []
def main():
    with open('sketch.txt') as file:
        for each_line in file:
            try:
                each_line.read
    # new_man = []
    # try:
    #     with open('output_man.txt','rb') as man_file:
    #        new_man = pickle.load(man_file)
    # except IOError:
    #    print('File error')
    # print_lol(new_man)

def print_lol(lst,indent = False,level=0,fh=sys.stdout):
    for each_item in lst:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fh)
        else:
            if indent:
                for levels in level:
                    print('\t',end='',file=fh)
            print(each_item,file=fh)

main()
