def is_armstrong(number):
    str_num = str(number)
    power = len(str_num)
    sum = 0;
    for s in list(str_num):
        sum += int(s) ** power
    return sum == number
