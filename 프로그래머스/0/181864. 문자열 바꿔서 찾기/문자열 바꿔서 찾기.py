def solution(myString, pat):
    answer = ''
    for s in myString:
        if s == 'A':
            answer += 'B'
        else:
            answer += 'A'
    return int(pat in answer)