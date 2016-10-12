# problem2: print results based on the calculation that user input,like user enter '4 + 5',then we need print '4 + 5 = 9'
# input: 4 + 5
# output: 4 + 5 = 9

# input the calculation
num1, operator, num2 = input('Enter calculation: ').split()
# convert num1 num2 from strings to integer
num1 = int(num1)
num2 = int(num2)
# judge operator
if operator == '+':
    print('{} + {} = {}'.format(num1, num2, num1 + num2))
elif operator == '-':
    print('{} - {} = {}'.format(num1, num2, num1 - num2))
elif operator == '*':
    print('{} * {} = {}'.format(num1, num2, num1 * num2))
elif operator == '/':
    print('{} / {} = {}'.format(num1, num2, num1 / num2))
elif operator == '%':
    print('{} % {} = {}'.format(num1, num2, num1 % num2))
else:
    print('use either + - * / or % next time')

# 其他比较运算符: 大于>、小于 <、大于等于>=、小于等于<=、不等于!=