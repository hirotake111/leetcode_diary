/**
 * https://leetcode.com/problems/diagonal-traverse-ii/
 * 1424. Diagonal Traverse II
 */
impl Solution {
    pub fn find_diagonal_order(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let longest = nums.iter().map(|arr| arr.len()).max().unwrap();
        let mut tmp: Vec<Vec<i32>> = vec![vec![]; nums.len() + longest - 1];

        for (i, arr) in nums.iter().enumerate() {
            for (j, &n) in arr.into_iter().enumerate() {
                tmp[i + j].push(n);
            }
        }

        tmp.into_iter().map(reverse).flatten().collect()
    }
}

fn reverse(arr: Vec<i32>) -> Vec<i32> {
    arr.into_iter().rev().collect()
}
