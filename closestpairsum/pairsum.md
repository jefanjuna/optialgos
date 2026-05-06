Write a Python function closest_pair_sum(num_list, target) that takes a list of numbers and a target value. The function should:

    find two distinct numbers from the list whose sum is closest to the target
    return a tuple of those two numbers in ascending order (smaller, larger)
    Tie-breaker: If two different pairs are equally close to the target, return the pair with the smaller sum.
    if the list has fewer than 2 elements, return None.

Constraints:

    Use the .sort() method or sorted() function to create a sorted version of the list first.
    Use the two-pointer technique to find the pair efficiently. Google to find out more about this wonderful technique.
    Do not use nested loops. You should only use a single while loop for this operation!

If two different pairs have the same sum and are equally close to the target, return the pair with the smallest first element.

Examples:

    closest_pair_sum([10, 2, 5, 8], 11) returns (2, 8) (Sum 10 is closer to 11 than 5+8=13 or 2+5=7)
    closest_pair_sum([1, 10, 5, 2], 9) returns (1, 5) (Sum 6 and Sum 12 are equally close to 9; we return the smaller sum)
