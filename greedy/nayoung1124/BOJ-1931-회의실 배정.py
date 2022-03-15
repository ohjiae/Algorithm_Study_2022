if __name__ == '__main__':
    N = int(input())
    meetings=[]
    ans = 1
    for _ in range (N):
        meeting = list(map(int,input().split()))
        meetings.append(meeting)
    meetings.sort(key = lambda x:(x[1],x[0])) # 끝나는 시간 기준으로 정렬
    target = meetings[0]
    for i in range(1,N):  # 첫번째는 넣고 시작하려고
        if target[1] <= meetings[i][0]:
            ans +=1
            target = meetings[i]
        else:continue
    print(ans)
