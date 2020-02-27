import json
f = open('SEATSMATRIX.txt','w')
def getX(start,end,lst):
    if start != end:
        start -= 60
        lst.append(float(start))
        return getX(start,end,lst)
    return lst
M = [[] for i in range(6)]
X = getX(448,-512,[])
X = X[::-1]
Y = [float(180.0),120.0,60.0,-60.0,-120.0,-180.0]
numbers = []
for idx,x in enumerate(X):
    for idy,y in enumerate(Y):
        M[idy].append((x,y))
for i in range(1,4):
   numbers.append([x for x in range(i,97,6)])
for i in range(6,3,-1):
    numbers.append(([x for x in range(i, 97, 6)]))
lst = [[] for i in range(6)]
k = 0
for number,seat in zip(numbers,M):
    for x,cor in zip(number,seat):
        lst[k].append((x,cor))
    k+=1
f.write(json.dumps(lst))
f.close()
