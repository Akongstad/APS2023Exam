import random

# write stuff here that generates valid input for your problem
import random

if __name__ == '__main__':
    n = random.randint(1, 1)
    print(n)
    for _ in range(n):
        m = random.randint(1000, 1000)
        p = random.randint(2000, 2000)
        print(m, p)
        for _ in range(m):
            bi = random.randint(1, 1)
            e1 = random.randint(100, 100)
            print(bi, e1)
