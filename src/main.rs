#![allow(unused_imports)]

use alg::{
    heapsort::sort_by_heapsort,
    selection_sort::sort_by_selection_sort,
    insertion_sort::sort_by_insertion_sort,
    bubble_sort::sort_by_bubble_sort,
    mergesort::sort_by_mergesort,
};

fn main() {
    // let mut array = [3, 6, 0, 4, 24, 10, 2, 3, 4, 7, 3, 1, 0];
    // let mut array = [1, 4, 0, 3];
    // let mut array = [0, 2, 3, 4, 1, 5, 6];
    let mut array = [6, 1, 9, 0, 3, 8, 5, 4, 7];

    // sort_by_heapsort(&mut array);
    // sort_by_selection_sort(&mut array);
    sort_by_insertion_sort(&mut array); // doesn't work yet
    // sort_by_bubble_sort(&mut array);
    // array = sort_by_mergesort(array); // doesn't work yet

    println!("{:?}", array);
}