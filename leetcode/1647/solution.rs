/**
 * https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
 * 1647. Minimum Deletions to Make Character Frequencies Unique
 */
impl Solution {
    pub fn min_deletions(s: String) -> i32 {
        let mut counter: Vec<usize> = vec![0; 26];
        for i in s.into_bytes().iter().map(|b| (b - 97) as usize) {
            counter[i] += 1;
        }

        let max_value = counter.iter().max().unwrap();
        let mut freq: Vec<usize> = vec![0; max_value + 1];
        for &count in &counter {
            if count > 0 {
                freq[count] += 1;
            }
        }

        let mut answer = 0;
        let mut extra = 0;
        for f in freq.iter().skip(1).rev() {
            let f = f + extra;
            if f > 1 {
                extra = f - 1;
                answer += extra;
            } else {
                extra = 0;
            }
        }
        answer as i32
    }
}
