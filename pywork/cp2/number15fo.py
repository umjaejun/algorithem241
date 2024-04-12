def algorithm(n) :
    k = 0
    while n > 1 :
        n = n / 2
        k = k + 1
    return k
result = algorithm(100)
print(result)