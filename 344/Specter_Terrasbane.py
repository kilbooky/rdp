#Specter_Terrasbane
from itertools import groupby, count, islice

def odd_run(n):
    return n and any(k == '0' and sum(1 for __ in g) & 1 for k, g in groupby(bin(n)[2:]))

def baum_sweet_sequence():
    for n in count():
        yield 0 if odd_run(n) else 1

def challenge(n):
    return ', '.join(str(b) for b in islice(baum_sweet_sequence(), n + 1))

# Testing

gold = '1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0'
assert  challenge(20) == gold