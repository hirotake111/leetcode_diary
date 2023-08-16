/**
 * https://leetcode.com/problems/sliding-window-maximum/
 * 239. Sliding Window Maximum
 *
 * Monotonic queue (in decreasing order) approach
 */
use std::collections::VecDeque;

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut queue = VecDeque::<usize>::new();
        let mut answer: Vec<i32> = vec![];

        for (right, &n) in nums.iter().enumerate() {
            // left is left-most index of current k elements
            let left = right as i32 - k + 1;

            if left < 0 {
                // Just update the monotonic queue
                update_queue(&nums, &mut queue, n, right);
            } else {
                // If the largest value (queue.front()) is out of bound, pop it
                if let Some(&front) = queue.front() {
                    if left > front as i32 {
                        queue.pop_front();
                    }
                }
                // Update the monotonic queue
                update_queue(&nums, &mut queue, n, right);
                // Then update the answer
                if let Some(&idx) = queue.front() {
                    answer.push(nums[idx]);
                }
            }
        }

        answer
    }
}

fn update_queue(arr: &Vec<i32>, queue: &mut VecDeque<usize>, n: i32, idx: usize) {
    while let Some(&back) = queue.back() {
        if arr[back] < n {
            queue.pop_back();
        } else {
            break;
        }
    }
    queue.push_back(idx)
}
