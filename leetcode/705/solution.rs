struct MyHashSet {
    store: Vec<bool>,
}

const INITIAL_CAPACITY: usize = 256;

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashSet {

    fn new() -> Self {
        Self { store: vec![false; INITIAL_CAPACITY] }
    }
    
    fn add(&mut self, key: i32) {
        let key = key as usize;
        if self.store.len() <= key {
            let mut new_store: Vec<bool> = vec![false; key + 1];
            for i in 0..self.store.len() {
               new_store[i] = self.store[i];
            }
            std::mem::replace(&mut self.store, new_store);
        }
        self.store[key as usize] = true;
    }
    
    fn remove(&mut self, key: i32) {
        let key = key as usize;
        if self.store.len() <= key {
            return;
        }
        self.store[key as usize] = false;
    }
    
    fn contains(&self, key: i32) -> bool {
        let key = key as usize;
        if self.store.len() <= key {
            false
        } else {
            self.store[key as usize]
        }
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * let obj = MyHashSet::new();
 * obj.add(key);
 * obj.remove(key);
 * let ret_3: bool = obj.contains(key);
 */