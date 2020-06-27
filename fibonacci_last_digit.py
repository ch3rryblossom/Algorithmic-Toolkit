# Uses python3
def get_fibonacci_last_digit_fast(n):
    A = [0, 1]
    for i in range(2,n+1):
        A.append((A[i-1] + A[i-2])%10)
    return A[n]
if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_fast(n))