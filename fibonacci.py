# Uses python3
def calc_fib_fast(n):
    A = [0, 1]
    for i in range(2,n+1):
        A.append(A[i-1] + A[i-2])
    return A[n]
n = int(input())
print(calc_fib_fast(n))
