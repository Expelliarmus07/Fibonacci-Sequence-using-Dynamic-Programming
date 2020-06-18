
def topDown_fibonacci(n):
    memo = [None] * (n + 1)
    return fibonacci(n, memo)

def fibonacci(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    return result

n = int(input('Enter n: '))

ans = topDown_fibonacci(n)
print('The nth Fibonacci number:', ans)