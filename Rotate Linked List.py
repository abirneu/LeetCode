n, k = map(int, input().split())
arr = list(map(int, input().split()))

drop = []
for i in range(n-1, -1, -1):
    drop.append(arr[i])

drop.pop(k-1)

drop = drop[::-1]

print(*drop)
