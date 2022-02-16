import math
n = int(input())
# 质素定理：整数n的质因子较小的那个应该在[2, sqrt(n)+1)之间
for i in range(2, int(math.sqrt(n))+1):
    # 一旦返现了质因子，就将质因子打印出来，并且重置n
    while(n%i == 0):
        print(i, end=' ')
        n = n//i
# 打印出最后的那个质因子
if(n > 2):
    print(n)