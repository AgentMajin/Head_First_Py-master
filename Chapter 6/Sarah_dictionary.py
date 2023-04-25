import sanitize

sarah_dict = sanitize.get_data('sarah2.txt')
print(sarah_dict['Name'] + "'s fastest records are: " + str(sarah_dict['Records']))