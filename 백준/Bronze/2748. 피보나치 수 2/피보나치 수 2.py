n = int(input())
fibonacciNum = [0] * 91
fibonacciNum[1] = 1

for i in range(2, n+1):
    fibonacciNum[i] = fibonacciNum[i-1] + fibonacciNum[i-2]

print(fibonacciNum[n])