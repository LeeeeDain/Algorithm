import copy

def solution(phone_book):
    phone_book.sort()

    for i in phone_book:
        tmp = copy.deepcopy(phone_book)
        tmp.remove(i)
        for j in tmp:
            if i in j[:len(i)] :
                return False
    return True