/**
 * https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
 * 1464. Maximum Product of Two Elements in an Array
 */
impl Solution {
    pub fn max_product(mut nums: Vec<i32>) -> i32 {
        let (mut largest, mut largest_2nd) = (-1, -1);
        for n in nums {
            if n > largest {
                largest_2nd = largest;
                largest = n;
            } else if n >= largest_2nd {
                largest_2nd = n;
            }
        }
        (largest - 1) * (largest_2nd - 1)
    }
}
