def binary_search_iterative(array, target):
    start = 0
    end = len(array) - 1

    half = (start + end) // 2

    while array[half] != target:
        if array[half] < target:
            start = half + 1
        else:
            end = half - 1

        if start > end:
            return -1

        half = (start + end) // 2

    return half

def binary_search(array, target, start, end):
    if start > end:
        return -1

    half = (start + end) // 2

    if array[half] == target:
        return half

    if array[half] < target:
        return binary_search(array, target, half + 1, end)
    else:
        return binary_search(array, target, start, half - 1)

def binary_search_recursive(array, target):
    return binary_search(array, target, 0, len(array) - 1)