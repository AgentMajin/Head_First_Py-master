import sanitize


class Athlete(list):
    def __init__(self, name, dob=None, records=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(records)

    def top_3(self):
        return sorted(set(sanitize.sanitize(t) for t in self))[0:3]


def get_file(filename):
    try:
        with open(filename) as file:
            temp = file.readline().strip().split(',')
            return Athlete(temp.pop(0), temp.pop(0), temp)
    except IOError as err:
        print('File error' + str(err))


sarah = get_file('sarah2.txt')
print(sarah.name + "best 3 records are: " + str(sarah.top_3()))

new_record = Athlete("Violet")
new_record.extend(["1:2", "4:3", "1-1"])
print(new_record.name)
print(new_record.top_3())
