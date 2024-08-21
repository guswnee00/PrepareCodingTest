def solution(my_string):
    mo = ("a,e,i,o,u")
    for m in mo:
        my_string = my_string.replace(m, "")
    return my_string