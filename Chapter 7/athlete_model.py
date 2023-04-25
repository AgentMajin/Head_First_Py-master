import pickle
# Get the class def
from AthleteList import Athlete


# Same functin as previous code file
def get_file(filename):
    try:
        with open(filename) as file:
            temp = file.readline().strip().split(',')
            return Athlete(temp.pop(0), temp.pop(0), temp)
    except IOError as err:
        print('File error' + str(err))


# A function that take a list of file as an argument and return a pickle with all data stored in a dictionary
def put_to_store(file_list):
    all_athlete = {}
    for file in file_list:
        ath_class = get_file(file)
        all_athlete[ath_class.name] = ath_class
    try:
        with open('athletes.pickle.txt','wb') as ath_pickle:
            pickle.dump(all_athlete,ath_pickle)
    except IOError as err:
        print('Error in writing pickle file' + str(err))
    return all_athlete


# A function to open the pickle file and return a dictionary of athletes
def get_from_store():
    all_athlete = {}
    try:
        with open('athletes.pickle.txt','rb') as pickle_file:
            all_athlete = pickle.load(pickle_file)
    except IOError as err:
        print('Error in reading pickle file' + str(err))
    return all_athlete


