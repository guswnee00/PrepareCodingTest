def solution(message):
    answer = 0
    message = message.replace(' ', '-')
    for i in message:
        answer += 1
    return answer * 2