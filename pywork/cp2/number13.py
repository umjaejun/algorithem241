def mystery1(n) :
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

result = mystery1(5)
print(result)