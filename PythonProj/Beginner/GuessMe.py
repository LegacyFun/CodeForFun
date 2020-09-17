import random

a, b = map(int, input('Set you Suitable rang a -> b: ').split())
x = random.randint(a, b)
State = False
print('Now Start to Guess :)')
while not State:
    Guessed = int(input())
    if Guessed < x:
        print('Higher')
    elif Guessed > x:
        print('lower')
    else:
        print('Fabulous you Got it')
        State = True
