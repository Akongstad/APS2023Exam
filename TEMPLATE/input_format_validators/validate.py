import sys
import re

firstline = sys.stdin.readline()
assert re.match(r"(0|-?[1-9][0-9]*)\n", firstline), firstline

n = int(firstline)
assert 2 < n < 301

secondline = sys.stdin.readline()
assert re.match(r"(0 ?|-?[1-9][0-9]{0,4} )*(0 ?|-?[1-9][0-9]{0,4})\n", secondline), secondline

array = secondline.split()

for number in range(len(array)):
    assert -10001 < number < 10001

assert sys.stdin.readline() == ""

sys.exit(42)