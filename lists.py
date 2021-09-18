list = [2,6,3,8,1,4,7]
a = len(list)

for i in range(0 ,a -1):
    for j in range(i+1,a):
        if(list[i]>list[j]):
            b = list[i]
            list[i] = list[j]
            list[j] = b
            print(list)