/**
 * https://leetcode.com/problems/non-overlapping-intervals/
 * 435. Non-overlapping Intervals
 *
 * Given an array of intervals intervals where intervals[i] = [start_i, end_i],
 * return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
 */
impl Solution {
    pub fn erase_overlap_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        let mut count = intervals.len() as i32;
        let mut intervals = intervals
            .iter()
            .map(|i| (i[0], i[1]))
            .collect::<Vec<(i32, i32)>>();
        intervals.sort_by(|a, b| a.1.cmp(&b.1));

        let mut edge = intervals[0].0;
        for (start, end) in intervals {
            if edge <= start {
                edge = end;
                count -= 1;
            }
        }

        count
    }
}
