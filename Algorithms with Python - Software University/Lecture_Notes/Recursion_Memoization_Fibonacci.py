# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ..
# 0, 1, 2, 3, 4, 5, 6, 7, 8 ...



# Input 20 = Output 6765

def calc_fib(n, memo):
    if n in memo:

        return memo[n]
    if n <= 2:

        return 1

    result = calc_fib(n - 1, memo) + calc_fib(n - 2, memo)
    memo[n] = result
    return result

n = int(input())

print(calc_fib(n, {}))



