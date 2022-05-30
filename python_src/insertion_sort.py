def shift_array(array, start, end):
    for i in range(end, start, -1):
        array[i], array[i - 1] = array[i - 1], array[i]

def sort_by_insertion_sort(array):
    for i in range(1, len(array)):
        curr_element = array[i]

        new_index = i - 1

        while new_index != -1 and array[new_index] > curr_element:
            new_index -= 1

        new_index += 1

        shift_array(array, new_index, i)