def print_str(string, chk):
    print(''.join([string[i] if chk[i] else '?' for i in range(len(string))]))

def chk_validation(std, chk, n):
    for i in range(n):
        string = input()
        for j in range(len(string)):
            if string[j] != std[j]:
                chk[j] = False
    return chk

def main():
    n = int(input())
    std = input()
    chk = [True] * (len(std))
    chk = chk_validation(std, chk, n-1)
    print_str(std, chk)

if __name__ == "__main__":
    main()