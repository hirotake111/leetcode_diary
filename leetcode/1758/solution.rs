/**
 * https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
 * 1758. Minimum Changes To Make Alternating Binary String
 */
impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let mut case_a = 0;
        let mut expect_zero = true;

        for c in s.chars() {
            match (expect_zero, c) {
                (true, '1') | (false, '0') => case_a += 1,
                _ => {}
            }
            expect_zero = !expect_zero;
        }

        case_a.min(s.len() as i32 - case_a)
    }
}
