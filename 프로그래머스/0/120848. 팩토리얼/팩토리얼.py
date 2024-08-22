from math import factorial
def solution(n):
    f = 10
    while n < factorial(f):
        f -= 1
    return f