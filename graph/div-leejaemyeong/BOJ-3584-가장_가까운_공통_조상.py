for _ in range(int(input())):
    N=int(input())
    graph=[[]for _ in range(N+1)]

    for _ in range(N-1):
        a,b=map(int,input().split())
        graph[b].append(a)

    a_node,b_node=map(int,input().split())
    setB = {b_node}
    while graph[b_node]:
        if graph[b_node]:
            b_node=graph[b_node][0]
            setB.add(b_node)
    while True:
        if a_node in setB:
            print(a_node)
            break
        if graph[a_node]:
            a_node=graph[a_node][0]