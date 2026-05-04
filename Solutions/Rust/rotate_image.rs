/*
    [MEDIUM]
    48. Rotate Image

    Concepts:
    - matrix
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.18 MB   [Beats 80.00%]
*/
impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let n = matrix.len();

        for i in 0..n {
            for j in i..n {
                [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
            }
        }

        matrix
            .iter_mut()
            .for_each(|vec| vec.reverse());
    }
}