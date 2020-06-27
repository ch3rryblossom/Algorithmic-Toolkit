# Uses python3
def gcd_fast(a, b):
    if b==0:
        return a
    A = a%b
    return gcd_fast(b, A)
if __name__ == "__main__":
    a, b = input().split()
    print(gcd_fast(int(a), int(b)))
