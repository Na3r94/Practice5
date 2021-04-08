fib = (0 , 1)

print("Donbale Fibo ta Onsore chandom chap shavad? " , end=' ')
n = int(input())

for i in range(n-1):
    y = list(fib)
    a = y[i] + y[i+1]
    y.append(a)
    fib = tuple(y)

print(fib)