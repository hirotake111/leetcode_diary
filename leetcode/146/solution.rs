use std::{cell::RefCell, collections::HashMap, fmt::Display, rc::Rc};

struct LRUCache {
    capacity: usize,
    cache: HashMap<i32, Rc<RefCell<LinkedNode>>>,
    dll: DoublyLinkedList,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl LRUCache {
    fn new(capacity: i32) -> Self {
        Self {
            capacity: capacity as usize,
            cache: HashMap::new(),
            dll: DoublyLinkedList::new(),
        }
    }

    fn get(&mut self, key: i32) -> i32 {
        if let Some(node) = self.cache.get(&key) {
            // Cache hit -> update doubly linked list
            self.dll.move_to_tail(Rc::clone(&node));
            return node.borrow().val.clone();
        }
        -1
    }

    fn put(&mut self, key: i32, value: i32) {
        match self.cache.get(&key) {
            Some(node) => {
                node.borrow_mut().val = value;
                self.dll.move_to_tail(Rc::clone(&node));
            }
            None => {
                let new_node = Rc::new(RefCell::new(LinkedNode::new(key, value)));
                self.cache.insert(key, Rc::clone(&new_node));
                self.dll.push_tail(Rc::clone(&new_node));
                if self.capacity < self.cache.len() {
                    let key = self.dll.pop_head();
                    self.cache.remove(&key);
                }
            }
        }
    }
}

struct DoublyLinkedList {
    head: Option<Rc<RefCell<LinkedNode>>>,
    tail: Option<Rc<RefCell<LinkedNode>>>,
}

impl DoublyLinkedList {
    pub fn new() -> Self {
        Self {
            head: None,
            tail: None,
        }
    }

    fn get_head(&self) -> Option<Rc<RefCell<LinkedNode>>> {
        match &self.head {
            Some(head) => Some(Rc::clone(head)),
            None => None,
        }
    }

    fn get_tail(&self) -> Option<Rc<RefCell<LinkedNode>>> {
        match &self.tail {
            Some(tail) => Some(Rc::clone(tail)),
            None => None,
        }
    }

    pub fn push_tail(&mut self, node: Rc<RefCell<LinkedNode>>) {
        match &self.get_tail() {
            Some(prev_tail) => {
                prev_tail.borrow_mut().next.replace(Rc::clone(&node));
                node.borrow_mut().prev = Some(Rc::clone(&prev_tail));
            }
            None => {
                // This node should be the 1st node
                node.borrow_mut().prev = None;
                self.head = Some(Rc::clone(&node));
            }
        }
        node.borrow_mut().next = None;
        self.tail = Some(Rc::clone(&node));
    }

    pub fn move_to_tail(&mut self, node: Rc<RefCell<LinkedNode>>) {
        self.remove(Rc::clone(&node));
        self.push_tail(Rc::clone(&node));
    }

    pub fn pop_head(&mut self) -> i32 {
        if let Some(head) = &self.head {
            return self.remove(Rc::clone(&head));
        }
        -1
    }

    pub fn remove(&mut self, node: Rc<RefCell<LinkedNode>>) -> i32 {
        let prev = self.get_prev(Rc::clone(&node));
        let next = self.get_next(Rc::clone(&node));
        let key = node.borrow().key;
        match (prev, next) {
            (Some(prev), Some(next)) => {
                // node was in the middle of doubly linked list
                prev.borrow_mut().next.replace(Rc::clone(&next));
                next.borrow_mut().prev.replace(Rc::clone(&prev));
            }
            (Some(prev), None) => {
                // The node should be the tail
                prev.borrow_mut().next.take();
                self.tail.replace(Rc::clone(&prev));
            }
            (None, Some(next)) => {
                // The node should be the head
                next.borrow_mut().prev.take();
                self.head.replace(Rc::clone(&next));
            }
            (None, None) => {
                // The node should be head and tail
                self.head.take();
                self.tail.take();
            }
        }
        key
    }

    fn get_prev(&self, node: Rc<RefCell<LinkedNode>>) -> Option<Rc<RefCell<LinkedNode>>> {
        match &node.borrow().prev {
            Some(prev) => Some(Rc::clone(&prev)),
            None => None,
        }
    }

    fn get_next(&self, node: Rc<RefCell<LinkedNode>>) -> Option<Rc<RefCell<LinkedNode>>> {
        match &node.borrow().next {
            Some(next) => Some(Rc::clone(&next)),
            None => None,
        }
    }
}

struct LinkedNode {
    key: i32,
    val: i32,
    prev: Option<Rc<RefCell<LinkedNode>>>,
    next: Option<Rc<RefCell<LinkedNode>>>,
}

impl Display for LinkedNode {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}: {}", self.key, self.val)
    }
}

impl LinkedNode {
    pub fn new(key: i32, val: i32) -> Self {
        Self {
            key,
            val,
            prev: None,
            next: None,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::LRUCache;

    #[test]
    fn it_works() {
        let mut lru = LRUCache::new(2);
        lru.put(1, 1);
        lru.put(2, 2);
        assert_eq!(lru.get(1), 1);
        lru.put(3, 3);
        assert_eq!(lru.get(2), -1);
        lru.put(4, 4);
        assert_eq!(lru.get(1), -1);
        assert_eq!(lru.get(3), 3);
        assert_eq!(lru.get(4), 4);
    }

    #[test]
    fn test_case1() {
        let mut lru = LRUCache::new(3);
        lru.put(1, 1);
        lru.put(2, 2);
        lru.put(3, 3);
        assert_eq!(lru.get(3), 3);
        assert_eq!(lru.get(1), 1);
        lru.put(4, 4);
        assert_eq!(lru.get(2), -1);
        assert_eq!(lru.get(1), 1);
        lru.put(3, 3);
        assert_eq!(lru.get(1), 1);
        lru.put(4, 4);
        assert_eq!(lru.get(1), 1);
        assert_eq!(lru.get(2), -1);
        lru.put(1, 2);
        assert_eq!(lru.get(1), 2);
        assert_eq!(lru.get(2), -1);
        lru.put(4, 2);
        lru.put(5, 5);
        assert_eq!(lru.get(3), -1);
        assert_eq!(lru.get(4), 2);
    }
}
