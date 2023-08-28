/**
 * https://leetcode.com/problems/implement-stack-using-queues/
 * 225. Implement Stack using Queues
 */
use std::collections::VecDeque;

struct MyStack {
    q: VecDeque<i32>,
}

impl MyStack {
    fn new() -> Self {
        Self { q: VecDeque::new() }
    }

    fn push(&mut self, x: i32) {
        self.q.push_back(x);
        let mut counts = self.q.len();
        while let Some(item) = self.q.pop_front() {
            self.q.push_back(item);
            counts -= 1;
            if counts <= 1 {
                break;
            }
        }
    }

    fn pop(&mut self) -> i32 {
        self.q.pop_front().unwrap()
    }

    fn top(&self) -> i32 {
        *self.q.front().unwrap()
    }

    fn empty(&self) -> bool {
        self.q.is_empty()
    }
}
