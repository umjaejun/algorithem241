def factorial_iter(n) :
    result = 1
    for k in range(1, n+1) :
        result = result * k
    return result

print(factorial_iter(10))