while True:
    try:
        n = int(input())
        lst = []
        for i in range(n):
            lst.append(int(input()))
        # 使用集合这个数据结构是为了去掉里面的重复数据
        s = set(lst)
        # 使用list这个数据结构是为了用它的排序方法
        lst = list(s)
        lst.sort()
        for i in lst:
            print(i)
    except:
        break