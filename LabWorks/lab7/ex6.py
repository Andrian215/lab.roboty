
import random
import math
N = int(input('N='))
matrix = [[random.randint(-10,10)for x in range(N)]for y in range(N)]
for x in range(len(matrix)):
    if True:
        print(matrix[x])
print('--------------------------------------')
forsum= []
for x in range(N-1):
    for y in range(N-1):
        y+=1
        if y>x:
            forsum.append(math.fabs(matrix[x][y]))
print(sum(forsum))
