/**
 * https://leetcode.com/problems/search-in-rotated-sorted-array/
 * 33. Search in Rotated Sorted Array
 *
 * Recursively perform binary search:
 * - If there is no rotation between two indexes, perform binary search.
 * - Otherwise, recursively find new two indexes in which there is no rotation.
 *
 * Time Complexity: O(logN)
 * Space Complexity: O(1)
 */
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut begin, mut end) = (0, nums.len() - 1);
        if nums[begin] < nums[end] {
            binary_search(&nums, target, begin, end)
        } else {
            rotated_binary_search(&nums, target, begin, end)
        }
    }
}

pub fn rotated_binary_search(nums: &Vec<i32>, target: i32, begin: usize, end: usize) -> i32 {
    let mid = (begin + end) / 2;
    if nums[begin] == target {
        return begin as i32;
    }
    if nums[mid] == target {
        return mid as i32;
    }
    if nums[end] == target {
        return end as i32;
    }
    if begin == mid {
        return -1;
    }
    if nums[begin] < nums[mid] {
        // begin-mid: no rotation
        // mid-end: has a rotation
        if nums[begin] < target && target < nums[mid] {
            binary_search(&nums, target, begin, mid)
        } else {
            // target might be somewhere between mid-end
            rotated_binary_search(&nums, target, mid, end)
        }
    // begin-mid: has a rotation
    // mid-end: no rotation
    } else if nums[mid] < target && target < nums[end] {
        binary_search(&nums, target, mid, end)
    } else {
        // target might be somewhere between begin-mid
        rotated_binary_search(&nums, target, begin, mid)
    }
}

fn binary_search(nums: &Vec<i32>, target: i32, mut begin: usize, mut end: usize) -> i32 {
    if nums[begin] == target {
        return begin as i32;
    }
    if nums[end] == target {
        return end as i32;
    }

    while begin < end {
        let mid = (begin + end) / 2;
        if nums[mid] == target {
            return mid as i32;
        }
        if nums[mid] < target {
            begin = mid + 1;
        } else {
            end = mid;
        }
    }

    if nums[begin] == target {
        begin as i32
    } else {
        -1
    }
}
