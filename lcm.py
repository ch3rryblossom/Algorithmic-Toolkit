# Uses python3
def gcd_fast(a, b):
    if b==0:
        return a
    A = a%b
    return gcd_fast(b, A)

def lcm_fast(a, b):
    return int((a/gcd_fast(a, b))*b)

if __name__ == '__main__':
    a, b = input().split()
    print(lcm_fast(int(a), int(b)))
