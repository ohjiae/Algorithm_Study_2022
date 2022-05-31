def solution(phone_book):
    hash = {}

    for num in phone_book:
        hash[num]=0
  
    for num in phone_book:
        tmp=''
        for x in num:
            tmp+=x
            if tmp in hash and tmp!=num:
                return False

    return True