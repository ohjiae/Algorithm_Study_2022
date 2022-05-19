import sys
input = sys.stdin.readline
for i in range(int(input())):
    N = int(input())
    p_li = {}
    for _ in range(N-1):
        mom, kid = map(int,input().split())
        p_li[kid] = [mom, False]
    a,b = map(int,input().split())
    result = 0
    while result == 0:
        try :
            if not p_li[a][1]:
                v = p_li[a][0]
                p_li[a] = [v, True]
                a = v
            else:
                result = a
                break
        except: pass
        try :
            if not p_li[b][1]:
                v = p_li[b][0]
                p_li[b] = [v, True]
                b = v
            else:
                result = b
                break
        except: pass
    print(result)