def solution(participant, completion):
    cnt = {}
    for name in participant:
        if name in cnt:
            cnt[name] += 1
        else:
            cnt[name] = 1
            
    for name in completion:
        if name in cnt:
            cnt[name] -= 1

    for name in cnt:
        if cnt[name] > 0:
            return name