day = 99
month = 99
year = 9999

def num_sum(num):
    if num > 27:
        return num_sum(sum(map(int, list(str(num)))))
    return num


print(num_sum((day + month + year)))


def num_sum1(num):
    number = int(num)
    if 100 > number > 27:
        number = number % 10 + number // 10
    elif 1000 > number >= 100:
        number = number % 10 + (number % 100) // 10 + number // 100
    elif number >= 1000:
        number = number % 10 + (number % 100) // 10 + (number % 1000) // 100 + number // 1000
        if number > 27:
            return num_sum(number)
    return number


print(num_sum((day + month + year)))
