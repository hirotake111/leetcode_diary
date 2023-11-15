/**
 * https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
 * 1846. Maximum Element After Decreasing and Rearranging
 */

impl Solution {
    pub fn maximum_element_after_decrementing_and_rearranging(mut arr: Vec<i32>) -> i32 {
        arr.sort_unstable();
        arr.into_iter().skip(1).fold(1, stay_or_increment)
    }
}

fn stay_or_increment(acc: i32, cur: i32) -> i32 {
    cur.min(acc + 1)
}
