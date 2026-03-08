/*
    [EASY]
    1812. Determine Color of a Chessboard Square

    Concepts:
    - math
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.06 MB   [Beats 92.86%]
*/

impl Solution {
    pub fn square_is_white(coordinates: String) -> bool {
        let [_, letter, number, _]: [&str; 4] = coordinates
            .split("")
            .collect::<Vec<&str>>()
            .try_into()
            .unwrap();
        return (
            (
                (("a".as_bytes()[0] - letter.as_bytes()[0]) & 1)
                == 0
            )
            ^ (
                (number.parse::<u32>().unwrap() & 1)
                != 0
            )
        );
    }
}