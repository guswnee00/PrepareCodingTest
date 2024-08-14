def solution(num_list):
    s = sum(num_list) * sum(num_list)
    m = 1
    for i in num_list:
        m *= i
    return int(s > m)