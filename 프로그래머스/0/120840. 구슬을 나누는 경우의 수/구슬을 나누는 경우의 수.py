from math import factorial
def solution(balls, share):
    n = factorial(balls)
    m = factorial(share)
    b = factorial(balls - share) * m
    return n/b