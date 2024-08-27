def solution(M, N):
    return 0 if N == 1 and M == 1 else (M - 1) + M * (N - 1)
    