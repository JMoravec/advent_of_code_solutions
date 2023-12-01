use std::collections::VecDeque;
use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").expect("Unable to read file");
    let input_clean = input.split_whitespace().next().unwrap();

    let mut queue = get_queue_from_input(input_clean);
    let fish = get_fish_after_n_days(&mut queue, 80);
    println!("Part 1 answer: {}", fish);

    let mut queue_part2 = get_queue_from_input(input_clean);
    let fish_part2 = get_fish_after_n_days(&mut queue_part2, 256);
    println!("Part 2 answer: {}", fish_part2);
}

struct Lanternfish {
    amount: i64,
}

impl Lanternfish {
    fn new() -> Self {
        Lanternfish { amount: 0 }
    }

    fn new_from_amount(amount: i64) -> Self {
        Lanternfish { amount: amount }
    }

    fn add_fish(&mut self) {
        self.add_multiple_fish(1);
    }

    fn add_multiple_fish(&mut self, amount_to_add: i64) {
        self.amount += amount_to_add;
    }
}

fn new_day(all_fish: &mut VecDeque<Lanternfish>) {
    let parents = all_fish.pop_front().unwrap();
    if let Some(fish) = all_fish.get_mut(6) {
        fish.add_multiple_fish(parents.amount);
    }
    all_fish.push_back(Lanternfish::new_from_amount(parents.amount))
}

fn get_fish_after_n_days(all_fish: &mut VecDeque<Lanternfish>, days: i64) -> i64 {
    for _ in 0..days {
        new_day(all_fish);
    }
    let mut total: i64 = 0;
    for fish in all_fish {
        total += fish.amount;
    }
    total
}

fn get_queue_from_input(input: &str) -> VecDeque<Lanternfish> {
    let mut queue: VecDeque<Lanternfish> = VecDeque::new();
    for _ in 0..9 {
        queue.push_back(Lanternfish::new())
    }

    for num in input.split(',') {
        let num32: usize = num.parse().unwrap();
        if let Some(fish) = queue.get_mut(num32) {
            fish.add_fish();
        }
    }
    queue
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_sample() {
        let input = "3,4,3,1,2";
        let mut queue = get_queue_from_input(input);
        assert_eq!(26, get_fish_after_n_days(&mut queue, 18));
        let mut queue2 = get_queue_from_input(input);
        assert_eq!(5934, get_fish_after_n_days(&mut queue2, 80));
        let mut queue3 = get_queue_from_input(input);
        assert_eq!(26984457539, get_fish_after_n_days(&mut queue3, 256));
    }
}
