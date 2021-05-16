'''Date: 16/05/2021
ake as input str, a string. Write a recursive function which returns a new string in which all duplicate consecutive characters are reduced to a single char. E.g. for “hello” return “helo”. Print the value returned.'''

s = input()
l = []
p = ''
for i in range(len(s)):
    if s[i] not in l:
        l.append(s[i])
        p = p + s[i]
    else:
        continue
print(p)