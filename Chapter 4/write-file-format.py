import sys
import pickle

def main():
    man = []
    other = []
    try:
        with open('sketch.txt') as file:
            for each_line in file:
                try:
                    (role,spoken_line) = each_line.split(':',1)
                    if role == 'Man':
                        man.append(spoken_line)
                    elif role == 'Other Man':
                        other.append(spoken_line)
                except ValueError:
                    pass
    except IOError as error:
        print('Missing file ' + str(error))

    try:
        with open('output_man.txt','wb') as man_file, open('output_other.txt', 'wb') as other_file:
            pickle.dump(man,man_file)
            pickle.dump(other,other_file)
    except pickle.PickleError as error:
        print('Cannot Open' + str(error))

# def print_lol(lst,indent = False,level=0,fh=sys.stdout):
#     for each_item in lst:
#         if isinstance(each_item,list):
#             print_lol(each_item,indent,level+1,fh)
#         else:
#             if indent:
#                 for levels in level:
#                     print('\t',end='',file=fh)
#             print(each_item,file=fh)

main()
