def solution(hp):
    h = hp // 5
    m = (hp - h * 5) // 3
    l = hp - h * 5- m * 3
    return l+m+h