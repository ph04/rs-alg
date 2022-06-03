def merge(array, start, half, end):
    i = start
    j = half + 1

    buffer = []

    while i <= half and j <= end:
        curr_element_i = array[i]
        curr_element_j = array[j]

        if curr_element_i <= curr_element_j:
            buffer.append(curr_element_i)
            i += 1
        else:
            buffer.append(curr_element_j)
            j += 1

    while i <= half:
        buffer.append(array[i])
        i += 1

    while j <= end:
        buffer.append(array[j])
        j += 1

    for index in range(len(buffer)):
        array[start + index] = buffer[index]

def mergesort(array, start, end):
    if start < end:
        half = (start + end) // 2

        mergesort(array, start, half)
        mergesort(array, half + 1, end)

        merge(array, start, half, end)

def sort_by_mergesort(array):
    mergesort(array, 0, len(array) - 1)