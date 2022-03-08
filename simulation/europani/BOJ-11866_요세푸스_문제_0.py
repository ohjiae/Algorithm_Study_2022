n, k = map(int, input().split())
people = [i for i in range(1, n+1)]
idx = 0
result = []

while people:
    idx=(idx+k-1)%len(people)
    num = people.pop(idx)
    result+=[num]

print(f"<{', '.join(map(str, result))}>") 