n = int(input())
k = int(input())
cards = [input().strip() for i in range(n)]

def per(cards, k):
    if k == 0:
        return ['']
    
    result = []
    for i in range(len(cards)):
        remaining = cards[:i] + cards[i+1:]
        for p in per(remaining, k-1):
            result.append(cards[i] + p)
    return result

print(len(set(per(cards, k))))