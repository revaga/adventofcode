""""import re

f = open("input1-1.txt")
print(f.readline())
temparr = []
temparr = re.split("   ", f.readline())
arrofall = []
arrofall.append(int(temparr[0]))
arrofall.append(int(temparr[1]))


f.close()

print(arrofall)
"""

array1 = []
array2 = []

# Open the input file and read line by line
with open('input1-1.txt', 'r') as file:
    for line in file:
        # Strip whitespace and split the line into two numbers
        parts = line.strip().split()
        if len(parts) == 2:
            num1, num2 = map(int, parts)
            array1.append(num1)
            array2.append(num2)

#Part 1
"""
array1.sort()
array2.sort()

sum = 0

while len(array1) > 0:
    sum = sum + abs(array1[0] - array2[0])
    array1.remove(array1[0])
    array2.remove(array2[0])

print(sum)
"""

#Day1 part 2

dictofnum = {}
sum = 0
for i in range(len(array1)):
    if array1[i] in dictofnum:
        sum = sum + dictofnum[array1[i]]
    else:
        k = 0
        newnum = 0
        while array1[i] in array2[k:]:
           # print(array2[k:])
            k = k + array2[k:].index(array1[i]) + 1
            newnum = newnum + 1
        dictofnum[array1[i]] = newnum * array1[i]
        sum = sum + (newnum * array1[i])

print(sum)



dictofnum = {}
sum = 0
for i in range(len(array1)):
    if array1[i] in dictofnum:
        sum = sum + dictofnum[array1[i]]
    else:
        newnum = array2.count(array1[i])
        sum = sum + (newnum * array1[i])

print(sum)





