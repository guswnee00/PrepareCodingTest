def solution(numbers):
    numlist = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, n in enumerate(numlist):
        numbers = numbers.replace(n, str(i))
    return int(numbers)