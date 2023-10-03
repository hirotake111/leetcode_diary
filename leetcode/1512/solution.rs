/**
 * https://leetcode.com/problems/number-of-good-pairs/
 * 1512. Number of Good Pairs
 */
impl Solution {
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        let mut counter: [i32; 101] = [0; 101];
        let mut count = 0;
        for n in nums {
            let n = n as usize;
            count += counter[n];
            counter[n] += 1;
        }
        count
    }
}
