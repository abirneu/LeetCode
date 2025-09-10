t = int(input())
for _ in range(t):
    n = int(input())
    st = list(map(int, input().split()))
    chef = st[0]
    count = sum(1 for x in st if x >= chef)
    print(count)
