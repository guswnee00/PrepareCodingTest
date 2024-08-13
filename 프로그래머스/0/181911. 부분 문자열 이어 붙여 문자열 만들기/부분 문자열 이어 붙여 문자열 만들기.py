def solution(my_strings, parts):
    answer = ''
    for i, n in enumerate(parts):
        answer += my_strings[i][n[0]:n[1]+1]
    return answer