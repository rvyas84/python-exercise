weight = int(input('Enter your weight: '))
weight_unit = input('(L)bs or (K)g: ')

if weight_unit == 'L' or weight_unit == 'l':
    weight = float(weight*0.45)
    print(f'You are {weight} kilos.')
elif weight_unit == 'K' or weight_unit == 'k':
    weight = float(weight/0.45)
    print(f'You are {weight} pounds.')
else:
    print('Incorrect Weight Unit')

# Guess Game
secret_num = 9
guess_limit = 3
guess_count = 0

while  guess_count < guess_limit:
    guess_input = int(input('Guess: '))
    guess_count += 1
    if guess_input == secret_num:
        print('You win!')
        break
else:
    print('Sorry, You failed!')

# Car Game

car_state = ""
car_started = False
while True:
    car_state = input('> ').lower()

    if car_state == 'start':
        if car_started:
            print('Car Already Started...')
        else:
            car_started = True
            print('Car started... Ready to go!')
    elif car_state == 'stop':
        if not car_started:
            print('Car already stopped.')
        else:
            car_started = False
            print('Car Stopped.')
    elif car_state == 'quit':
        break
    elif car_state == 'help':
        print ('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    else:
        print('Incorrect input')

# For Look Exercise

prices = [10, 20, 30]
total = 0;

for price in prices:
    total += price;
print(f"Total: {total}")

input = 'Python'
for item in input:
    print(item)

for i in range(5, 10, 2):
    print(i)

for i in range (10):
    print(i)

for i in range(5,10):
    print(i)

#Nested For Loop

number = [5,2,5,2,2]
for i in number:
    output = ''
    for j in range(i):
        output += 'X'
    print(output)


# Find largest number in a list

num_list = [19,2,4,5,7,9,11,99,19,2,5,7,9]
max_num = 0

for i in num_list:
    if max_num < i:
        max_num = i

print(f'Max Number is: {max_num}')

# Print Matrix

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for item in row:
        print(item)

num_list.append(99)
print(f'Updated NUM_LIST: {num_list}')
print(f'index of 99 is {num_list.index(99)}')
print(50 in num_list)
print(f'Count of 99 is {num_list.count(99)}')
num_list.sort()
print(f'Sorted Numer List: {num_list}')
num_list.reverse()
print(f'Sorted Numer List: {num_list}')

uniques = []

for item in num_list:
    if item not in uniques:
        uniques.append(item)
print(uniques)

for item in num_list:
    count = num_list.count(item)
    if count > 1:
        for j in range(1, count):
            num_list.remove(item)

print(num_list)

tupper = (1,3,5,2,4,6,9)
print(tupper[0])

print("Tupple Elements")

for i in tupper:
    print(i)