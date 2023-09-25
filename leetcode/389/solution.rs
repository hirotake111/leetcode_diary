/**
 * https://leetcode.com/problems/find-the-difference/?envType=daily-question&envId=2023-09-25
 * 389. Find the Difference
 */
impl Solution {
    pub fn find_the_difference(s: String, t: String) -> char {
        let mut arr = [0; 26];
        for c in s.chars() {
            arr[c as usize - 97] += 1;
        }
        for c in t.chars() {
            arr[c as usize - 97] -= 1;
        }
        for i in 0..26 {
            if arr[i] != 0 {
                return (i as u8 + 97) as char;
            }
        }
        unreachable!()
    }
}
