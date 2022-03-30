# 转换字符串
# 如果是字符串，就用字符后面的那个字符
# 如果是数字，就用比它大一的那个数字

# 便利字符串
str = input()
for i in str:
    # 如果i是数字，那么就将它加一打印出来
    if i.isdigit():
        # print(chr((ord(i)+1)%10), end='')
        # 将字符转换成数字，打印
        print(chr(ord(i) + 1), end='')
    
    else:
        print(chr(ord(i) + 1), end='')
        # print(i, end='')