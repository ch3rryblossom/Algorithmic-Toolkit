# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    vwarray = []
    index = list(range(len(values)))
    ratio = [v/w for v, w in zip(values, weights)]
    index.sort(key=lambda i: ratio[i], reverse=True)

    for i in index:
        if weights[i] <= capacity:
            value += values[i]
            capacity -= weights[i]
        else:
            value += values[i]*capacity/weights[i]
            break
 
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
