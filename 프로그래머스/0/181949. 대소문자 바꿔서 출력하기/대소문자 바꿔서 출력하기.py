str = input()
new_str = ''
for s in range(len(str)):
    if (str[s].islower()):
        new_str += str[s].upper()
    else:
        new_str += str[s].lower()
print(new_str)