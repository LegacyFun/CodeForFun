"""
This is Rock, Paper, Scissor Game With Computer
Way too easy !!! :)
But with LITTLE BIT OF bitwise / sound Better!
"""


def winner(first, second):
    if first == second:
        return 'Draw'
    if ((first | (1 << 2)) - second) % 3:
        return 'First Person :)'
    return 'Second Person :)'


while True:
    First = int(input('Please enter First person Choice: (0 Rock, 1 Paper, 2 Scissor)\n'))
    Second = int(input('Please enter First person Choice: (0 Rock, 1 Paper, 2 Scissor)\n'))
    print(winner(First, Second))
    if input("Wanna Play again? y or n ") == 'n':
        break

print('Thanks, Have fun!!')
