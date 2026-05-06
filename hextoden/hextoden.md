Write a Python function hex_to_denary(hex_str) that:

    takes a string hex_str

    returns the denary (base-10) value of the hexadecimal number

    uses the string "0123456789abcdef"

    uses index() to find the value of each hex digit

Rules

    hex_str may start with 0x or 0X; if so, ignore that prefix

    Hex digits may be uppercase or lowercase

    Do not use the built in function int(hex_str, 16) for this exercise!

Examples

    hex_to_denary("0x1a") should return 26

    hex_to_denary("FF") should return 255

    hex_to_denary("10") should return 16

    hex_to_denary("0X0") should return 0
