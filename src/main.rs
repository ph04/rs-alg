#![allow(unused_imports)]

use alg::{
    heapsort::sort_by_heapsort,
    selection_sort::sort_by_selection_sort,
    insertion_sort::sort_by_insertion_sort
};

fn main() {
    let mut array = [3, 6, 0, 4, 24, 10, 7, 2, 3, 4, 7, 3, 1, 0];
    // let mut array = [1, 4, 0, 3];
    // let mut array = [0, 2, 3, 4, 1, 5, 6];

    // sort_by_heapsort(&mut array);
    // sort_by_selection_sort(&mut array);
    sort_by_insertion_sort(&mut array);

    println!("{:?}", array);
}