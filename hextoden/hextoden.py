def hex_to_denary(hex_str):
    digits = "0123456789abcdef"
    if hex_str.startswith("0x") or hex_str.startswith("0X"):
        hex_str = hex_str[2:]
    result = 0
    for i in hex_str.lower():
        result = result * 16 + digits.index(i)
    return result