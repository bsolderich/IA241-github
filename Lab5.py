"""
lab5
"""

#3.1

alien_color = 'red'

if alien_color == 'green' :
    print('You have earned 5 points')
    
#3.2

alien_color = 'red'

if alien_color == 'green' :
    print('You have earned 5 points')
    
else: 
    print('You have earned 10 points')
    
#3.3

favorite_fruits=['pineapple','mango','apple']

if 'pineapple' in favorite_fruits:
    print('pineapple is delicious')
    
if 'banana' in favorite_fruits:
    print('you really enjoy bananas')
    
if 'apple' in favorite_fruits:
    print('apples are my favorite too')
    
#3.4

age = 75

if age <10:
    print('kid')
    
elif age >=10 and age <20:
    print('teenager')
    
else: 
    print('adult')
    
    if age>= 65:
        print('elder')