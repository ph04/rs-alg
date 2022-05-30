# from heapsort import sort_by_heapsort
from selection_sort import sort_by_selection_sort
# from insertion_sort import sort_by_insertion_sort
from bubble_sort import sort_by_bubble_sort
# from mergesort import sort_by_merge_sort

def main():
    # array = [3, 6, 0, 4, 24, 10, 2, 3, 4, 7, 3, 1, 0]
    array = [6, 1, 9, 0, 3, 8, 5, 4, 7]

    # sort_by_heapsort(array)
    sort_by_selection_sort(array)
    # sort_by_insertion_sort(array)
    sort_by_bubble_sort(array)
    # array = sort_by_mergesort(array)

    print(array)

if "__main__" == __name__:
    main()