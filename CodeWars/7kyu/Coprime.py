from math import gcd

def are_coprime(n,m):
    if gcd(n, m) == 1:
        print(f"{n} and {m} are coprime")
    else:
        print(f"{n} and {m} are not coprime")

print(are_coprime(20,27))