def solution(arr):
    answer = 0
    while(True):
        l = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                l.append(int(i/2))
            elif i < 50 and i % 2 == 1:
                l.append(i * 2 + 1)
            else:
                l.append(i)
        
        if arr == l:
            return answer
        else:
            answer += 1
            arr = l