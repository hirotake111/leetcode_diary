/**
 * https://leetcode.com/problems/reverse-words-in-a-string-iii/
 * 557. Reverse Words in a String III
 */
impl Solution {
    pub fn reverse_words(s: String) -> String {
        s.split(" ")
            .map(|w| w.chars().rev().collect())
            .collect::<Vec<String>>()
            .join(" ")
    }
}
