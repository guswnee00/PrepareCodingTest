while True:
    l = list(map(int, input().split()))
    
    if l == [-1]:
        break
        
    l.remove(0)
    
    cnt = 0
    for num in l:
        if 2 * num in l:
            cnt += 1
    print(cnt)
