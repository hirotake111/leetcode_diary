/**
 * https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
 * 81. Search in Rotated Sorted Array II
 */
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> bool {
        let mut begin = 0;
        let mut end = nums.len() - 1;
        search_rotated(&nums, target, begin, end)
    }
}

fn search_rotated(nums: &Vec<i32>, target: i32, mut begin: usize, mut end: usize) -> bool {
    // move begin to remove duplication
    while nums[begin] == nums[end] {
        begin += 1;
        if end <= begin {
            // All elements between begin and end are the same
            return nums[end] == target;
        }
    }
    let mid = (begin + end) / 2;
    if nums[begin] == target || nums[mid] == target || nums[end] == target {
        return true;
    }
    if begin == mid {
        // No rotation can't be performed anymore
        return false;
    }
    if nums[begin] <= nums[mid] {
        // No rotation between begin and mid
        if nums[begin] <= target && target <= nums[mid] {
            return nums[begin..=mid].binary_search(&target).is_ok();
        }
        // target should be between mid and end
        return search_rotated(nums, target, mid, end);
    }
    // No rotation between mid and end
    if nums[mid] <= target && target <= nums[end] {
        return nums[mid..=end].binary_search(&target).is_ok();
    }
    // target should be between begin and mid
    return search_rotated(nums, target, begin, mid);
}
