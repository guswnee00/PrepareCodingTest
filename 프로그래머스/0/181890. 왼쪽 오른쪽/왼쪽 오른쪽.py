def solution(str_list):
    for x in range(len(str_list)):
        if str_list[x]=='l': 
            return str_list[:x]
        elif str_list[x]=='r': 
            return str_list[x+1:]
    return []