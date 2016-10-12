# problem1: convert miles to kilometers , kilometers = miles * 1.60934
# input miles and assign it to variable miles
miles = input('Enter miles: ')
# convert from string to integer
miles = int(miles)
# perfom calculation
kilometers = 1.60934 * miles
# print results using format
print('{} miles equals {} kilometers!'.format(miles, kilometers))


