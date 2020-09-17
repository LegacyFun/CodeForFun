"""
This is Program just do a simple Dice Gen so ... yeh
"""
import random

print("let's Roll it")
while True:
    Dice = random.randint(1, 6)
    print('Your dice is showing {}'.format(Dice))
    st = input('Do you wanna roll again?(y or n): ')
    if st != 'y': break
print('Thank you For Using this Program. Have Fun!!')
