/**
 * https://leetcode.com/problems/min-cost-climbing-stairs/
 * 746. Min Cost Climbing Stairs
 */

impl Solution {
    pub fn min_cost_climbing_stairs(mut cost: Vec<i32>) -> i32 {
        for i in (0..(cost.len() - 2)).rev() {
            cost[i] += cost[i + 1].min(cost[i + 2]);
        }
        cost[0].min(cost[1])
    }
}
