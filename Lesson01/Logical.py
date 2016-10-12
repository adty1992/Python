# input age, judge important or not
# 1-18, 21, 35, >=65 is important; others is not important
# Logical : 与(and)、或(or)、非(not)


age = input('Enter age: ')
age = int(age)

if (age >= 1) and (age <= 18):
    print('important')
elif (age == 21) or (age == 35):
    print('important')
elif not (age < 65):
    print('important')
else:
    print('not important')