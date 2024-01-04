/**
 * https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
 * 2870. Minimum Number of Operations to Make Array Empty
 */
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let mut total = 0;
        let mut counter: HashMap<i32, i32> = HashMap::new();
        for n in nums {
            *counter.entry(n).or_default() += 1;
        }
        for &(mut counts) in counter.values() {
            let mut ops = 0;
            while counts > 5 {
                counts -= 3;
                ops += 1;
            }
            match counts {
                5 | 4 => ops += 2,
                3 | 2 => ops += 1,
                1 => return -1,
                _ => {}
            }
            total += ops;
        }
        total
    }
}
