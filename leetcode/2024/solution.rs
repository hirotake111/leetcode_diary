/**
 * https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/
 * 2024. Maximize the Confusion of an Exam
 */
impl Solution {
    // Sliding window approach
    pub fn max_consecutive_answers(answer_key: String, k: i32) -> i32 {
        let a = Self::window(&answer_key.as_bytes(), k, 'T' as u8);
        let b = Self::window(&answer_key.as_bytes(), k, 'F' as u8);
        a.max(b)
    }

    fn window(keys: &[u8], mut skip: i32, v: u8) -> i32 {
        let mut slow = 0;
        let mut answer = 0;

        for fast in 0..keys.len() {
            if keys[fast] == v {
                skip -= 1;
            }
            while skip < 0 {
                if keys[slow] == v {
                    skip += 1;
                }
                slow += 1;
            }
            answer = answer.max(fast - slow + 1);
        }
        answer as i32
    }
}
