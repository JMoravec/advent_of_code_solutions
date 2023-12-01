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

func TestShootAsteroids(t *testing.T) {
	var tests = []struct {
		shotNumber       int
		expectedAsteroid Asteroid
	}{
		{0, Asteroid{11, 12}},
		{1, Asteroid{12, 1}},
		{2, Asteroid{12, 2}},
		{9, Asteroid{12, 8}},
		{19, Asteroid{16, 0}},
		{49, Asteroid{16, 9}},
		{99, Asteroid{10, 16}},
		{199, Asteroid{8, 2}},
		{200, Asteroid{10, 9}},
		{298, Asteroid{11, 1}},
	}
	asteroidInput := ".#..##.###...#######\n##.############..##.\n.#.######.########.#\n.###.#######.####.#.\n#####.##.#.##.###.##\n..#####..#.#########\n####################\n#.####....###.#.#.##\n##.#################\n#####.##.###..####..\n..######..##.#######\n####.##.####...##..#\n.#####..#.######.###\n##...#.##########...\n#.##########.#######\n.####.#.###.###.#.##\n....##.##.###..#####\n.#.#.###########.###\n#.#.#.#####.####.###\n###.##.####.##.#..##"
	locations := getAsteroids(strings.Split(asteroidInput, "\n"))
	station := Asteroid{11, 13}
	shotAsteroids := shootAsteroids(locations, station)
	for _, test := range tests {
		assert.Equal(t, 299, len(shotAsteroids))
		testname := fmt.Sprintf("%d,%v", test.shotNumber, test.expectedAsteroid)
		t.Run(testname, func(t *testing.T) {
			assert.Equal(t, test.expectedAsteroid, shotAsteroids[test.shotNumber])
		})
	}
}
