def baum_sweet(n):
    z = 0
    while n:
        if (n & 1) == 0:
            z += 1
        else:
            if z % 2 != 0:
                return 0
            z = 0
        n >>= 1
    return 1

results = []
for i in range(21):
    results.append(baum_sweet(i))
print(results)