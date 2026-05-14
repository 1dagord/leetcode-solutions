/*
    [MEDIUM]
    289. Game of Life

    Concepts:
    - matrix
    - simulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.18 MB   [Beats 63.16%]
*/
impl Solution {
    pub fn game_of_life(board: &mut Vec<Vec<i32>>) {
        /*
            < 2 live neighbors: dies
            2-3 live neighbors: survives
            >3 live neighbors: dies
            dead w 3 live neighbors: revived
        */
        let [m, n] = [board.len(), board[0].len()];
        let mut live_neighbors = 0;
        let [mut ni, mut nj];
        let mut next_state = board.clone();
        let moves: [(i32, i32); 8] = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        ];

        // get next state
        for i in 0..m {
            for j in 0..n {
                // get number of live neighbors
                live_neighbors = 0;
                for (di, dj) in moves {
                    [ni, nj] = [i as i32 + di, j as i32 + dj];
                    if (
                        0 <= ni && ni < m as i32
                        && 0 <= nj && nj < n as i32
                        && board[ni as usize][nj as usize] != 0
                    ) {
                        live_neighbors += 1;
                    }
                }

                // if current cell is live...
                if board[i][j] != 0 {
                    match live_neighbors {
                        nei if nei < 2 || nei > 3 => {
                            next_state[i][j] = 0;
                        },
                        2 | 3 => {
                            next_state[i][j] = 1;
                        },
                        _ => {}
                    }
                }
                // if current cell is dead...
                else {
                    if live_neighbors == 3 { next_state[i][j] = 1; }
                }
            }
        }

        for i in 0..m {
            board[i] = next_state[i].clone();
        }
    }
}