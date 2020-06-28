# Uses python3

#S(n) = F(n+2) - 1
def get_fibonacci_sum_last_digit_fast(n):
    fib = [0,1]
    n=n+2
    m = 10
    pisano_period = 0
    while True:
        fib.append((fib[-1] + fib[-2]) % m)
        if fib[-2:] == [0,1]:
            pisano_period = len(fib) - 2
            break
    true_n = n%pisano_period
    return (fib[true_n]-1)%10
if __name__ == '__main__':
    n = input()
    print(get_fibonacci_sum_last_digit_fast(int(n)))
