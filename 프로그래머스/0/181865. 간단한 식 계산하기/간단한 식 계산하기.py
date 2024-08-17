def solution(binomial):
    l = binomial.split(' ')
    if l[1] == '+':
        return int(l[0]) + int(l[2])
    elif l[1] == '-':
        return int(l[0]) - int(l[2])
    else:
        return int(l[0]) * int(l[2])