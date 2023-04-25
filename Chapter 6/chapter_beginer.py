import sanitize

sarah = sanitize.get_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)

print(sarah_name + "'s top 3 record are:" + str(sorted(set(sanitize.sanitize(time) for time in sarah))[0:3]))
