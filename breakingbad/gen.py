from random import randint
N = 100001
M = 0

print(N)
for i in range(N):
    print(f'{i}A')
print(M)
'''for j in range(M):
    a = randint(1,N-1)
    b = randint(1,M-1)
    while a==b:
        b=randint(1,M-1)
    print(f'{a}A {b}A')'''

'''for j in range(1, M-1):
    if j%3 > 0:
        print(f'{j}A {j+1}A')
    else:
        print(f'{j}A {j-1}A')

print(f'{1}A {2}A')
print(f'{1}A {2}A')'''


#3.in small random impossible
#4.in medium connected possible
#5.in large connect possible
#6.in small disconnected possible
#7.in large disconnected possible #worst case? Or at least close to it?
#8.in large completely disconnected