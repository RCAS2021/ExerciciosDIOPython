T = int(input())

for i in range(T):
    n, k = map(int, input().split())

    if k>n:
        n1 = n
        n = k
        k = n1
    
    print(n//k + n % k)