fn day_01(input: &str) -> u32 {
    // 142
    let output: String = input
        .lines()
        .map(|line| {
            let it: = line.chars().filter_map(|character| {
                character.to_digit(10)
            })
        })
        // .inspect(|line| {
        //     dbg!(line)
        // })
        .collect();
    
}

fn main() {
    println!("{}", day_01("poop"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn day_01_test() {
        let result = day_01("1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet",);

        assert_eq!(result, 142);
    }
}

