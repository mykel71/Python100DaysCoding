### https://ascii.co.uk/art

import random

# random_integer = random.randint(1,10)
# print(random_integer)

random_number_0_to_1 = random.random() ## Known as semi open range
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)


### Create a program that prints out Heads or Tails

print('Welcome to the game!')
choice_one = input('Choose "Head" or "Tail":').lower()
random_side = random.randint(1, 2)

if choice_one == 'head':
    if random_side == 1:
        print('Head, You won the game!')
    else:
        print('Tail, You lost!')
elif choice_one == 'tail':
    if random_side == 2:
        print('Tail, You won the game!')
else:
    print('Tail, You lost!')


# Lists - Data Structure

states_of_america = ['Delta', 'Delware', 'Pennyslavia', 'Gweru']
print(random.choice(states_of_america))
print(states_of_america[0])

states_of_america[3] = 'Centurion'
print(states_of_america[3])

states_of_america.append('Masvingo')
states_of_america.extend('Masvingo Netara')

print(states_of_america)

states_of_america = ['Delta', 'Delware', 'Pennyslavia', 'Gweru']

number_of_states = len(states_of_america)

print(number_of_states)
print(states_of_america[number_of_states - 1])


# Banker Roulette Game:

Friends = ['Michael', 'Symantha', 'Asa', 'Zoe', 'Mael']

print(random.choice(Friends))


# if we need more at once

random_index = random.randint(0,4)
print(Friends[random_index])

# Nested List

fruits = ['Strawberries', 'Nectarines', 'Apples', 'Pearls', 'Peaches', 'Cherry']
vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery']

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

