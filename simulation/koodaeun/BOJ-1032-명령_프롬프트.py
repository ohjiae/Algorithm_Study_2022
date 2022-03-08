N = int(input())
input_arr = list()

for i in range (N):
    input_arr.append(list(input()))
output = input_arr[0]
len_output = len(output)

for i in range (N):
    for j in range(len_output):
        if output[j] != input_arr[i][j]:
            output[j] = '?'
str_output="".join(output)
print(str_output)