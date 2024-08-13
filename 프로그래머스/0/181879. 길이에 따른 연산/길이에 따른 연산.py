def solution(num_list):
    answer = 1
    if len(num_list) < 11:
        for n in num_list:
            answer *= n
    else:
        answer = sum(num_list)
    return answer