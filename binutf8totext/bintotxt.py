with open("text2.txt", 'r') as file:
    binary_string = file.read()
bytes_lst = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

def bint(binary):
    integer = 0
    binary = binary[::-1]
    for i in range(len(binary)):
        if binary[i] == "1":
            integer += 2**i
    return integer

word = ""
for i in range(len(bytes_lst)):
    prebyte = 0
    for bit in bytes_lst[i][:6]:
        if bit == "1":
            prebyte += 1
        else:
            break
    if prebyte > 1:
        char_bytes = bytes_lst[i:i+prebyte]
        char_bytes[0] = char_bytes[0][prebyte+1:]
        for j in range(1, len(char_bytes)):
            char_bytes[j] = char_bytes[j][2:]
        word += chr(bint("".join(char_bytes)))
    elif prebyte == 0:
        word += chr(bint(bytes_lst[i]))
print(word)