"""
This is Just email slicer + Validation; That's All :)
"""
from validate_email import validate_email
import re

Email = input('Please Enter Your Email: ')
is_valid = validate_email(Email, verify=True)
if is_valid: print('Email is Correct')
else: print('Not Valid Email')

if is_valid:
    St = input('Do you want me slice it?(y or n) ')
    if St == 'y':
        ls = re.split('@', Email)
        print('Domain: {}'.format(ls[0]))
        print('Server: {}'.format(ls[1]))
