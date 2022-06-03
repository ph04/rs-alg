def sort_by_counting_sort_special(array):
    max_value = max(array)
    len_array = len(array)

    C = [0] * (max_value + 1)

    for i in range(len_array):
        C[array[i]] += 1

    i = 0
    j = 0

    while i < len_array:
        for _ in range(C[j]):
            array[i] = j

            i += 1

        j += 1

def sort_by_counting_sort_general(array):
    max_value = max(array)
    len_array = len(array)

    C = [0] * (max_value + 1)
    B = [0] * len_array

    for i in range(len_array):
        C[array[i]] += 1

    for i in range(max_value):
        C[i + 1] += C[i]

    for i in range(len_array - 1, -1, -1):
        curr_element = array[i]

        index = C[curr_element] - 1

        B[index] += curr_element

        C[curr_element] -= 1

    return B