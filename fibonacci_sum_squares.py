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
#From modular arithmetic, (A * B) mod C = (A mod C * B mod C) mod C
#From week2 pdf, S(n^2) = F(n)*F(n+1)
def fib_squares_sum(n):
    return ((get_fibonacci_huge_fast(n, 10))*(get_fibonacci_huge_fast(n+1, 10))) % 10
if __name__ == '__main__':
    n = input()
    print(fib_squares_sum(int(n)))
