
n = int(input())

a = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    a[i][0] = 1

for i in range(1 ,n):
    for j in range(1 , n):
        a[i][j] = a[i-1][j] + a[i-1][j-1]

print(a)
