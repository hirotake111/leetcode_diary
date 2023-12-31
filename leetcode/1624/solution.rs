/**
 * https://leetcode.com/problems/largest-substring-between-two-equal-characters/
 * 1624. Largest Substring Between Two Equal Characters
 */

impl Solution {
    pub fn max_length_between_equal_characters(s: String) -> i32 {
        let mut arr: [i32; 26] = [-1; 26];
        let mut largest = -1;
        for (i, b) in s.bytes().enumerate() {
            let b = (b - 97) as usize;
            let i = i as i32;
            if arr[b] >= 0 {
                largest = largest.max(i - arr[b] - 1);
            } else {
                arr[b] = i;
            }
        }
        largest
    }
}
