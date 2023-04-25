# 2 ways to initiate a dictionary
best_rockband = {}
Beatles = dict()
# Checking type of a variable:
print(type(best_rockband))
# Output: <class 'dict'>
print(type(Beatles))
# Output: <class 'dict'>

# Adding elements into a dictionary
best_rockband['Name'] = 'John Lennon'
best_rockband['Occupation'] = ['singer','song composer','actor']
Beatles = {'Name': 'Paul McCartney', 'Occupation':['song composer','Beatles\' leader', 'actor','leader']}

# Accessing data in dictionaries. "-1" means the last element in the list, -2: the second last element,...
print(best_rockband['Name'])
# Output: John Lennon
print(Beatles['Occupation'][-1])
# Output: leader

# A dictionary can grow dynamically to store additional value:
best_rockband['Member'] = "4"
Beatles['Best songs'] = ['Yesterday','Let it be','Hey jude']

print(best_rockband)
print(Beatles)
