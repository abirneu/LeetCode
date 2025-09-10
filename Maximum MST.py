def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        M = N * (N - 1) // 2
        weights = list(map(int, input().split()))
        
        weights.sort(reverse=True)
        
        ans = sum(weights[:N-1])
        print(ans)

