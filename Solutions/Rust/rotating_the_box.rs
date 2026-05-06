/*
    [MEDIUM]
    1861. Rotating the Box

    Concepts:
    - matrix
    - two pointers

    Stats:
        Runtime | 10 ms     [Beats 57.14%]
        Memory  | 18.90 MB  [Beats 57.14%]
*/
impl Solution {
    pub fn rotate_the_box(bocks: Vec<Vec<char>>) -> Vec<Vec<char>> {
        let [m, n] = [bocks.len(), bocks[0].len()];
        let mut res = vec![vec!['.'; m]; n];

        for i in 0..m {
            for j in 0..n {
                res[j][m-1-i] = bocks[i][j];
            }
        }

        // iterate over all columns
        for j in 0..m {
            let [mut i, mut bottom] = [n - 1; 2];
            while i >= 0 {
                // find lowest empty space for bottom
                if res[i][j] == '*' { bottom = i - 1; }
                // swap stone w lowest space and update
                else if res[i][j] == '#' {
                    [res[i][j], res[bottom][j]] = [res[bottom][j], res[i][j]];
                    bottom -= 1;
                }

                // if at top of col, break
                if i == 0 { break; }
                i -= 1;
            }
        }

        return res;
    }
}