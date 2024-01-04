/**
 * https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
 * 2610. Convert an Array into a 2D Array with Conditions
 */
use std::collections::HashMap;

impl Solution {
    pub fn find_matrix(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut counter: HashMap<i32, usize> = HashMap::new();
        nums.into_iter()
            .for_each(|n| *counter.entry(n).or_default() += 1);

        let mut max_val = counter.values().fold(0, |acc, cur| acc.max(*cur));
        let mut arr = vec![vec![]; max_val];
        for (n, count) in counter {
            for i in (0..count) {
                arr[i].push(n);
            }
        }

        arr
    }
}
