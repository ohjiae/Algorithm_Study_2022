from collections import deque

def calculate(string):
    res = 0
    Bracket = deque()
    while string:
        tmp = string.popleft()
        # string input을 하나하나 검사하면서
        # { 는 push,
        # } 는 { 와 쌍을 만들 수 없는 경우에만 { 로 바꾸어서 push
        if tmp == '{':
            Bracket.append(tmp)
        elif tmp == '}':
            if Bracket:
                Bracket.pop()
            else:
                Bracket.append('{')
                res += 1
    # 남은 { 는 절반만 바꿔주면 되므로  길이의 절반을 더해줌
    return res + int(len(Bracket)/2)

def main():
    step = 0
    while True:
        step += 1
        string = deque(input().rstrip())
        if string[0] == '-':
            break
        print(str(step) + ". ",end='')
        print(calculate(string))

if __name__ == "__main__":
    main()