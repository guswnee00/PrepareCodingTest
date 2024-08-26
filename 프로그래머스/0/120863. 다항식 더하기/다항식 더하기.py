def solution(polynomial):
    p = polynomial.replace(' ', '').split('+')
    x, c = 0, 0
    
    for i in p:
        if 'x' in i:
            if len(i) == 1:
                x += 1
            else:
                x += int(i[:-1])
        else:
            c += int(i)   
    
    if c == 0:
        if x == 0:
            return ('0')
        elif x == 1:
            return ('x')
        elif x > 1:
            return (str(x) + 'x')
    elif c != 0:
        if x == 0:
            return str(c)
        elif x == 1:
            return ('x + ' + str(c))
        elif x > 1:
            return (str(x) + 'x + ' + str(c))