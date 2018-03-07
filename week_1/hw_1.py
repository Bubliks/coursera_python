import sys

string = sys.argv[1]
num = 0
for str in string:
    num += int(str)

print(num)