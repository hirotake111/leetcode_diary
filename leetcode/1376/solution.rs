#[allow(dead_code)]
struct Solution {}

impl Solution {
    pub fn num_of_minutes(n: i32, head_id: i32, manager: Vec<i32>, inform_time: Vec<i32>) -> i32 {
        // DFS approach
        // Create graph
        let mut graph: Vec<Vec<usize>> = vec![vec![]; n as usize];
        for (e, &m) in manager.iter().enumerate() {
            if m != -1 {
                graph[m as usize].push(e);
            }
        }

        Self::dfs(head_id as usize, 0, &graph, &inform_time)
    }

    fn dfs(m: usize, minutes: i32, graph: &Vec<Vec<usize>>, time: &Vec<i32>) -> i32 {
        let subordinates: &Vec<usize> = &graph[m];
        let mut max_minutes = 0;
        if subordinates.len() == 0 {
            return minutes;
        }
        for &sub in subordinates {
            max_minutes = max_minutes.max(Self::dfs(sub, minutes + time[m], graph, time));
        }
        max_minutes
    }

    // pub fn num_of_minutes(n: i32, head_id: i32, manager: Vec<i32>, inform_time: Vec<i32>) -> i32 {
    // BFS approach
    // use std::collections::{HashMap, VecDeque};

    // // Create graph
    // let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
    // for (e, &m) in manager.iter().enumerate() {
    // let e = e as i32;
    // graph.entry(m).or_insert(vec![]).push(e);
    // }

    // // enqueue the first item (the head of the company)
    // let mut queue: VecDeque<(i32, i32)> = VecDeque::with_capacity(n as usize);
    // let mut answer = 0;
    // queue.push_back((head_id, 0));
    // while let Some((man, minutes)) = queue.pop_front() {
    // // If manager has subordinate(s), push them to the queue
    // // If not, update answer
    // match graph.get(&man) {
    // Some(subordinates) => {
    // for &sub in subordinates {
    // queue.push_back((sub, minutes + inform_time[man as usize]));
    // }
    // }
    // None => {
    // answer = answer.max(minutes);
    // }
    // }
    // }

    // answer
    // }
}
