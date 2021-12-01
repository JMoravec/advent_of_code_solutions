use std::env;
use std::fs;
use day1::*;

fn main() {
    let args: Vec<String>  = env::args().collect();
    let filename = &args[1];

    let data = fs::read_to_string(filename).expect("Unable to read file");
    let mut lines = data.split("\n");

    let mut depth = Depth::new(lines.next().unwrap().parse::<i32>().unwrap());
    let mut depths: Vec<i32> = Vec::new();

    for line in lines {
        println!("{}", line);
        let new_depth = match line.parse::<i32>() {
            Ok(value) => value,
            _ => break,
        };
        depths.push(new_depth);
    };
    depth.calculate_total_increases(depths);
    println!("Part 1 answer: {}", depth.get_increases());
    println!("Part 2 answer: {}", depth.get_sliding_window_increases());
}
