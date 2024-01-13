/**
 * https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=daily-question&envId=2024-01-05
 * 1704. Determine if String Halves Are Alike
 */
impl Solution {
    pub fn halves_are_alike(s: String) -> bool {
        let n = s.len() / 2;
        let s: Vec<char> = s.chars().collect();
        let (mut a, mut b) = (0, 0);
        for (c1, c2) in (0..n).map(|i| (s[i], s[i + n])) {
            a += if "aeiouAEIOU".contains(c1) { 1 } else { 0 };
            b += if "aeiouAEIOU".contains(c2) { 1 } else { 0 };
        }
        a == b
    }
}
