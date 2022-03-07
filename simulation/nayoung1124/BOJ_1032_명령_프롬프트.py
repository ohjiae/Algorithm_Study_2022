if __name__ == '__main__':
    N = int(input())
    text = []
    ans = ''
    for _ in range(N):
        text.append(list(input()))
    for j in range(len(text[0])):
        target=set()
        for i in range(len(text)):
            target.add(text[i][j])
        if len(target) == 1:
            ans += list(target)[0]
        else: ans += '?'

    print(ans)
