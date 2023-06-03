#[allow(dead_code)]
struct Solution {}

impl Solution {
    #[allow(dead_code)]
    pub fn num_of_minutes(n: i32, head_id: i32, manager: Vec<i32>, inform_time: Vec<i32>) -> i32 {
        use std::collections::{HashMap, VecDeque};

        // Create graph
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for (e, &m) in manager.iter().enumerate() {
            let e = e as i32;
            graph.entry(m).or_insert(vec![]).push(e);
        }

        // enqueue the first item (the head of the company)
        let mut queue: VecDeque<(i32, i32)> = VecDeque::with_capacity(n as usize);
        let mut answer = 0;
        queue.push_back((head_id, 0));
        while let Some((man, minutes)) = queue.pop_front() {
            // If manager has subordinate(s), push them to the queue
            // If not, update answer
            match graph.get(&man) {
                Some(subordinates) => {
                    for &sub in subordinates {
                        queue.push_back((sub, minutes + inform_time[man as usize]));
                    }
                }
                None => {
                    answer = answer.max(minutes);
                }
            }
        }

        answer
    }
}
