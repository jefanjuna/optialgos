Hashing is the process of turning data, like a string, into a fixed-size number called a hash. A hash is useful because it gives a quick way to compare, store, or identify data.

A simple hashing idea is:

    look at each character in a string

    convert it to a number using its ASCII value

    give each character a weight based on its position

    add everything together

    use modulo to keep the result within a smaller range.

 

Your task is to write a Python function simple_hash(text, mod) that returns a weighted sum hash value.

    The first character has weight 1

    The second character has weight 2

    The third character has weight 3, and so on

    For each character, multiply its ASCII value by its weight

    Add all those values together

    Return the total modulo mod

    If text is empty, return 0

Example

For text = "abc" and mod = 13:

    'a' has ASCII value 97, so 1 × 97 = 97

    'b' has ASCII value 98, so 2 × 98 = 196

    'c' has ASCII value 99, so 3 × 99 = 297

Add them together and taking modulo 13, the function should return 5:

    (97 + 196 + 297) % 13 = 590 % 13 = 5