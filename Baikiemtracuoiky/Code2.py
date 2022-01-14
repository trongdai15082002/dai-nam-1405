A = [1,1,2,3,5,8,13,21,34,55,88]
B = [1,3,5,4,7,88,66,59,40,54]
C=[]
for i in range(0,len(A)):
    for j in range(0,len(B)):
        if A[i]==B[j]:
            C.append(A[i])
print(C)
A = list (set(A)^set(C))
B = list (set(B)^set(C))
print(A)
print(B)