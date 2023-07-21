/**
 * https://leetcode.com/problems/asteroid-collision/
 * 735. Asteroid Collision
 *
 * We are given an array asteroids of integers representing asteroids in a row.
 * For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
 * Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
 */

impl Solution {
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        use std::cmp::Ordering;
        let mut stack: Vec<i32> = vec![];

        let mut i = 0;
        while i < asteroids.len() {
            let astr = asteroids[i];
            let last = stack.last();

            if astr > 0 || last.is_none() {
                stack.push(astr);
                i += 1;
                continue;
            }

            let last = *last.unwrap();
            if last < 0 {
                stack.push(astr);
                i += 1;
                continue;
            }

            // Collision occurs
            match last.cmp(&astr.abs()) {
                Ordering::Greater => {
                    // astr explodes
                    i += 1;
                }
                Ordering::Equal => {
                    // Both explode
                    stack.pop();
                    i += 1;
                }
                Ordering::Less => {
                    // last explodes
                    stack.pop();
                }
            }
        }
        stack
    }
}
