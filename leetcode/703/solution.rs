use std::collections::BinaryHeap;
use std::cmp::Reverse;

struct KthLargest {
    k: usize,
    queue: BinaryHeap<Reverse<i32>>,
}



/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl KthLargest {
    fn new(k: i32, nums: Vec<i32>) -> Self {
        let k = k as usize;
        let queue = BinaryHeap::with_capacity(k + 1);
        let mut obj = Self { k, queue };
        nums.into_iter().for_each(|a| {
            obj.add(a);
        });
        obj
    }

    fn add(&mut self, val: i32) -> i32 {
        self.queue.push(Reverse(val));
        if self.k < self.queue.len() {
            self.queue.pop();
        }
        self.queue.peek().unwrap().0
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * let obj = KthLargest::new(k, nums);
 * let ret_1: i32 = obj.add(val);
 */