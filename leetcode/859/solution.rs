/**
 * https://leetcode.com/problems/buddy-strings/
 * 859. Buddy Strings
 * Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
 * Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
 * For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 */
struct Solution {}

impl Solution {
    pub fn buddy_strings(s: String, goal: String) -> bool {
        use std::collections::HashSet;
        let (mut prev_a, mut prev_b) = ('a', 'a');
        let mut swapped = false;

        if s.len() != goal.len() {
            return false;
        }

        if s == goal {
            // If s has duplicated character they can be buddy strings
            let hs = s.chars().collect::<HashSet<char>>();
            return hs.len() < s.len();
        }
        for (a, b) in s.chars().zip(goal.chars()) {
            if a == b {
                continue;
            }

            if swapped {
                return false;
            }

            if prev_a == prev_b {
                prev_a = a;
                prev_b = b;
            } else if prev_a == b && prev_b == a {
                swapped = true;
            } else {
                return false;
            }
        }
        swapped
    }
}
