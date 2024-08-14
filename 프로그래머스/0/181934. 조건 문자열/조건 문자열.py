def solution(ineq, eq, n, m):
    if eq == "!":
        if ineq == ">":
            return int(n > m)
        else:
            return int(m > n)
    else:
        if ineq == ">":
            return int(n >= m)
        else:
            return int(m >= n)