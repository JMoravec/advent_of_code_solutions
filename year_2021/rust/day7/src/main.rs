use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").expect("Unable to read file");
    let sorted_list = get_sorted_list(input.as_str());
    let median = get_median(&sorted_list);
    let mean = get_mean(&sorted_list);
    println!("Part 1: {}", get_best_fuel(&sorted_list, median, true));
    println!("Part 2: {}", get_best_fuel(&sorted_list, mean, false));
}

fn get_median(list: &Vec<i32>) -> f64 {
    let len = list.len();
    let mid = len / 2;
    if len % 2 == 0 {
        get_mean(&list[(mid-1)..(mid+1)])
    } else {
        f64::from(list[mid])
    }

}

fn get_mean(list: &[i32]) -> f64 {
    let sum: i32 = Iterator::sum(list.iter());
    f64::from(sum) / (list.len() as f64)
}

fn get_sorted_list(numbers: &str) -> Vec<i32> {
    let mut array: Vec<i32> = numbers.split(',').map(|f| f.parse::<i32>().unwrap()).collect();
    array.sort_unstable();
    array
}

fn get_fuel_spent(steps: i32, linear: bool) -> i32 {
    if linear {
        steps
    } else {
        (steps * (steps + 1)) / 2
    }
}

fn get_total_fuel(list: &Vec<i32>, target: i32, linear_fuel: bool) -> i32 {
    let mut total_fuel = 0;
    for value in list {
        let steps = (*value - target).abs();

        total_fuel += get_fuel_spent(steps, linear_fuel);
    }
    total_fuel
}

fn get_best_fuel(list: &Vec<i32>, target: f64, linear_fuel: bool) -> i32 {
    let target_int = target.trunc() as i32;
    let mut best_fuel = i32::MAX;
    for i in target_int-2..target_int+2 {
        let new_fuel = get_total_fuel(list, i, linear_fuel);
        if new_fuel < best_fuel {
            best_fuel = new_fuel;
        }
    }
    best_fuel
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sample_input() { 
        let input = "16,1,2,0,4,2,7,1,2,14";
        let sorted_list = get_sorted_list(input);
        let median = get_median(&sorted_list);
        let mean = get_mean(&sorted_list);
        assert_eq!(37, get_total_fuel(&sorted_list, 2, true));
        assert_eq!(168, get_total_fuel(&sorted_list, 5, false));
        assert_eq!(37, get_best_fuel(&sorted_list, median, true));
        assert_eq!(168, get_best_fuel(&sorted_list, mean, false));
    }
}