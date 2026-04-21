/*
    [HARD]
    68. Text Justification

    Concepts:
    - string
    - simulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.24 MB   [Beats 80.33%]
*/
impl Solution {
    pub fn full_justify(words: Vec<String>, max_width: i32) -> Vec<String> {
        /*
            1) Store lines in list
            2) Add words to line until word length > line length
            3) Join words by adding up lengths, subtracting total
                letter length by max_width, then floor-dividing
                by number of words
        */
        let max_width: i8 = max_width as i8;
        let mut lines: Vec<Vec<String>> = Vec::new();
        let mut line: Vec<String> = Vec::new();
        let mut gaps: Vec<f32> = Vec::new();
        let mut words_in_line: i8 = 0;
        let mut num_letters: i8 = 0;
        let [mut line_len, mut word_len, mut num_spaces, mut num_gaps]: [i8; 4] = [0, 0, 0, 0];
        let mut space: f32 = 0.0;
        let mut res: String = String::new();
        let mut ans: Vec<String> = Vec::new();

        // split words up into lines
        for word in words {
            line_len = line.len() as i8;
            word_len = word.len() as i8;

            if (words_in_line - 1) + num_letters + word_len < max_width {
                words_in_line += 1;
                num_letters += word_len;
                line.push(word);
            } else {
                lines.push(line);
                words_in_line = 1;
                num_letters = word_len;
                line = Vec::from([word]);
            }
        }

        if !line.is_empty() {
            lines.push(line);
        }

        // add spaces as necessary
        for (i, wrds) in lines.iter().enumerate() {
            num_letters = wrds
                .iter()
                .map(|item| item.len() as i8)
                .fold(0, |a, b| a + b);

            num_spaces = max_width - num_letters;
            num_gaps = lines[i].len() as i8 - 1;

            // store number of spaces needed to fill gaps
            gaps.clear();
            while num_gaps >= 0 {
                space = (num_spaces as f32 / num_gaps as f32).ceil();
                gaps.push(space);

                num_spaces -= space as i8;
                num_gaps -= 1;
            }

            // different logic for last line
            res.clear();
            if i == lines.len() - 1 {
                for j in 0..lines[i].len() - 1 {
                    res.push_str(lines[i][j].as_str());
                    res.push(' ');
                }
            } else {
                for j in 0..lines[i].len() - 1 {
                    res.push_str(lines[i][j].as_str());
                    res.push_str(" ".repeat(gaps[j] as usize).as_str());
                }
            }

            res.push_str(lines[i].last().unwrap().as_str());

            // pad zeroes if needed
            let remaining_spaces: usize = max_width as usize - res.len();
            res.push_str(" ".repeat(remaining_spaces).as_str());
            ans.push(res.clone());
        }

        return ans;
    }
}