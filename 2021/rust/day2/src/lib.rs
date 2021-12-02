pub struct Position {
    horizontal: i32,
    depth: i32,
    aim: i32,
    horizontal_part2: i32,
    depth_part2: i32,
}

#[derive(PartialEq, Eq, Debug)]
pub enum Direction {
    UP,
    DOWN,
    FORWARD,
}

impl Direction {
    pub fn from_str(direction: &str) -> Option<Direction> {
        let lowercase = direction.to_lowercase();
        if lowercase == "up" {
            Some(Direction::UP)
        } else if lowercase == "down" {
            Some(Direction::DOWN)
        } else if lowercase == "forward" {
            Some(Direction::FORWARD)
        } else {
            None
        }
    }
}

impl Position {
    pub fn new() -> Position {
        Position {
            horizontal: 0,
            depth: 0,
            aim: 0,
            horizontal_part2: 0,
            depth_part2: 0,
        }
    }

    pub fn move_sub(&mut self, direction: Direction, amount: i32) {
        match direction {
            Direction::UP => {
                self.depth -= amount;
                self.aim -= amount
            }
            Direction::DOWN => {
                self.depth += amount;
                self.aim += amount
            }
            Direction::FORWARD => {
                self.horizontal += amount;
                self.horizontal_part2 += amount;
                self.depth_part2 += self.aim * amount
            }
        }
    }

    pub fn get_final_mult(&self) -> i32 {
        self.depth * self.horizontal
    }

    pub fn get_final_mult_part2(&self) -> i32 {
        self.depth_part2 * self.horizontal_part2
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use test_case::test_case;

    #[test_case("up", Direction::UP ; "Test up lower")]
    #[test_case("uP", Direction::UP ; "Test up mixed")]
    #[test_case("UP", Direction::UP ; "Test up upper")]
    #[test_case("DOWN", Direction::DOWN ; "Test down upper")]
    #[test_case("DoWn", Direction::DOWN ; "Test down mixed")]
    #[test_case("down", Direction::DOWN ; "Test down lower")]
    #[test_case("forward", Direction::FORWARD ; "Test forward lower")]
    #[test_case("fOrWaRd", Direction::FORWARD ; "Test forward mixed")]
    #[test_case("FORWARD", Direction::FORWARD ; "Test forward upper")]
    fn test_direction_enum(input_str: &str, expected: Direction) {
        assert_eq!(expected, Direction::from_str(input_str).unwrap());
    }

    #[test]
    fn test_direction() {
        let mut submarine = Position::new();
        submarine.move_sub(Direction::DOWN, 10);
        assert_eq!(10, submarine.depth);
        assert_eq!(0, submarine.horizontal);
        submarine.move_sub(Direction::UP, 4);
        assert_eq!(6, submarine.depth);
        assert_eq!(0, submarine.horizontal);
        submarine.move_sub(Direction::FORWARD, 100);
        assert_eq!(6, submarine.depth);
        assert_eq!(100, submarine.horizontal);
    }

    #[test]
    fn test_example() {
        let mut submarine = Position::new();
        submarine.move_sub(Direction::FORWARD, 5);
        submarine.move_sub(Direction::DOWN, 5);
        submarine.move_sub(Direction::FORWARD, 8);
        submarine.move_sub(Direction::UP, 3);
        submarine.move_sub(Direction::DOWN, 8);
        submarine.move_sub(Direction::FORWARD, 2);
        assert_eq!(150, submarine.get_final_mult());
        assert_eq!(900, submarine.get_final_mult_part2());
    }
}
