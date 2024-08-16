def solution(num_list):
    c = 0
    for i in num_list:
        while i > 1:
            if i % 2:
                i = (i - 1) / 2
                c += 1
            else:
                i /= 2
                c += 1
    return c
        