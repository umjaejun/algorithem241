def sub(n) :
    if n <= 1 : return n
    return sub(n-1) + sub(n-2)

result = sub(3)
print("결과: ", result)