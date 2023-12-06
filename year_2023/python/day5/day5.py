"""Solution for day 5 of 2023"""


from dataclasses import dataclass
from typing import Dict, List, NamedTuple, Tuple


class MapRange(NamedTuple):
    """Range tuple helper"""

    source_start: int
    length: int
    dest_source: int = 0

    @property
    def source_end(self) -> int:
        """Ge the source end for a given map"""
        return self.source_start + self.length - 1


@dataclass
class Map:
    """Object representing a map of source to dest"""

    source: str
    destination: str
    mapping: List[MapRange]

    @staticmethod
    def create_from_string(input_str: str) -> "Map":
        """Create an object from initial string"""
        source, dest = input_str.strip().removesuffix(" map:").split("-to-")
        return Map(source, dest, [])

    def add_map_line(self, input_str: str):
        """Add a a mapping line from str to the object"""
        dest, source, length = input_str.strip().split()
        self.mapping.append(MapRange(int(source), int(length), int(dest)))

    def get_value(self, source: int) -> int:
        """Get the value of a specific mapping of source to destination"""
        for map_tuple in self.mapping:
            if map_tuple.source_start <= source < map_tuple.source_end:
                return map_tuple.dest_source + source - map_tuple.source_start
        return source

    def get_ranges(self, ranges: List[MapRange]) -> List[MapRange]:
        """Get the ranges of the destination for a list of ranges"""
        dest_ranges = []
        while ranges:
            current_range = ranges.pop()
            for test_map in self.mapping:
                # not intersecting
                if (
                    current_range.source_end < test_map.source_start
                    or test_map.source_end < current_range.source_start
                ):
                    continue
                # current range is subset of mapping
                if (
                    test_map.source_start <= current_range.source_start
                    and test_map.source_end >= current_range.source_end
                ):
                    diff = current_range.source_start - test_map.source_start
                    dest_ranges.append(
                        MapRange(test_map.dest_source + diff, current_range.length)
                    )
                    break
                # end of current range is in mapping
                if (
                    current_range.source_start < test_map.source_start
                    and current_range.source_end >= test_map.source_start
                    and current_range.source_end <= test_map.source_end
                ):
                    # add outside range back to queue
                    ranges.append(
                        MapRange(
                            current_range.source_start,
                            test_map.source_start - current_range.source_start,
                        )
                    )
                    # add intersection to dest ranges
                    dest_ranges.append(
                        MapRange(
                            test_map.dest_source,
                            current_range.source_end - test_map.source_start,
                        )
                    )
                    break
                # start of current range is in mapping
                if (
                    current_range.source_start > test_map.source_start
                    and current_range.source_start <= test_map.source_end
                    and current_range.source_end > test_map.source_end
                ):
                    ranges.append(
                        MapRange(
                            test_map.source_end + 1,
                            current_range.source_end - test_map.source_end,
                        )
                    )
                    diff = current_range.source_start - test_map.source_start
                    dest_ranges.append(
                        MapRange(
                            test_map.dest_source + diff,
                            test_map.source_end - current_range.source_start,
                        )
                    )
                    break
                # map is subset of current range
                if (
                    current_range.source_start < test_map.source_start
                    and current_range.source_end > test_map.source_end
                ):
                    ranges.append(
                        MapRange(
                            current_range.source_start,
                            test_map.source_start - current_range.source_start,
                        )
                    )
                    ranges.append(
                        MapRange(
                            test_map.source_end + 1,
                            current_range.source_end - test_map.source_end + 1,
                        )
                    )
                    dest_ranges.append(MapRange(test_map.dest_source, test_map.length))
                    break
            else:
                dest_ranges.append(current_range)

        return dest_ranges


def process_input(input_str: str) -> Tuple[List[int], Dict[str, Map]]:
    """Process the whole input"""
    all_lines = input_str.splitlines()
    seed_line = all_lines[0].strip().split("seeds: ")[1].split()
    seeds = [int(x.strip()) for x in seed_line]
    mapping_lines = all_lines[2:]

    mappings = {}
    is_new_map = True
    current_map = None
    for mapping_line in mapping_lines:
        if is_new_map:
            new_map = Map.create_from_string(mapping_line)
            is_new_map = False
            mappings[new_map.source] = new_map
            current_map = new_map
        elif not mapping_line.strip():
            is_new_map = True
            current_map = None
        else:
            if current_map:
                current_map.add_map_line(mapping_line)
            else:
                raise ValueError
    return seeds, mappings


def get_location_num(seed: int, mappings: Dict[str, Map]) -> int:
    """Get the location num for a given seed"""
    current_stage = "seed"
    current_value = seed
    while current_stage != "location":
        current_map = mappings[current_stage]
        current_value = current_map.get_value(current_value)
        current_stage = current_map.destination

    return current_value


def get_location_ranges(
    seeds: List[MapRange], mappings: Dict[str, Map]
) -> List[MapRange]:
    """Get all the location ranges for a list of seed ranges"""
    current_stage = "seed"
    current_values = seeds
    while current_stage != "location":
        current_map = mappings[current_stage]
        current_values = current_map.get_ranges(current_values)
        current_stage = current_map.destination
    return current_values


def get_lowest_location(seeds: List[int], mappings: Dict[str, Map]) -> int:
    """Get the lowest location value for a list of seeds"""
    min_location = 99999999999999999
    for seed in seeds:
        min_location = min(get_location_num(seed, mappings), min_location)
    # return min(get_location_num(seed, mappings) for seed in seeds)
    return min_location


def solve_part_1(input_str: str) -> int:
    """Solve part 1 of day 5"""
    return get_lowest_location(*process_input(input_str))


def solve_part_2(input_str: str) -> int:
    """Solve part 2 of day 5"""
    seeds, mapping = process_input(input_str)
    all_seeds = []
    for i in range(0, len(seeds), 2):
        all_seeds.append(MapRange(seeds[i], seeds[i + 1]))

    location_ranges = get_location_ranges(all_seeds, mapping)
    return min(x.source_start for x in location_ranges)


if __name__ == "__main__":
    with open("year_2023/inputs/day5_input.txt", encoding="utf-8") as file:
        input_file = file.read()
    print(f"Day 5 part 1: {solve_part_1(input_file)}")
    print(f"Day 5 part 2: {solve_part_2(input_file)}")
