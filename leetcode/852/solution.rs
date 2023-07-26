/**
 * https://leetcode.com/problems/peak-index-in-a-mountain-array/
 * 852. Peak Index in a Mountain Array
 */

/**
 * Binary search approach
 */

impl Solution {
    pub fn peak_index_in_mountain_array(arr: Vec<i32>) -> i32 {
        let (mut l, mut r) = (0, arr.len() - 1);
        // Edge case
        if arr[l] > arr[l + 1] {
            return 0;
        }
        if arr[r - 1] < arr[r] {
            return r as i32;
        }

        loop {
            let m = (l + r) / 2;
            if arr[m - 1] < arr[m] && arr[m] > arr[m + 1] {
                return m as i32;
            }
            if arr[m - 1] < arr[m] {
                l = m;
            } else {
                r = m;
            }
        }

        unreachable!();
    }
}
