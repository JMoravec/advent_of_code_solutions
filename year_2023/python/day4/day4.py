"""Solution for day 4 of 2023"""
from typing import List


def get_points_for_card(input_str: str, double_points: bool = True) -> int:
    """Get the points for a single card"""
    no_card_num = input_str.strip().split(":")[1]
    winning_nums, pulled_nums = no_card_num.strip().split("|")

    total_wins = get_wins_for_card(winning_nums, pulled_nums)

    if not double_points:
        return total_wins

    if total_wins > 0:
        return 2 ** (total_wins - 1)
    return 0


def get_wins_for_card(winning_nums: str, pulled_nums: str) -> int:
    """Get the amount of wins for a given card"""
    winning_nums_set = set(x for x in winning_nums.split())
    total_wins = 0
    for num in pulled_nums.split():
        if num in winning_nums_set:
            total_wins += 1
    return total_wins


def sum_of_all_points(test_input: str) -> int:
    """Get the sum of all the points of cards"""
    return sum(get_points_for_card(input_str) for input_str in test_input.splitlines())


def get_card_counts(test_input: str) -> int:
    """get the total card count"""
    all_cards = get_winning_stats(test_input)
    card_counts = [1] * len(all_cards)
    for card, wins in enumerate(all_cards):
        for i in range(card + 1, card + 1 + wins):
            card_counts[i] += card_counts[card]

    return sum(card_counts)


def get_winning_stats(test_input: str) -> List[int]:
    """Get the amount of wining numbers for each card"""
    all_lines = test_input.splitlines()
    all_cards = [0] * len(all_lines)
    for i, card in enumerate(all_lines):
        nums = card.strip().split(":")[1]
        winning_nums, pulled_nums = nums.strip().split("|")
        total_wins = get_wins_for_card(winning_nums, pulled_nums)
        all_cards[i] = total_wins

    return all_cards


if __name__ == "__main__":
    with open("year_2023/inputs/day4_input.txt", encoding="utf-8") as file:
        test_file = file.read()
    print(f"Day 4 part 1: {sum_of_all_points(test_file)}")
    print(f"Day 4 part 2: {get_card_counts(test_file)}")
