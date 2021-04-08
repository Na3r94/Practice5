n = int(input('Enter number of A arrays : '))

A = set()
B = set()
C = set()
for i in range(n):
    a = int(input())
    A.add(a)

m = int(input('Enter number of B arrays : '))

for i in range(m):
    a = int(input())
    B.add(a)

C.update(B,A)
D = A.intersection(B)

print("Eshterake 2 majomoe = " , D)
print("Ejtema 2 Majmoe = " , C)