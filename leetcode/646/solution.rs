/**
 * https://leetcode.com/problems/maximum-length-of-pair-chain/
 * 646. Maximum Length of Pair Chain
 */

impl Solution {
    pub fn find_longest_chain(mut pairs: Vec<Vec<i32>>) -> i32 {
        pairs.sort_unstable_by_key(|x| x[1]);
        let (mut count, mut end) = (0, i32::MIN);
        pairs
            .iter()
            .map(|x| (x[0], x[1]))
            .for_each(|(left, right)| {
                if end < left {
                    count += 1;
                    end = right;
                }
            });
        count
    }
}
