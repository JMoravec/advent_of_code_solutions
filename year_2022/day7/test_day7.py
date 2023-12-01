"""Tests for day 7"""
from year_2022.day7.day7 import (
    FileType,
    TreeNode,
    parse_commands,
    get_total_size_dir_under_amount,
    flatten_sizes,
    get_smallest_deletable_dir,
)

TEST_COMMANDS = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]


def test_get_total_size():
    """Test that getting the size for various known totals works as expected"""
    top_level = TreeNode("/", FileType.DIRECTORY)
    top_level = parse_commands(TEST_COMMANDS, top_level)
    assert top_level.get_size() == 48381165
    assert top_level.children["a"].children["e"].get_size() == 584
    assert top_level.children["a"].get_size() == 94853
    assert top_level.children["d"].get_size() == 24933642


def test_get_sum():
    """Test getting the total size under an amount"""
    top_level = TreeNode("/", FileType.DIRECTORY)
    top_level = parse_commands(TEST_COMMANDS, top_level)
    assert get_total_size_dir_under_amount(top_level, 100000) == 95437


def test_get_directories_under():
    """Test getting the total size under an amount"""
    top_level = TreeNode("/", FileType.DIRECTORY)
    top_level = parse_commands(TEST_COMMANDS, top_level)
    assert flatten_sizes(top_level) == [584, 94853, 24933642, 48381165]


def test_get_smallest_size_to_delete():
    """Test getting the total size under an amount"""
    top_level = TreeNode("/", FileType.DIRECTORY)
    top_level = parse_commands(TEST_COMMANDS, top_level)
    assert get_smallest_deletable_dir(top_level) == 24933642
