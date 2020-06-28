# Uses python3

def get_fibonacci_huge_fast(n, m):
    fib = [0,1]
    pisano_period = 0
    while True:
        fib.append((fib[-1] + fib[-2]) % m)
        if fib[-2:] == [0,1]:
            pisano_period = len(fib) - 2
            break
    true_n = n%pisano_period
    return fib[true_n]

if __name__ == '__main__':
    n, m = input().split()
    print(get_fibonacci_huge_fast(int(n), int(m)))
