/*
    [MEDIUM]
    56. Merge Intervals

    Concepts:
    - array
    - prefix/suffix sum

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 3.10 MB   [Beats 64.20%]
*/
use std::collections::HashSet;

impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n: usize = *intervals
            .iter()
            .map(|it| {
                it
                    .iter()
                    .max()
                    .unwrap()
            })
            .max()
            .unwrap() as usize;
        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut rng: Vec<i32> = Vec::new();
        let mut singles: HashSet<i32> = HashSet::new();
        let [mut pref, mut suff] = [vec![0; n + 1], vec![0; n + 1]];

        for intv in intervals {
            if let [s, e] = intv[..] {
                if s == e {
                    singles.insert(s);
                    continue;
                }

                pref[s as usize] += 1;
                pref[e as usize] -= 1;

                suff[e as usize] += 1;
                suff[s as usize] -= 1;
            }
        }

        for i in 1..=n {
            pref[i] += pref[i-1];
            suff[n-i] += suff[n-i+1];
        }

        for i in 0..=n {
            if pref[i] != 0 && suff[i] == 0 {
                rng.clear();
                rng.push(i as i32);
            } else if pref[i] == 0 && suff[i] != 0 {
                res.push([rng.clone(), Vec::from([i as i32])].concat());
                rng.clear();
            } else if pref[i] == 0 && suff[i] == 0 {
                if singles.contains(&(i as i32)) {
                    res.push(Vec::from([i as i32; 2]));
                }
            }
        }

        return res
            .into_iter()
            .map(|it| {
                it
                    .into_iter()
                    .map(|v| v as i32)
                    .collect()
            })
            .collect();
    }
}