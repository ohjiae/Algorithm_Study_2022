from collections import OrderedDict
def solution(phone_book):
    answer = True
    phone_dict = {}
    for p_num in sorted(phone_book, key=len, reverse=True):
        phone_dict[p_num] = OrderedDict()
        for i in range(len(p_num)):
            p_num[p_num[i]] = i
        print(phone_dict)
    return answer
print(solution(["119", "97674223", "1195524421"]))