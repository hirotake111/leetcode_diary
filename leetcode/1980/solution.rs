/**
 * https://leetcode.com/problems/find-unique-binary-string/
 * 1980. Find Unique Binary String
 */
impl Solution {
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        use std::collections::HashSet;
        let mut set: HashSet<usize> = nums
            .iter()
            .map(|s| usize::from_str_radix(s, 2).unwrap())
            .collect();
        let mut n = 0;
        while set.contains(&n) {
            n += 1;
        }
        let bin_str = format!("{n:b}");
        let zeros = "0".repeat(nums.len() - bin_str.len());

        format!("{zeros}{bin_str}")
    }
}
