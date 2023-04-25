import sanitize

try:
    with open('james.txt') as james_file:
        james = james_file.readline().strip().split(',')

    with open('julie.txt') as julie_file:
        julie = julie_file.readline().strip().split(',')

    with open('mikey.txt') as mikey_file:
        mikey = mikey_file.readline().strip().split(',')

    with open('sarah.txt') as sarah_file:
        sarah = sarah_file.readline().strip().split(',')

except IOError as err:
    print('Error' + str(err))

print(sorted(set(sanitize.sanitize(time) for time in james))[0:3])
print(sorted(set(sanitize.sanitize(time) for time in julie))[0:3])
print(sorted(set(sanitize.sanitize(time) for time in mikey))[0:3])
print(sorted(set(sanitize.sanitize(time) for time in sarah))[0:3])


