s = input()
# 将字符串进行翻转
s = s[::-1]
res = ''
for i in s:
    if(i not in res):
        res = res + i
    else:
        continue
print(res)