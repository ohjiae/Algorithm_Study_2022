def solution(phone_book):
    answer = True
    hash={}
    for num in phone_book:
        hash[num]=1
    
    for num in phone_book:
        temp=''
        for i in num:
            temp+=i
            if temp in hash and temp!=num:
                answer=False
    
    return answer