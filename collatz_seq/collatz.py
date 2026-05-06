def hailstone_length(num):
    steps = 0
    if int(num) <= 0:
        return -1
    int_n = int(num)
    while int_n != 1:
        if int_n % 2 == 0:
            int_n /= 2
            steps += 1
        else:
            int_n = 3 * int_n + 1
            steps += 1
    return steps