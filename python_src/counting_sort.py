def sort_by_counting_sort(array):
    max_value = max(array)
    len_array = len(array)

    C = [0] * (max_value + 1)
    B = [0] * len_array

    for i in range(len_array):
        C[array[i]] += 1

    for i in range(0, max_value):
        C[i + 1] += C[i]

    for i in range(len_array - 1, -1, -1):
        curr_element = array[i]

        index = C[curr_element] - 1

        B[index] += curr_element

        C[curr_element] -= 1

    return B