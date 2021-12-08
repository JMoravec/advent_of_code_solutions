use std::collections::HashMap;
use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").expect("Unable to read file");
    let mut map: HashMap<Point, i32> = HashMap::new();
    let mut map_part2: HashMap<Point, i32> = HashMap::new();

    for line in input.lines() {
        let vent = Vent::from_str(line);
        add_points_to_map(&mut map, &vent.create_lines(false));
        add_points_to_map(&mut map_part2, &vent.create_lines(true));
    }
    let mut total = 0;
    for value in map.values() {
        if *value > 1 {
            total += 1;
        }
    }
    println!("Part 1: {}", total);

    let mut total_part2 = 0;
    for value in map_part2.values() {
        if *value > 1 {
            total_part2 += 1;
        }
    }
    println!("Part 2: {}", total_part2);
}

#[derive(PartialEq, Eq, Debug)]
struct Vent {
    x1: i32,
    x2: i32,
    y1: i32,
    y2: i32,
}

#[derive(PartialEq, Eq, Hash, Clone, Copy)]
struct Point {
    x: i32,
    y: i32,
}

impl Point {
    fn new(x: i32, y: i32) -> Self {
        Point { x: x, y: y }
    }
}

fn convert_str_point(input: &str) -> (i32, i32) {
    let (first, second) = input.split_once(',').unwrap();

    (first.parse().unwrap(), second.parse().unwrap())
}

fn add_points_to_map(map: &mut HashMap<Point, i32>, points_to_add: &Vec<Point>) {
    for point in points_to_add {
        let amount = map.entry(*point).or_insert(0);
        *amount += 1;
    }
}

impl Vent {
    fn from_str(input: &str) -> Self {
        let (beginning, end) = input.split_once(" -> ").unwrap();
        let first = convert_str_point(beginning);
        let second = convert_str_point(end);

        Vent {
            x1: first.0,
            y1: first.1,
            x2: second.0,
            y2: second.1,
        }
    }

    fn create_lines(&self, use_diag: bool) -> Vec<Point> {
        let mut points: Vec<Point> = Vec::new();
        if self.x1 == self.x2 {
            let (start, end) = if self.y1 > self.y2 {
                (self.y2, self.y1)
            } else {
                (self.y1, self.y2)
            };
            for i in start..(end + 1) {
                points.push(Point::new(self.x1, i));
            }
        } else if self.y1 == self.y2 {
            let (start, end) = if self.x1 > self.x2 {
                (self.x2, self.x1)
            } else {
                (self.x1, self.x2)
            };
            for i in start..(end + 1) {
                points.push(Point::new(i, self.y1));
            }
        } else if use_diag {
            let length = (self.x2 - self.x1).abs() + 1;
            let x_direction = if self.x2 > self.x1 { 1 } else { -1 };
            let y_direction = if self.y2 > self.y1 { 1 } else { -1 };
            for i in 0..length {
                points.push(Point::new(
                    self.x1 + (i * x_direction),
                    self.y1 + (i * y_direction),
                ));
            }
        }
        points
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        let input = "0,9 -> 5,9\n8,0 -> 0,8\n9,4 -> 3,4\n2,2 -> 2,1\n7,0 -> 7,4\n6,4 -> 2,0\n0,9 -> 2,9\n3,4 -> 1,4\n0,0 -> 8,8\n5,5 -> 8,2";
        let mut map: HashMap<Point, i32> = HashMap::new();
        let mut map_diags: HashMap<Point, i32> = HashMap::new();

        for line in input.lines() {
            let vent = Vent::from_str(line);
            add_points_to_map(&mut map, &vent.create_lines(false));
            add_points_to_map(&mut map_diags, &vent.create_lines(true));
        }
        let mut total = 0;
        for value in map.values() {
            if *value > 1 {
                total += 1;
            }
        }
        assert_eq!(5, total);

        let mut diag_total = 0;
        for value in map_diags.values() {
            if *value > 1 {
                diag_total += 1;
            }
        }
        assert_eq!(12, diag_total);
    }

    #[test]
    fn test_vent_creation() {
        assert_eq!(
            Vent {
                x1: 0,
                y1: 9,
                x2: 5,
                y2: 9
            },
            Vent::from_str("0,9 -> 5,9")
        );
        assert_eq!(
            Vent {
                x1: 8,
                y1: 0,
                x2: 0,
                y2: 8
            },
            Vent::from_str("8,0 -> 0,8")
        );
        assert_eq!(
            Vent {
                x1: 9,
                y1: 4,
                x2: 3,
                y2: 4
            },
            Vent::from_str("9,4 -> 3,4")
        );
        assert_eq!(
            Vent {
                x1: 2,
                y1: 2,
                x2: 2,
                y2: 1
            },
            Vent::from_str("2,2 -> 2,1")
        );
        assert_eq!(
            Vent {
                x1: 7,
                y1: 0,
                x2: 7,
                y2: 4
            },
            Vent::from_str("7,0 -> 7,4")
        );
        assert_eq!(
            Vent {
                x1: 6,
                y1: 4,
                x2: 2,
                y2: 0
            },
            Vent::from_str("6,4 -> 2,0")
        );
        assert_eq!(
            Vent {
                x1: 0,
                y1: 9,
                x2: 2,
                y2: 9
            },
            Vent::from_str("0,9 -> 2,9")
        );
        assert_eq!(
            Vent {
                x1: 3,
                y1: 4,
                x2: 1,
                y2: 4
            },
            Vent::from_str("3,4 -> 1,4")
        );
        assert_eq!(
            Vent {
                x1: 0,
                y1: 0,
                x2: 8,
                y2: 8
            },
            Vent::from_str("0,0 -> 8,8")
        );
        assert_eq!(
            Vent {
                x1: 5,
                y1: 5,
                x2: 8,
                y2: 2
            },
            Vent::from_str("5,5 -> 8,2")
        );
    }
}
