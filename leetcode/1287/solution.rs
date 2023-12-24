/**
 * https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
 * 1287. Element Appearing More Than 25% In Sorted Array
 */
impl Solution {
    pub fn find_special_integer(arr: Vec<i32>) -> i32 {
        let n = arr.len() / 4;
        for (i, &m) in arr.iter().enumerate() {
            if m == arr[i + n] {
                return m;
            }
        }
        unreachable!()
    }
}
