def denary_to_hex(n):
    digits = "0123456789abcdef"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        remainder = n % 16
        result = digits[remainder] + result
        n = n // 16
    return result