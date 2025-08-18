def sort_descending(lst):
    """
    Takes a list of integers and returns the list sorted in descending order.

    Parameters:
    lst (list of int): The list of integers to sort.

    Returns:
    list of int: The sorted list in descending order.
    """
    return sorted(lst, reverse=True)
print(sort_descending([1, 2, 3, 4, 5]))
