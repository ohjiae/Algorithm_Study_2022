c, n = map(int, input().split())
chars = [0]+sorted(input().split())
vowel = ['a', 'e', 'i', 'o', 'u']
result=[]

def is_vowel(char):
    if char in vowel:
        return True
    return False

def dfs(i, word, cnt_c, cnt_v):
    global result
    #Base Case
    if len(word)==c and cnt_c >= 2 and cnt_v >= 1:
        result+=[word]
        return

    for j in range(i+1, n+1):
        if is_vowel(chars[j]):
            dfs(j, word+chars[j], cnt_c, cnt_v+1)
        else:
            dfs(j, word+chars[j], cnt_c+1, cnt_v)
            
dfs(0, '', 0, 0)    
print(*result, sep='\n')