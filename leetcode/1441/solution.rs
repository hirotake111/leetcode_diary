/**
 * https://leetcode.com/problems/build-an-array-with-stack-operations/
 * 1441. Build an Array With Stack Operations
 */

impl Solution {
    pub fn build_array(target: Vec<i32>, n: i32) -> Vec<String> {
        let mut i = 0;
        let mut ops = vec![];

        for current in 1..=n {
            ops.push("Push".to_string());
            if current != target[i] {
                ops.push("Pop".to_string());
            } else {
                i += 1;
                if i == target.len() {
                    break;
                }
            }
        }

        ops
    }
}
