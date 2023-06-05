struct UnionFind {
    roots: Vec<usize>,
    n: usize,
}

impl UnionFind {
    pub fn new(n: usize) -> Self {
        let roots: Vec<usize> = (0..n).collect();
        Self { roots, n }
    }

    fn find(&mut self, idx: usize) -> usize {
        let root = self.roots[idx];
        if root != idx {
            self.roots[idx] = self.find(root);
        }
        self.roots[idx]
    }

    pub fn union(&mut self, idx_a: usize, idx_b: usize) {
        let (root_a, root_b) = (self.find(idx_a), self.find(idx_b));
        if root_a == root_b {
            return;
        }
        self.n -= 1;
        if root_a < root_b {
            self.roots[root_b] = root_a;
        } else {
            self.roots[root_a] = root_b;
        }
    }
}

impl Solution {
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let n = is_connected.len();
        let mut uf = UnionFind::new(n);
        for i in 0..n {
            ((i + 1)..n)
                .filter(|&j| is_connected[i][j] == 1)
                .for_each(|j| uf.union(i, j))
        }
        uf.n as i32
    }
}
