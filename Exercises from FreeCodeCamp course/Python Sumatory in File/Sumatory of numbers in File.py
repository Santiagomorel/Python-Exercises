
from asyncore import read
import re

name = 'data.txt'
handle = open(name)
count = 0
sumatory = list()
for line in handle:
    numbers = re.findall('[0-9]+',line)
    if numbers == []: continue
    for number in numbers:
        sumatory.append(int(number))

print(sum(sumatory))
