use std::fs;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");

    let mut data_lines = data.lines();

    let callouts: Vec<&str>= data_lines.next().unwrap().split(',').collect();
    let mut boards: Vec<BingoBoard> = Vec::new();

    for line in data_lines {
        let mut new_board = BingoBoard::new();

        for i in 0..5 {
            let next_line: Vec<i32> = data_lines.next().unwrap().split(' ').map(|x| x.parse().unwrap()).collect();
            let mut next_line_array: [i32; 5] = Default::default();
            for j in 0..5 {
                next_line_array[j] = *next_line.get(j).unwrap();
            }
            new_board.insert_row(next_line_array, i);
        }

        boards.push(new_board);
    }
}

struct BingoBoard {
    board: Vec<Vec<i32>>,
    length_totals: [i32; 5],
    vertical_totals: [i32; 5],
    diagnal_totals: [i32; 2],
}

impl BingoBoard {
    fn new() -> Self {
        BingoBoard{board: vec![vec![0; 5]], length_totals: [0; 5], vertical_totals: [0; 5], diagnal_totals: [0; 2]}
    }

    fn insert_row(&mut self, row: [i32; 5], vert_index: usize) {
        self.board.insert(vert_index, row.to_vec());
        let mut total = 0;
        for number in row {
            total += number;
        }
        self.length_totals[vert_index] = total;
    }

    fn update_totals(&mut self) {
        let mut vert_total = 0;
        let mut diag_total_1 = 0;
        let mut diag_total_2 = 0;
        for i in 0..5 {
            for row in &self.board {
                vert_total += row.get(i).unwrap();
            }
            self.vertical_totals[i] = vert_total;

            diag_total_1 += self.board.get(i).unwrap().get(i).unwrap();
            diag_total_2 += self.board.get(i).unwrap().get(4-i).unwrap();
        }
        self.diagnal_totals[0] = diag_total_1;
        self.diagnal_totals[1] = diag_total_2;
    }

    fn get_current_total(&self) -> i32 {
        let mut total = 0 ;
        for value in self.length_totals {
            total += value;
        };
        total
    }

    fn mark_number(&mut self, number: i32) -> bool {
        for i in 0..5 {
            let row = self.board.get(i).unwrap();
            for j in 0..5 {
                if *row.get(j).unwrap() == number {
                    let mut complete = false;
                    if let Some(total) = self.length_totals.get_mut(i) {
                        *total -= number;
                        if *total == 0 {
                            complete = true;
                        }
                    }

                    if let Some(total) = self.vertical_totals.get_mut(j) {
                        *total -= number;
                        if *total == 0 {
                            complete = true;
                        }
                    }

                    if i == j {
                        if let Some(total) = self.diagnal_totals.get_mut(0) {
                            *total -= number;
                            if *total == 0 {
                                complete = true;
                            }
                        }
                    }

                    if i + j == 5 {
                        if let Some(total) = self.diagnal_totals.get_mut(1) {
                            *total -= number;
                            if *total == 0 {
                                complete = true;
                            }
                        }
                    }

                    if complete {
                        return true;
                    }
                }
            }
        };
        false
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve_board() {
        let mut board = BingoBoard::new();
        board.insert_row([14,21,17,24,4], 0);
        board.insert_row([10,16,15,9,19], 1);
        board.insert_row([18,8,23,26,20], 2);
        board.insert_row([22,11,13,6,5], 3);
        board.insert_row([2,0,12,3,7], 4);
        board.update_totals();

        assert_eq!(false, board.mark_number(7));
        assert_eq!(false, board.mark_number(4));
        assert_eq!(false, board.mark_number(9));
        assert_eq!(false, board.mark_number(5));
        assert_eq!(false, board.mark_number(11));

        assert_eq!(false, board.mark_number(17));
        assert_eq!(false, board.mark_number(23));
        assert_eq!(false, board.mark_number(2));
        assert_eq!(false, board.mark_number(0));
        assert_eq!(false, board.mark_number(14));
        assert_eq!(false, board.mark_number(21));

        assert_eq!(true, board.mark_number(24));

        assert_eq!(188, board.get_current_total());
    }
}
