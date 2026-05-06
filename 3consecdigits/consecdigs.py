def find_consec(num):
    for i in range(len(str(num)) - 2):
        a, b, c = int(str(num)[i]), int(str(num)[i+1]), int(str(num)[i+2])
        if (b - a == 1 and c - b == 1) or (a - b == 1 and b - c == 1):
            return f"{i+1} {i+2} {i+3}"
    return ""