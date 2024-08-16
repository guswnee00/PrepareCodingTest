def solution(intStrs, k, s, l):
    answer = []
    for iStr in intStrs:
        if int(iStr[s:s+l]) > k:
            answer.append(int(iStr[s:s+l]))
    return answer