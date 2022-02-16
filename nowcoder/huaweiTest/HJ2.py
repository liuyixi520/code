s = input()
c = input()
s = s.upper()
c = c.upper()
count = 0
for i in s:
    if(c==i): count += 1
print(count)

