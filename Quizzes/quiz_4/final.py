import os
from collections import defaultdict

first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

Female_dictionary = defaultdict(list)
Male_dictionary = defaultdict(list)
year_dictionary = defaultdict(list)
for file in sorted(os.listdir(directory)):
    if not file.endswith('.txt'):  #判断文件扩展名 尽量用 if not
        continue
    year = int(file[3:7])   #字符串也可以切片遍历
    Female_Sum = 0
    Male_Sum = 0
    with open(directory + '/' + file) as data_file:
        for line in data_file:
            _,gender,count = line.split(',') #注意split的用法
            count = int(count)
            if gender == 'F':
                Female_Sum = Female_Sum + count
            if gender == 'M':
                Male_Sum = Male_Sum + count
    year_dictionary[year].append([Female_Sum,Male_Sum])
for file in sorted(os.listdir(directory)):
    if not file.endswith('.txt'):
        continue
    year = int(file[3:7])
    with open(directory + '/' + file) as data_file:
        for line in data_file:           
            name,gender,amount = line.split(',')
            amount = int(amount)
            if gender == 'F':
                Female_dictionary[name].append([amount/year_dictionary[year][0][0],year])
            if gender == 'M':
                Male_dictionary[name].append([amount/year_dictionary[year][0][1],year])
for name in Female_dictionary:
    Female_dictionary[name].sort(reverse = True)
for name in Male_dictionary:
    Male_dictionary[name].sort(reverse = True)
    
FAcc = 0
for name in Female_dictionary:
    if first_name == name :
        FAcc = FAcc + 1
    else:
        continue
if FAcc == 1: 
    female_first_year = Female_dictionary[first_name][0][1]
    min_female_frequency = Female_dictionary[first_name][0][0]*100
    
MAcc = 0
for name in Male_dictionary:
    if first_name == name :
        MAcc = MAcc + 1
    else:
        continue
if MAcc == 1: 
    male_first_year = Male_dictionary[first_name][0][1]
    min_male_frequency = Male_dictionary[first_name][0][0]*100   


    
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

