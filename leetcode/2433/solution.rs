/**
 * https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
 * 2433. Find the Original Array of Prefix Xor
 */
impl Solution {
    pub fn find_array(pref: Vec<i32>) -> Vec<i32> {
        let mut arr = vec![pref[0]; pref.len()];
        for i in 1..pref.len() {
            arr[i] = pref[i] ^ pref[i - 1];
        }

        arr
    }
}
