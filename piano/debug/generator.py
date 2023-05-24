import random

# write stuff here that generates valid input for your problem
import random

if __name__ == '__main__':
    n = random.randint(1, 100)
    print(n)
    for _ in range(n):
        m = random.randint(1, 1000)
        p = random.randint(1, 2000)
        print(m, p)
        for _ in range(m):
            bi = random.randint(1, 100)
            e1 = random.randint(bi, 100)
            print(bi, e1)
