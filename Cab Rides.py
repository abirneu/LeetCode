t = int(input())
for _ in range(t):
    n = int(input())
    
    full_cabs = n // 4
    rem = n % 4
    
    cost = full_cabs * 400
    if rem > 0:
        cost += max(200, 100 * rem)
    
    print(cost)
