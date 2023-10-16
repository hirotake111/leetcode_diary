/**
 * https://leetcode.com/problems/pascals-triangle-ii/
 * 119. Pascal's Triangle II
 */

impl Solution {
    pub fn get_row(i: i32) -> Vec<i32> {
        let i = i as usize;
        let mut arr = vec![0; i + 1];
        arr[0] = 1;

        for j in 1..=i {
            for k in (1..=j).rev() {
                arr[k] += arr[k - 1];
            }
        }

        arr
    }
}
