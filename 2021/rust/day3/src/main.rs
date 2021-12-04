use std::collections::HashMap;
use std::fs;
use std::str::FromStr;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");

    let (gamma_rate, epsilon_rate) = calculate_gamma_rate(data.lines());
    let answer = convert_bin_str(&gamma_rate) * convert_bin_str(&epsilon_rate);
    println!("Part 1 Answer: {}", answer);
    let oxy_rate = calc_oxygen_generator_rate(data.lines().collect(), 0);
    let co_rate = calc_co_scrub_rate(data.lines().collect(), 0);
    let part2_answer = convert_bin_str(&oxy_rate) * convert_bin_str(&co_rate);
    println!("Part2 Answer: {}", part2_answer)
}

fn calculate_gamma_rate<'a, I>(numbers: I) -> (String, String)
where
    I: IntoIterator<Item = &'a str>,
{
    let mut gamma_rate = String::with_capacity(15);
    let mut epsilon_rate = String::with_capacity(15);
    let mut value_counter = HashMap::new();
    let mut total_count = 0;

    for number in numbers {
        total_count += 1;
        for (i, num) in number.chars().enumerate() {
            match num {
                '1' => {
                    let counter = value_counter.entry(i).or_insert(0);
                    *counter += 1;
                }
                _ => {}
            }
        }
    }

    let half_total = total_count / 2;

    for i in 0..15 {
        match value_counter.get(&i) {
            Some(value) => {
                if value >= &half_total {
                    gamma_rate += "1";
                    epsilon_rate += "0";
                } else {
                    gamma_rate += "0";
                    epsilon_rate += "1";
                };
            }
            None => break,
        };
    }

    (gamma_rate, epsilon_rate)
}

fn calc_oxygen_generator_rate(numbers: Vec<&str>, index: usize) -> String {
    if numbers.len() == 1 {
        return String::from_str(numbers[0]).unwrap();
    };

    let mut number_map = HashMap::new();

    for number in numbers {
        match number.chars().nth(index).unwrap() {
            '1' => {
                let value = number_map.entry('1').or_insert(Vec::new());
                value.push(number);
            }
            '0' => {
                let value = number_map.entry('0').or_insert(Vec::new());
                value.push(number);
            }
            _ => {}
        };
    }

    if number_map.get(&'1').unwrap().len() >= number_map.get(&'0').unwrap().len() {
        calc_oxygen_generator_rate(number_map.get(&'1').unwrap().to_vec(), index + 1)
    } else {
        calc_oxygen_generator_rate(number_map.get(&'0').unwrap().to_vec(), index + 1)
    }
}

fn calc_co_scrub_rate(numbers: Vec<&str>, index: usize) -> String {
    if numbers.len() == 1 {
        return String::from_str(numbers[0]).unwrap();
    };

    let mut number_map = HashMap::new();

    for number in numbers {
        match number.chars().nth(index).unwrap() {
            '1' => {
                let value = number_map.entry('1').or_insert(Vec::new());
                value.push(number);
            }
            '0' => {
                let value = number_map.entry('0').or_insert(Vec::new());
                value.push(number);
            }
            _ => {}
        };
    }

    if number_map.get(&'1').unwrap().len() >= number_map.get(&'0').unwrap().len() {
        calc_co_scrub_rate(number_map.get(&'0').unwrap().to_vec(), index + 1)
    } else {
        calc_co_scrub_rate(number_map.get(&'1').unwrap().to_vec(), index + 1)
    }
}

fn convert_bin_str(input: &String) -> i32 {
    i32::from_str_radix(input, 2).unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_gamma() {
        let test_str =
            "00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010";
        let (actual_gamma, actual_epsilon) = calculate_gamma_rate(test_str.lines());
        assert_eq!(22, convert_bin_str(&actual_gamma));
        assert_eq!(9, convert_bin_str(&actual_epsilon));
    }

    #[test]
    fn test_oxy() {
        let test_str =
            "00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010";
        let oxy_answer = calc_oxygen_generator_rate(test_str.lines().collect(), 0);
        let co_answer = calc_co_scrub_rate(test_str.lines().collect(), 0);
        assert_eq!(23, convert_bin_str(&oxy_answer));
        assert_eq!(10, convert_bin_str(&co_answer));
    }
}
