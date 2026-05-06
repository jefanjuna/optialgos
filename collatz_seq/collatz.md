The Collatz sequence, also known as the Hailstone sequence, is a famous mathematical problem that has fascinated researchers for decades. It was introduced by the German mathematician Lothar Collatz in 1937, and despite its very simple definition, it leads to surprisingly complex behavior. The sequence has become well known because it is easy to state but extremely difficult to fully understand, and it remains one of the most intriguing unsolved problems in mathematics.

 

Write a Python function hailstone_length(num) that:

    takes an integer num

    repeatedly applies the following rules until the value becomes 1:

        if the number is even, divide it by 2

        if the number is odd, multiply it by 3 and add 1

    returns the number of steps needed to reach 1

    returns -1 if num is not positive.

[Think: Do you know the number of times the loop needs to run? So should you use a for loop or a while loop to implement this?]

Examples:

    hailstone_length(1) should return 0

    hailstone_length(6) should return 8 (6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1)

    hailstone_length(19) should return 20

    hailstone_length(54) should return 112
