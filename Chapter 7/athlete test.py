import AthleteList
import athlete_model

list_file = ['james2.txt','julie2.txt','mikey2.txt','sarah2.txt']

data = athlete_model.put_to_store(list_file)
print(data)
data_2 = athlete_model.get_from_store()
print(data_2)

for each_line in data:
    print(data[each_line].name + " " + data[each_line].dob)