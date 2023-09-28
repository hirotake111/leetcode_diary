/**
 * https://leetcode.com/problems/sort-array-by-parity/
 * 905. Sort Array By Parity
 */
impl Solution {
    pub fn sort_array_by_parity(nums: Vec<i32>) -> Vec<i32> {
        let mut answer: Vec<i32> = Vec::with_capacity(nums.len());
        // Push even numbers
        for n in nums.iter().filter(|&x| (x & 1) == 0) {
            answer.push(*n);
        }
        // Push odd numbers
        for n in nums.iter().filter(|&x| (x & 1) == 1) {
            answer.push(*n);
        }
        answer
    }
}
