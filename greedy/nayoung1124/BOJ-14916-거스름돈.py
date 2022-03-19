if __name__ == '__main__':
    N = int(input())
    ans = 0
    flag = True
    while True:
        if N == 0:
            break
        elif N%5==0:
            ans += 1
            N-=5
        else:
            N-=2
            ans+=1
            if N < 0:
                print('-1')
                flag = False
                break

    if flag == True:
        print(ans)
