def binary_search_recursive(arr: list, target: any, left: int, right: int) -> int:
    """
    Recursive implementation of binary search on a sorted `arr` to search for `target`. Returns the index of the target if found, otherwise returns `-1`.
    """

    if left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        else:
            return binary_search_recursive(arr, target, left, mid - 1)

    return -1

def binary_search(arr: list, target: any, is_sorted: bool = True) -> int:
    """
    Performs a binary search on `arr` to search for `target`. If target is not found, `-1` is returned.

    `arr` should be sorted; set `is_sorted` to `False` if it is not sorted.
    """

    arr = arr.copy() if is_sorted else sorted(arr)

    return binary_search_recursive(arr, target, 0, len(arr) - 1)

# Example usage; this will only execute if you run `main.py`
if __name__ == "__main__":
    import random

    n = 10 # Number of random numbers (exclusive)
    numbers = [int(random.random() * 100) for x in range(n)]
    target = random.choice(numbers)
    print(
        binary_search(
            numbers,
            target,
            is_sorted=False
        )
    )
