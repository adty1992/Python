# input user investment amount and expected interset rate
# each year their investment will increase by their "investment + investment * interest rate"
# print out the earnings after a 10 years period


investment, interest_rate = input('input investment amout and interest rate: ').split()
# convert the value to a float and round the percentage rate by 2 digits
investment = float(investment)
interest_rate = float(interest_rate) * 0.01

for i in range(10):
    investment = investment + (investment * interest_rate)

# output the results with 2 decimals
print('afger 10 years, the earnings is : {:.2f}'.format(investment))