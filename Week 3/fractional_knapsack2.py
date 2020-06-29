# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    vwarray = []
    class knapsack:
        def __init__(self, weights, values):
            self.weight = weights
            self.value = values
            self.vwrate = self.value/self.weight
    
    for i in range(len(weights)):
        vwarray.append(knapsack(weights[i], values[i]))
    
    sorted(vwarray, key=lambda knapsack: knapsack.vwrate, reverse=True)

    for i in range(len(vwarray)):
        if capacity == 0:
            return value
        a = min((vwarray[i].weight),capacity)
        value += a*(vwarray[i].vwrate)
        capacity -= a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
