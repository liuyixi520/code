# 先将输入根据分号隔离开来
lst = input().split(';')
point = [0, 0]

for i in lst:
    # 如果输入的移动坐标非法就直接跳过
    if len(i)<2 or len(i)>3:
        continue
    move = i[0]
    try:
        step = int(i[1:3])
    except:
        continue
    if move in ['A', 'S', 'D', 'W'] and 1<= step <=99:
        if(move=='A'):
            point[0] = point[0] - step
        elif(move=='D'):
            point[0] = point[0] + step
        elif(move=='S'):
            point[1] = point[1] - step
        elif(move=='W'):
            point[1] = point[1] + step

print(str(point[0]) + ',' + str(point[1]))

