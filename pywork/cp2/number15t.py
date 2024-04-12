n = 10
sum = 0
for i in range(n):
    for j in range(i+1, n, 2):
        sum = sum + j
print(sum)