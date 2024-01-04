/**
 * https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
 * 2125. Number of Laser Beams in a Bank
 */
impl Solution {
    pub fn number_of_beams(bank: Vec<String>) -> i32 {
        bank.into_iter()
            .map(count_ones)
            .filter(|n| *n > 0)
            .collect::<Vec<i32>>()
            .windows(2)
            .fold(0, |acc, w| acc + w[0] * w[1])
    }
}

fn count_ones(s: String) -> i32 {
    s.chars().filter(is_one).count() as i32
}

fn is_one(c: &char) -> bool {
    *c == '1'
}
