/**
 * https://leetcode.com/problems/image-smoother/
 * 661. Image Smoother
 */
impl Solution {
    pub fn image_smoother(img: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let (m, n) = (img.len(), img[0].len());
        (0..m)
            .map(|i| (0..n).map(|j| average(i, j, &img)).collect())
            .collect()
    }
}

fn average(row: usize, col: usize, v: &Vec<Vec<i32>>) -> i32 {
    let (m, n) = (v.len() as i32, v[0].len() as i32);
    let mut total = 0;
    let mut count = 0;
    for i in [-1, 0, 1] {
        let row = (row as i32) + i;
        if row < 0 || row >= m {
            continue;
        }
        for j in [-1, 0, 1] {
            let col = (col as i32) + j;
            if col < 0 || col >= n {
                continue;
            }
            total += v[row as usize][col as usize];
            count += 1;
        }
    }

    ((total as f32) / (count as f32)) as i32
}
