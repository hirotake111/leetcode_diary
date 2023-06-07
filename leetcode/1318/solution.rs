// https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
// 1318. Minimum Flips to Make a OR b Equal to c
// Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
// Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

impl Solution {
    pub fn min_flips(mut a: i32, mut b: i32, mut c: i32) -> i32 {
        let mut flips = 0;
        // Loop over until a, b, and c are all 0.
        // In each iteration, we compare the 1st bit, and increment flips if needed.
        // Right-shift a, b, and c for the next iteration
        while 0 < a || 0 < b || 0 < c {
            if c & 1 == 1 {
                // Either a or b must be 1
                // -> add 1 if both a and b are 0
                flips += ((a & 1) | (b & 1)) ^ 1;
            } else {
                // Both a and b must be 0
                // -> add 1 if each of a and b is 1 respectively
                flips += (a & 1) + (b & 1);
            }
            a = a >> 1;
            b = b >> 1;
            c = c >> 1;
        }
        flips
    }
}
