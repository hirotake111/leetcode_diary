/**
 * https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
 * 1491. Average Salary Excluding the Minimum and Maximum Salary
 * You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
 * Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
 */

impl Solution {
    pub fn average(salary: Vec<i32>) -> f64 {
        let max = salary.iter().max().unwrap();
        let min = salary.iter().min().unwrap();
        let n = (salary.len() - 2);
        let total = salary.iter().fold(0, |a, c| a + c);
        (total - max - min) as f64 / n as f64
    }
}
