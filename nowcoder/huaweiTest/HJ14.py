while True:
    try:
        n = int(input())
        lst = []
        for i in range(n):
            lst.append(input())
        print('\n'.join(sorted(lst)))
    except:
        break