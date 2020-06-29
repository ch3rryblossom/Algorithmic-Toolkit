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
def fib_partial_sum(m, n):
    return (get_fibonacci_huge_fast(n+2, 10) + 10 - get_fibonacci_huge_fast(m+1, 10)) % 10
if __name__ == '__main__':
    n, m = input().split()
    print(fib_partial_sum(int(n),int(m)))