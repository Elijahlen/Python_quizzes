# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
# 
# Written by Eric Martin for COMP9021


import os


first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

tallies = {'F': {}, 'M': {}}
records = {'F': {}, 'M': {}}
for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3: 7])
    with open(directory + '/' + filename, 'r') as file:
        for gender in {'F', 'M'}:
            tallies[gender][year] = 0           
        for line in file:
            name, gender, count = line.split(',')
            count = int(count)
            tallies[gender][year] += count
            if name == first_name:
                records[gender][year] = count
frequencies = dict.fromkeys('M', 'F')
for gender in {'F', 'M'}:
    frequencies[gender] = [(records[gender][year] * 100 / tallies[gender][year], year)
                                                                         for year in records[gender]
                          ]
    frequencies[gender].sort(reverse = True)
if frequencies['F']:
    min_female_frequency, female_first_year = frequencies['F'][0][0], frequencies['F'][0][1]
if frequencies['M']:
    min_male_frequency, male_first_year = frequencies['M'][0][0], frequencies['M'][0][1]
if not female_first_year:
    print(f'In all years, {first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a female name first in the year {female_first_year}.\n'
          f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
         )
if not male_first_year:
    print(f'In all years, {first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a male name first in the year {male_first_year}.\n'
          f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
         )

