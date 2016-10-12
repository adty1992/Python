# 输入两个内容存储在变量num1 num2
num1, num2 = input('Enter num1 num2: ').split(',')
# 将输入的字符串转变成整数
num1 = int(num1)
num2 = int(num2)
# 计算和存在变量sum中
sum = num1 + num2
# 计算差存在变量difference中
difference = num1 - num2
# 计算乘存在变量product中
product = num1 * num2
# 计算除存在变量quotient中
quotient = num1 / num2
# 取余存在变量reminder中
reminder = num1 % num2
# 打印
print('{} + {} = {}'.format(num1, num2, sum))
print('{} - {} = {}'.format(num1, num2, difference))
print('{} * {} = {}'.format(num1, num2, product))
print('{} / {} = {}'.format(num1, num2, quotient))
print('{} % {} = {}'.format(num1, num2, reminder))
