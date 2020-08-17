package main

import (
	"fmt"
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestgetAsteroidParsing(t *testing.T) {
	var tests = []struct {
		input    []string
		expected []Asteroid
	}{
		{[]string{".#..#", ".....", "#####", "....#", "...##"},
			[]Asteroid{{1, 0}, {4, 0}, {0, 2}, {1, 2}, {2, 2}, {3, 2}, {4, 2}, {4, 3}, {3, 4}, {4, 4}}},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%s,%v", test.input, test.expected)
		t.Run(testname, func(t *testing.T) {
			actualLocations := getAsteroids(test.input)
			assert.Equal(t, len(test.expected), len(actualLocations))
			for pos, value := range actualLocations {
				assert.Equal(t, test.expected[pos], value)
			}
		})
	}
}

func TestAsteroidVision(t *testing.T) {
	var tests = []struct {
		input    Asteroid
		expected int
	}{
		{Asteroid{1, 0}, 7},
		{Asteroid{4, 0}, 7},
		{Asteroid{0, 2}, 6},
		{Asteroid{1, 2}, 7},
		{Asteroid{2, 2}, 7},
		{Asteroid{3, 2}, 7},
		{Asteroid{4, 2}, 5},
		{Asteroid{4, 3}, 7},
		{Asteroid{3, 4}, 8},
		{Asteroid{4, 4}, 7},
	}
	allAsteroids := []Asteroid{{1, 0}, {4, 0}, {0, 2}, {1, 2}, {2, 2}, {3, 2}, {4, 2}, {4, 3}, {3, 4}, {4, 4}}
	for _, test := range tests {
		testname := fmt.Sprintf("%v,%d", test.input, test.expected)
		t.Run(testname, func(t *testing.T) {
			actualVision := getAsteroidVision(test.input, allAsteroids)
			assert.Equal(t, test.expected, actualVision)
		})
	}
}

func TestGetStation(t *testing.T) {
	var tests = []struct {
		input             string
		expectedAsteroid  Asteroid
		numberOfAsteroids int
	}{
		{".#..#\n.....\n#####\n....#\n...##", Asteroid{3, 4}, 8},
		{"......#.#.\n#..#.#....\n..#######.\n.#.#.###..\n.#..#.....\n..#....#.#\n#..#....#.\n.##.#..###\n##...#..#.\n.#....####", Asteroid{5, 8}, 33},
		{"#.#...#.#.\n.###....#.\n.#....#...\n##.#.#.#.#\n....#.#.#.\n.##..###.#\n..#...##..\n..##....##\n......#...\n.####.###.", Asteroid{1, 2}, 35},
		{".#..#..###\n####.###.#\n....###.#.\n..###.##.#\n##.##.#.#.\n....###..#\n..#.#..#.#\n#..#.#.###\n.##...##.#\n.....#.#..", Asteroid{6, 3}, 41},
		{".#..##.###...#######\n##.############..##.\n.#.######.########.#\n.###.#######.####.#.\n#####.##.#.##.###.##\n..#####..#.#########\n####################\n#.####....###.#.#.##\n##.#################\n#####.##.###..####..\n..######..##.#######\n####.##.####...##..#\n.#####..#.######.###\n##...#.##########...\n#.##########.#######\n.####.#.###.###.#.##\n....##.##.###..#####\n.#.#.###########.###\n#.#.#.#####.####.###\n###.##.####.##.#..##", Asteroid{11, 13}, 210},
	}
	for _, test := range tests {
		testname := fmt.Sprintf("%s,%v", test.input, test.expectedAsteroid)
		t.Run(testname, func(t *testing.T) {
			locations := getAsteroids(strings.Split(test.input, "\n"))
			actualStation, actualNumAsteroids := getStation(locations)
			assert.Equal(t, test.expectedAsteroid, actualStation)
			assert.Equal(t, test.numberOfAsteroids, actualNumAsteroids)
		})
	}
}
