import math

print(math.floor(2.999))
x = (2 + 3) * 10 - 3
print(x)

house_Price = 1000000
good_credit = False

if good_credit:
    print('Buyer has to put 10% Down Payment: $' + str(house_Price*0.10))
else:
    print('Buyer has to put 20% Down Payment: $' + str(house_Price*0.20))

has_good_credit = True
has_criminal_record = True
has_high_income = False
has_exceptional_credit = False

if has_high_income and has_good_credit and not has_criminal_record or has_exceptional_credit:
    print('Eligible for loan')
else:
    print('Not Eligible for loan')

name = 'Rajan Vyas'
if len(name) <= 2:
    print('Name must be at least 3 characters long')
elif len(name) >= 51:
    print('Max length of Name should be 50 characters long')
else:
    print('Name looks good!')