def solution(myString, pat):
    e = myString.rfind(pat)
    return myString[:e + len(pat)]