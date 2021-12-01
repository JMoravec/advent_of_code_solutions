pub struct Depth {
    two_previous: i32,
    previous: i32,
    current: i32,
    increases: i32,
    sliding_window_increases: i32,
}

impl Depth {
    pub fn new(starting_num: i32) -> Depth {
        Depth{current: starting_num, increases: 0, two_previous: -1, previous: -1, sliding_window_increases: 0}
    }

    pub fn next_num(&mut self, next_num: i32) {
        if self.current < next_num {
            self.increases += 1;
        };

        if self.two_previous != -1 && self.previous != -1 {
            if self.get_sliding_total() < (self.previous + self.current + next_num) {
                self.sliding_window_increases += 1;
            }
        }

        self.two_previous = self.previous;
        self.previous = self.current;
        self.current = next_num;
    }

    pub fn get_increases(&self) -> i32 {
        self.increases
    }

    pub fn get_sliding_window_increases(&self) -> i32 {
        self.sliding_window_increases
    }

    fn get_sliding_total(&self) -> i32 {
        self.two_previous + self.previous + self.current
    }
    
    pub fn calculate_total_increases(&mut self, depths: Vec<i32>) {
        for depth in depths {
            self.next_num(depth);
        };
    }
}