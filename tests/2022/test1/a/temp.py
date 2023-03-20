from math import isqrt

def is_prime(n):
    if n == 2 or n == 3 or n <= 1:
        return False
    if n%2 == 0 or n%3 == 0:
        return False
    
    for i in range(5, isqrt(n)+1, 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    print(is_prime(n))