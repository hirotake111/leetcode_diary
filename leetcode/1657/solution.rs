/**
 * https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=daily-question&envId=2024-01-14
 * 1657. Determine if Two Strings Are Close
 */
impl Solution {
    pub fn close_strings(word1: String, word2: String) -> bool {
        use std::collections::{HashMap, HashSet};
        if word1.len() != word2.len() {
            return false;
        }
        let set1 = word1.chars().collect::<HashSet<char>>();
        let set2 = word2.chars().collect::<HashSet<char>>();
        if set1 != set2 {
            return false;
        }
        let mut arr1 = [0; 26];
        for i in word1.bytes().map(|b| b as usize - 97) {
            arr1[i] += 1;
        }
        let mut arr2 = [0; 26];
        for i in word2.bytes().map(|b| b as usize - 97) {
            arr2[i] += 1;
        }
        arr1.sort_unstable();
        arr2.sort_unstable();
        arr1 == arr2
    }
}
