Write a Python function find_peaks(data_list) that identifies "peaks" within a list of integers. A peak is defined as an element that is strictly greater than its immediate neighbours.

The Rules:

    Iterate by Index: You must use for i in range(len(data_list)) to access elements by their position.
    Boundaries:
        The first element (index 0) is a peak if it is strictly greater than the second element.
        The last element is a peak if it is strictly greater than the second-to-last element.
    Return: A list of the indices where peaks are found. If the list has fewer than 2 elements, return [].

Example:

    find_peaks([1, 5, 2, 3, 1]) returns [1, 3]
    find_peaks([10, 2, 3, 8]) returns [0, 3]
    find_peaks([5, 5, 5, 5, 5]) returns []