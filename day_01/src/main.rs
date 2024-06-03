fn part1(input: &str) -> u32 {
    let output: u32 = input
        .lines()
        .map(|line| {
            let mut it = 
                line.chars().filter_map(|character| {
                    character.to_digit(10)
                });
            let first: u32 = it.next().expect("Should be a number");
            let last: Option<u32> = it.last();

            match last {
                Some(num) =>    format!("{first}{num}"),
                None =>         format!("{first}{first}"),
            }
                .parse::<u32>()
                .expect("Should be a number")
        })
        .sum::<u32>();
        output
        
    // let _output: String = input
    //     .lines()
    //     .inspect(|line| {
    //         dbg!(line);
    //     })
    //     .collect();
    // println!("_output: {_output}");
    // 1
}

fn main() {
    let input: &str = include_str!("python/input.txt");

    let output: u32 = part1(input);
    println!("output: {}", output);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_test() {
        let result = part1("1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet",);

        assert_eq!(result, 142);
    }
}

