/*
    [MEDIUM]
    54. Spiral Matrix

    Concepts:
    - matrix
    - simulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.33 MB   [Beats 22.47%]
*/
impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        // `i` beholden to `m`
        // `j` beholden to `n`
        let [m, n] = [matrix.len() - 1, matrix[0].len() - 1];
        let mut visited: Vec<Vec<i32>> = vec![vec![0; n+1]; m+1];
        let mut path: Vec<i32> = Vec::new();

        const RIGHT: i8 = 1 << 0;
        const DOWN: i8 = 1 << 1;
        const LEFT: i8 = 1 << 2;
        const UP: i8 = 1 << 3;

        let mut direc: i8 = RIGHT;
        let [mut i, mut j] = [0, 0];

        for num_visited in 0..(m+1)*(n+1) {
            if visited[i][j] == 0 {
                visited[i][j] = 1;
                path.push(matrix[i][j]);
            }

            // move in same direction until edge or
            // visited square reached, then
            // change direction
            match direc {
                RIGHT => {
                    if j < n && visited[i][j+1] == 0 {
                        j += 1;
                    } else {
                        direc = DOWN;
                        i += 1;
                    }
                },
                DOWN => {
                    if i < m && visited[i+1][j] == 0 {
                        i += 1;
                    } else {
                        direc = LEFT;
                        j -= 1;
                    }
                },
                LEFT => {
                    if j > 0 && visited[i][j-1] == 0 {
                        j -= 1;
                    } else {
                        direc = UP;
                        i -= 1;
                    }
                },
                UP => {
                    if i > 0 && visited[i-1][j] == 0 {
                        i -= 1;
                    } else {
                        direc = RIGHT;
                        j += 1;
                    } 
                },
                _ => break
            }
        }

        return path;
    }
}