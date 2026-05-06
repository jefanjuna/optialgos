Write a Python function find_consec(num) that:

    takes a positive integer num

    scans through its digits to find the first occurrence of three digits in a row where each digit differs by exactly 1 from the previous, and they are either all increasing or all decreasing

    returns a string "i j k" where i, j, k are the 1-based positions of those three digits (look at examples below, and note how they are separated by a single space)

    if no such occurrence exists, return ""

Examples

    find_consec(8701298) should return "3 4 5", because the third, fourth and fifth digits of the number 8701298 are consecutive values (increasing).

    find_consec(9593678) should return "5 6 7", because the fifth, sixth and seventh digits are consecutive values (increasing).

    find_consec(9876543) should return "1 2 3", because the first, second and third digits of 9876543 are consecutive values (decreasing).

    find_consec(9999999) should return ""

    find_consec(1359) should return ""
