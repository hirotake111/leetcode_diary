/**
 * https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
 * 2369. Check if There is a Valid Partition For The Array
 */
use std::collections::HashSet;

impl Solution {
    pub fn valid_partition(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut falses = HashSet::<usize>::new();

        fn dfs(v: &Vec<i32>, i: usize, mut falses: &mut HashSet<usize>) -> bool {
            let n = v.len();
            if i == n {
                return true;
            }
            if falses.contains(&i) {
                return false;
            }
            if i + 1 < n && v[i] == v[i + 1] && dfs(&v, i + 2, &mut falses) {
                return true;
            }
            if i + 2 < n {
                if v[i] == v[i + 1] && v[i] == v[i + 2] && dfs(&v, i + 3, &mut falses) {
                    return true;
                }
                if v[i] + 1 == v[i + 1] && v[i] + 2 == v[i + 2] && dfs(&v, i + 3, &mut falses) {
                    return true;
                }
            }
            falses.insert(i);
            false
        }

        dfs(&nums, 0, &mut falses)
    }
}
