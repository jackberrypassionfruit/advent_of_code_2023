use regex::Regex;
// use std::collections::HashMap;

fn part1(input: &str) -> u32 {
    // let mut feas_games: Vec<u32> = Vec::new();
    let output = input
        .lines()
        .map(|line| {
            let game_line = line.trim();
            let re = Regex::new(r"; |, |: ").unwrap();
            let mut it = re.split(game_line);

            let game_num: u32 = it.next()
                .expect("Line should start with a Game num")
                [5..]
                .parse::<u32>()
                .expect("Should be a number");
            let nums_and_colors = it.map(|cube| {
                let mut v= cube.split(" ");
                let num: u32 =      v.next().expect("Should be a number")
                    .parse::<u32>().expect("Should be a number");
                let color: &str =   v.next().expect("Should be a color");
                (color, num)
            });


            let mut breakout: bool = false;

            for (color, num) in nums_and_colors {
                if color=="red" && num > 12 {
                    breakout = true;
                    break;
                } else if color=="green" && num > 13 {
                    breakout = true;
                    break;
                } else if color=="blue" && num > 14 {
                    breakout = true;
                    break;
                }
            }

            if !breakout {
                // feas_games.push(game_num);
                game_num
            } else {
                0
            }

            // 2
        })
        .sum::<u32>();
    output

    // feas_games.iter().fold(0, |acc, &x| acc + x)
}

fn main() {
    let input: &str = include_str!("../input.txt");
    let output: u32 = part1(input);

    println!("part1_answer: {output}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_test() {
        let test_input: &str = include_str!("../test_input.txt");
        let result = part1(test_input);

        assert_eq!(result, 8);
    }
}