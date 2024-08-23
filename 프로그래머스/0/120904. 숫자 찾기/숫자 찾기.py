def solution(num, k):
    for s in str(num):
        if s == str(k):     
            return str(num).find(str(k)) + 1
    return -1