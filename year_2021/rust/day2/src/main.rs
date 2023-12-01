//use std::env;
use day2::{Direction, Position};
use std::fs;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let lines = data.split("\n");
    let mut postition = Position::new();

    for line in lines {
        let (direction, amount) = line.split_once(" ").unwrap();
        postition.move_sub(
            Direction::from_str(direction).unwrap(),
            amount.parse().unwrap(),
        );
    }

    println!("Part 1 answer: {}", postition.get_final_mult());
    println!("Part 2 answer: {}", postition.get_final_mult_part2());
}
