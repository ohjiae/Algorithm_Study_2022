## 미완성
if __name__ == '__main__':
    while True:
        cnt = 1
        strings = list(map(str, input().rstrip()))
        if '-' in strings:
            break
        ans = 0
        stack = list()
        for target in strings:
            if target == '{':
                stack.append(target)
            else:
                if len(stack) != 0:
                    stack.pop()
                else:
                    ans += 1
                    stack.append('{')

        if len(stack) == 0:
            print(f'{cnt}. {int(ans)}')
        else: print(f'{cnt}. {int(len(stack)/2+ans)}')
        cnt+=1
    print()


