def find_parent(x):     # x에 대한 root node 찾는 함수
    if x==friends[x]:
        return x
    else:               # 각 하위 노드의 value를 모두 root node로 바꿔줌. 값이 커지면 순회하는 시간이 줄어듦.
        root_x=find_parent(friends[x])   
        friends[x]=root_x
        return friends[x]


def union(x,y):
    root_x=find_parent(x)  # x, y의 root node를 찾음
    root_y=find_parent(y)

    # x, y의 root node가 같지 않으면
    # y의 root node가 x의 root node의 자식이 되도록 함
    # 그리고 root_x의 친구 수에 root_y의 친구 수를 더함
    
    if root_x!=root_y:
        friends[root_y]=root_x
        number[root_x]+=number[root_y]

for i in range(int(input())):
    friends = {}
    number = {}
    for j in range(int(input())):
        x,y=input().split()
        if x not in friends:
            friends[x]=x
            number[x]=1
        if y not in friends:
            friends[y]=y
            number[y]=1
        union(x,y)
        # 위의 함수에서 x, y의 root node가 같지 않으면
        # x의 root node가 y의 root node가 되도록 했기 때문에
        # x의 root node의 값을 찾아서 갯수를 출력함
        print(number[find_parent(x)])
