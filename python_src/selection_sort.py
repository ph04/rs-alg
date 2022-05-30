def get_min_index(array, start):
    min_element = array[start]
    min_index = start

    for i in range(start + 1, len(array)):
        if array[i] < min_element:
            min_element = array[i]
            min_index = i

    return min_index

def sort_by_selection_sort(array):
    for i in range(len(array) - 1):
        min_index = get_min_index(array, i)

        array[i], array[min_index] = array[min_index], array[i]