f = float(input())
y_pos = lambda x:int(x+0.5)
y_nag = lambda x:int(x-0.5)
if(f>0):
    print(y_pos(f))
else:
    print(y_nag(f))