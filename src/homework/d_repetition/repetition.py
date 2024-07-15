

def get_factorial(num):
    if num < 0:
        return "Invalid"
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

def sum_odd_numbers(num):
    if num < 0:
        return "Invalid."
    sum_odds = 0
    current = 1
    while current <= num:
        if current % 2 != 0:
            sum_odds += current
        current += 1
    return sum_odds
