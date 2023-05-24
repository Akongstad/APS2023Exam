import sys
import re

firstline = sys.stdin.readline() #Money, time, amount of missions
assert re.match(r"([1-9][0-9]*) ([1-9][0-9]*) ([1-9][0-9]*)\n", firstline), firstline

M, T, N = firstline.split()
M = int(M)
T = int(T)
N = int(N)

assert 0 < M < 251
assert 0 < T < 126
assert 0 < N < 101

for _ in range(N):
    secondline = sys.stdin.readline() #Money cost, time spend, people rescued
    assert re.match(r"([1-9][0-9]*) ([1-9][0-9]*) ([1-9][0-9]*)\n", secondline), secondline
    
    m, t, r = secondline.split()
    m = int(m)
    t = int(t)
    r = int(r)

    assert 0 < m <= M
    assert 0 < t <= T
    assert 0 < r < 100

assert sys.stdin.readline() == ""

sys.exit(42)