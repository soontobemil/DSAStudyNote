def fibonacciIterative(n):
    arr = [0,1]
    for i in range(2, n + 1):
        arr.append(arr[n-1] + arr[n-2])
    return arr[n]


def fibonacciRecurive(n): ## Big 2^O (it's not an ideal soltuion)
    if n < 2:
        return n
    return fibonacciRecurive(n-1) + fibonacciRecurive(n-2)

print(fibonacciRecurive(5))
