/**
 * https://leetcode.com/problems/maximum-score-after-splitting-a-string/
 * 1422. Maximum Score After Splitting a String
 */
impl Solution {
    pub fn max_score(s: String) -> i32 {
        let mut zeroes = 0;
        let mut ones = s.chars().filter(|n| *n == '1').count() as i32;
        let s = s.chars().collect::<Vec<char>>();
        let mut total = -1;
        println!("{}", zeroes + ones);
        for i in 0..(s.len() - 1) {
            if s[i] == '0' {
                zeroes += 1;
            } else {
                ones -= 1;
            }
            total = total.max(zeroes + ones);
        }
        total
    }
}
