text = input()
print('f("' + text + '") == "', end = ' ')
s = text.split(' ')
for i in s:
    print(i[::-1], end = ' ')

print('"')