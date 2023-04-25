import sanitize


# Create a class called Athlete with 2 method:
class Athlete:
    # Method 1: Ini a method that initiates 3 attributes and assigned to 3 class attributes using supplied argument data
    def __init__(self, name, DOB=None, records=[]):
        self.name = name
        self.dob = DOB
        self.record = records

    # Method 2: A method that return top 3 record for the attribute self.record
    def top_3(self):
        return sorted(set(sanitize.sanitize(t) for t in self.record))[0:3]

    # Method 3: Append a single additional timing to athlete's data
    def add_time(self,time_value):
        self.record.append(time_value)

    # Method 4: Append a list of additional timing to athlete's data
    def add_times(self,time_list):
        self.record.extend(time_list)

def get_data(filename):
    try:
        with open(filename) as file:
            temp_list = file.readline().strip().split(',')
            # Create object Athlete with 3 arguments
            return Athlete(temp_list.pop(0), temp_list.pop(0), temp_list)
    except IOError as err:
        print('Error' + str(err))
        return None

# Create object instances for each athlete
james = get_data('james2.txt')
julie = get_data('julie2.txt')
mikey = get_data('mikey2.txt')
sarah = get_data('sarah2.txt')

# Test method 3 and method 4
vera = Athlete('Vera Vi')
vera.add_time('1.31')
print(vera.top_3())
vera.add_times(['2.22', "1-21", '2:22'])
print(vera.top_3())

# Print out athlete's result:
print(james.name + "'s best records are: " + str(james.top_3()))
print(julie.name + "'s best records are: " + str(julie.top_3()))
print(mikey.name + "'s best records are: " + str(mikey.top_3()))
print(sarah.name + "'s best records are: " + str(sarah.top_3()))

