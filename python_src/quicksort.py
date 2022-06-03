def partition(array, start, end):
    pivot = array[start]

    i = start - 1
    j = end + 1

    while True:
        i += 1
        while array[i] < pivot:
            i += 1

        j -= 1
        while array[j] > pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            return j

def quicksort(array, start, end):
    if start < end:
        half = partition(array, start, end)

        quicksort(array, start, half)
        quicksort(array, half + 1, end)

def sort_by_quicksort(array):
    quicksort(array, 0, len(array) - 1)