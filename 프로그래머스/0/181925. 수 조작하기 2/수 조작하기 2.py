def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        num = numLog[i+1]  - numLog[i]
        if num == 1:
            answer += 'w'
        elif num == -1:
            answer += 's'
        elif num == 10:
            answer += 'd'
        else:
            answer += 'a'
    return answer