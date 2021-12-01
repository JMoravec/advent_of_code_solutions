#[cfg(test)]
mod tests {
    use day1::*;
    use test_case::test_case;

    #[test_case(0, 1 ; "test low num")]
    #[test_case(0, 100 ; "test higher")]
    #[test_case(100, 101 ; "test start higher")]
    #[test_case(-599, 1 ; "test neg start")]
    #[test_case(10000, 20000 ; "test high start")]
    fn test_increase(start: i32, next_num: i32) {
        let mut depth = Depth::new(start);
        depth.next_num(next_num);
        assert_eq!(1, depth.get_increases());
    }

    #[test_case(0, -1 ; "test low num")]
    #[test_case(0, 0 ; "test same")]
    #[test_case(100, 99 ; "test start higher")]
    #[test_case(-599, -600 ; "test neg start")]
    #[test_case(10000, 0 ; "test high start")]
    fn test_decrease(start: i32, next_num: i32) {
        let mut depth = Depth::new(start);
        depth.next_num(next_num);
        assert_eq!(0, depth.get_increases());
    }

    #[test]
    fn test_total_increase() {
        let depths = vec![200, 208,210,200,207,240,269,260,263];
        let expected_answer = 7;
        let mut depth = Depth::new(199);
        depth.calculate_total_increases(depths);
        assert_eq!(expected_answer, depth.get_increases());
    }

    #[test]
    fn test_sliding_window_increases() {
        let depths = vec![200, 208,210,200,207,240,269,260,263];
        let expected_answer = 5;
        let mut depth = Depth::new(199);
        depth.calculate_total_increases(depths);
        assert_eq!(expected_answer, depth.get_sliding_window_increases());
    }
}