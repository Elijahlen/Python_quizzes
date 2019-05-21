# Written by Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''


import sys
from math import gcd


try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''

the_gcd = gcd(numerator, denominator)
the_numerator = numerator // the_gcd
the_denominator = denominator // the_gcd
denominator_1 = the_denominator
for divisor in 2, 5:
    while not denominator_1 % divisor:
        denominator_1 //= divisor
has_finite_expansion = denominator_1 == 1

integral_part = numerator // denominator
numerator_1 = numerator % denominator
numerators = [0]
decimal_expansion = []
while True:
    try:
        tau_start_index = numerators.index(numerator_1)
        break
    except ValueError:
        numerators.insert(-1, numerator_1)
        numerator_1 *= 10
        decimal_expansion.append(numerator_1 // denominator)
        numerator_1 %= denominator
sigma = ''.join(str(d) for d in decimal_expansion[: tau_start_index])
tau = ''.join(str(d) for d in decimal_expansion[tau_start_index: ])

if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator} / {denominator} = {integral_part}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
    print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')

    
    



    
