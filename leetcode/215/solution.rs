use std::cmp::Reverse;
/**
 * https://leetcode.com/problems/kth-largest-element-in-an-array/
 * 215. Kth Largest Element in an Array
 */
use std::collections::BinaryHeap;

impl Solution {
    pub fn find_kth_largest(mut nums: Vec<i32>, k: i32) -> i32 {
        let k = nums.len() - k as usize;
        *nums.select_nth_unstable(k).1
    }
}

// Binary heap solution
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut queue = BinaryHeap::with_capacity(k + 1);
        for n in nums {
            queue.push(Reverse(n));
            if k < queue.len() {
                queue.pop();
            }
        }
        queue.pop().unwrap().0
    }
}
