print("Double Quote: Hello World!")
print('Single Quote: Hello World!')

print('*' * 10)

multiline_var = '''
Hi Rajan,

All the best for the interview.

Best,
Rajan

'''

print(multiline_var)

price = 10
price = 20
rating = 4.5
print(rating + price)

is_published = True

print(is_published + price)

full_name = 'Rajan Vyas'
age = 40
is_new = True

# print(full_name+"'s age is " + age +' ' +  is_new)

person_name = input('Enter your name: ')
fav_color = input('Enter your favorite color: ')
print(person_name + ' likes ' + fav_color + ' color')

#Calculate Age
birth_year = input('Enter your birth year: ')
age = 2024 - int(birth_year)
print(age)

weight = input('Enter your weight in Pound: ')
print(type(weight))
print(int(weight) * 0.45)

test = 'This is "test string"'
sub_test1 = test[8:-1]
print(sub_test1)

formatted_Str = f'{person_name} likes {fav_color} color - Huhhaaaaa'
print(formatted_Str)
print(formatted_Str.upper() + ' --> UPPER CASE')
print(formatted_Str.lower() + ' --> lower Case')
print(str(formatted_Str.find('likes')) + ' -- Index of likes')
print(str(formatted_Str.find('k')) + ' -- Index of l')
print(formatted_Str.find('likes'))
print(f'Length of {formatted_Str} is {len(formatted_Str)}')
print(f'Length of {formatted_Str} is {str(len(formatted_Str))}')
print(formatted_Str.replace('Red','Only Red'))
print(f'Like exist in {formatted_Str}? ' + str('Like' in formatted_Str))
print(f'like exist in {formatted_Str}? ' + str('likes' in formatted_Str))
print('Rajan' in formatted_Str)
print('rajan' in formatted_Str)
print(formatted_Str.title())