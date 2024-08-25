def solution(quiz):
    answer = []
    for i in quiz:
        m = i.split(' = ')
        if eval(m[0]) == int(m[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer