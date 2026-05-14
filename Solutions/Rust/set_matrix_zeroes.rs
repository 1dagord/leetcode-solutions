/*
    [MEDIUM]
    73. Set Matrix Zeroes

    Concepts:
    - matrix

    Stats:
        Runtime | 11 ms     [Beats 13.25%]
        Memory  | 2.55 MB   [Beats 53.01%]
*/
impl Solution {
    pub fn set_zeroes(mat: &mut Vec<Vec<i32>>) {
        let [m, n] = [mat.len(), mat[0].len()];
        let mut matrix = mat
            .into_iter()
            .map(|row| {
                row
                    .into_iter()
                    .map(|v| Some(*v as i32))
                    .collect::<Vec<Option<i32>>>()
            })
            .collect::<Vec<Vec<Option<i32>>>>();

        for i in 0..m {
            for j in 0..n {
                match matrix[i][j] {
                    Some(val) => {
                        if val == 0 {
                            for row in 0..m {
                                if row != i && mat[row][j] != 0 { matrix[row][j] = None; }
                            }
                            for col in 0..n {
                                if col != j && mat[i][col] != 0 { matrix[i][col] = None; }
                            }
                        }
                    },
                    None => {}
                }
            }
        }

        for i in 0..m {
            for j in 0..n {
                match matrix[i][j] {
                    Some(_) => {},
                    None => { mat[i][j] = 0; }
                }
            }
        }
    }
}