/**
 * https://leetcode.com/problems/arithmetic-subarrays/
 * 1630. Arithmetic Subarrays
 */
impl Solution {
    pub fn check_arithmetic_subarrays(nums: Vec<i32>, l: Vec<i32>, r: Vec<i32>) -> Vec<bool> {
        l.into_iter()
            .zip(r.into_iter())
            .map(|(begin, end)| is_arithmetic(&nums[(begin as usize)..=(end as usize)]))
            .collect()
    }
}

fn is_arithmetic(nums: &[i32]) -> bool {
    use std::collections::HashSet;
    let min = *(nums.iter().min().unwrap()) as usize;
    let max = *(nums.iter().max().unwrap()) as usize;
    let mut diff = (max - min) as usize;
    if (diff % (nums.len() - 1)) != 0 {
        return false;
    }
    diff /= nums.len() - 1;
    let mut hs: HashSet<i32> = (0..nums.len()).map(|n| (min + n * diff) as i32).collect();
    for n in nums {
        if (!hs.remove(n) && diff != 0) {
            return false;
        }
    }
    true
}
