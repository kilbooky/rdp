#Gprime5
def baum_sweet(n):
    count = 0
    while n:
        if n & 1:
            if count & 1:
                 return "0"
        else:
            count += 1
        n >>= 1
    return "1"

def bs_sequence(n):
    print(", ".join(map(baum_sweet, range(n+1))))

bs_sequence(20)