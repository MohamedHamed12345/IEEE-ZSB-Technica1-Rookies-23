def g(number, base: int = 10):
    total = 0
    while number > 0:
        total += pow(number % base, 2)
        number = number // base
    return total

def h(number: int):
    seen_numbers = set()
    while number > 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = g(number)
    return number == 1
print(h(int(input())))