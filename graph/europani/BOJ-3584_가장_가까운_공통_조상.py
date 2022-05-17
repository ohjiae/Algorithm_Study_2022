t = int(input())

for _ in range(t):
    n = int(input())
    parent = [-1] * (n+1)
    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b]=a

    ta, tb = map(int, input().split())

    parent_ta = [ta]
    while ta != -1:
        parent_ta.append(parent[ta])
        ta=parent[ta]

    while tb != -1:
        if tb in parent_ta:
            print(tb)
            break
        tb=parent[tb]