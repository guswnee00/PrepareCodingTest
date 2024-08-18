def solution(arr, query):
    for x in range(len(query)):
        if x == 0 or x % 2 == 0:
            del arr[query[x]+1:]
        else:
            del arr[:query[x]]
    return arr
        