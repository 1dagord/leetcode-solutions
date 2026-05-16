/*
    [MEDIUM]
    71. Simplify Path

    Concepts:
    - stack
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.24 MB   [Beats 85.71%]
*/
impl Solution {
    pub fn simplify_path(path: String) -> String {
        let dirs = path.split("/");
        let mut stack = Vec::new();

        for dir in dirs {
            if !dir.is_empty() {
                if dir == ".." {
                    match stack.pop() { _ => {} }
                } else if dir == "." {
                    continue;
                } else {
                    stack.push(dir);
                }
            }
        }

        return String::from("/") + &stack.join("/");
    }
}