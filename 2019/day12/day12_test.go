package main

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestApplyGravity(t *testing.T) {
	var tests = []struct {
		moon1         Moon
		moon2         Moon
		expectedMoon1 Moon
		expectedMoon2 Moon
	}{
		{Moon{0, 0, 0, 0, 0, 0}, Moon{1, 1, 1, 0, 0, 0}, Moon{0, 0, 0, 1, 1, 1}, Moon{1, 1, 1, -1, -1, -1}},
		{Moon{0, 0, 0, 0, 0, 0}, Moon{-1, -1, -1, 0, 0, 0}, Moon{0, 0, 0, -1, -1, -1}, Moon{-1, -1, -1, 1, 1, 1}},
		{Moon{0, 0, 0, 0, 0, 0}, Moon{0, 0, 0, 0, 0, 0}, Moon{0, 0, 0, 0, 0, 0}, Moon{0, 0, 0, 0, 0, 0}},
		{Moon{0, 0, 0, 1, 1, 1}, Moon{1, 1, 1, -1, -1, -1}, Moon{0, 0, 0, 2, 2, 2}, Moon{1, 1, 1, -2, -2, -2}},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v,%v,%v,%v", test.moon1, test.moon2, test.expectedMoon1, test.expectedMoon2)
		t.Run(testname, func(t *testing.T) {
			test.moon1.applyGravity(&test.moon2)
			assert.Equal(t, test.expectedMoon1, test.moon1)
			assert.Equal(t, test.expectedMoon2, test.moon2)
		})
	}
}

func TestMoonParsing(t *testing.T) {
	var tests = []struct {
		input    string
		expected Moon
	}{
		{"<x=-1, y=0, z=2>", Moon{-1, 0, 2, 0, 0, 0}},
		{"<x=2, y=-10, z=-7>", Moon{2, -10, -7, 0, 0, 0}},
		{"<x=4, y=-8, z=8>", Moon{4, -8, 8, 0, 0, 0}},
		{"<x=3, y=5, z=-1>", Moon{3, 5, -1, 0, 0, 0}},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%s,%v", test.input, test.expected)
		t.Run(testname, func(t *testing.T) {
			actualMoon := textToMoon(test.input)
			assert.Equal(t, test.expected, actualMoon)
		})
	}
}

func TestMoonSimulation(t *testing.T) {
	var tests = []struct {
		numberOfSteps int
		expectedMoons []Moon
	}{
		{0, []Moon{Moon{-1, 0, 2, 0, 0, 0}, Moon{2, -10, -7, 0, 0, 0}, Moon{4, -8, 8, 0, 0, 0}, Moon{3, 5, -1, 0, 0, 0}}},
		{1, []Moon{Moon{2, -1, 1, 3, -1, -1}, Moon{3, -7, -4, 1, 3, 3}, Moon{1, -7, 5, -3, 1, -3}, Moon{2, 2, 0, -1, -3, 1}}},
		{2, []Moon{Moon{5, -3, -1, 3, -2, -2}, Moon{1, -2, 2, -2, 5, 6}, Moon{1, -4, -1, 0, 3, -6}, Moon{1, -4, 2, -1, -6, 2}}},
		{3, []Moon{Moon{5, -6, -1, 0, -3, 0}, Moon{0, 0, 6, -1, 2, 4}, Moon{2, 1, -5, 1, 5, -4}, Moon{1, -8, 2, 0, -4, 0}}},
		{4, []Moon{Moon{2, -8, 0, -3, -2, 1}, Moon{2, 1, 7, 2, 1, 1}, Moon{2, 3, -6, 0, 2, -1}, Moon{2, -9, 1, 1, -1, -1}}},
		{5, []Moon{Moon{-1, -9, 2, -3, -1, 2}, Moon{4, 1, 5, 2, 0, -2}, Moon{2, 2, -4, 0, -1, 2}, Moon{3, -7, -1, 1, 2, -2}}},
		{6, []Moon{Moon{-1, -7, 3, 0, 2, 1}, Moon{3, 0, 0, -1, -1, -5}, Moon{3, -2, 1, 1, -4, 5}, Moon{3, -4, -2, 0, 3, -1}}},
		{7, []Moon{Moon{2, -2, 1, 3, 5, -2}, Moon{1, -4, -4, -2, -4, -4}, Moon{3, -7, 5, 0, -5, 4}, Moon{2, 0, 0, -1, 4, 2}}},
		{8, []Moon{Moon{5, 2, -2, 3, 4, -3}, Moon{2, -7, -5, 1, -3, -1}, Moon{0, -9, 6, -3, -2, 1}, Moon{1, 1, 3, -1, 1, 3}}},
		{9, []Moon{Moon{5, 3, -4, 0, 1, -2}, Moon{2, -9, -3, 0, -2, 2}, Moon{0, -8, 4, 0, 1, -2}, Moon{1, 1, 5, 0, 0, 2}}},
		{10, []Moon{Moon{2, 1, -3, -3, -2, 1}, Moon{1, -8, 0, -1, 1, 3}, Moon{3, -6, 1, 3, 2, -3}, Moon{2, 0, 4, 1, -1, -1}}},
	}

	for _, test := range tests {
		moonSet := []Moon{Moon{-1, 0, 2, 0, 0, 0}, Moon{2, -10, -7, 0, 0, 0}, Moon{4, -8, 8, 0, 0, 0}, Moon{3, 5, -1, 0, 0, 0}}
		testname := fmt.Sprintf("%d,%d", test.numberOfSteps, test.expectedMoons)
		t.Run(testname, func(t *testing.T) {
			moonSet, _ = runSimulation(moonSet, test.numberOfSteps)
			for i, actualMoon := range moonSet {
				assert.Equal(t, test.expectedMoons[i], actualMoon)
			}
		})
	}
}

func TestTotalEnergy(t *testing.T) {
	var tests = []struct {
		moonSet        []Moon
		numberOfSteps  int
		expectedEnergy int
	}{
		{[]Moon{Moon{-1, 0, 2, 0, 0, 0}, Moon{2, -10, -7, 0, 0, 0}, Moon{4, -8, 8, 0, 0, 0}, Moon{3, 5, -1, 0, 0, 0}}, 10, 179},
		{[]Moon{Moon{-8, -10, 0, 0, 0, 0}, Moon{5, 5, 10, 0, 0, 0}, Moon{2, -7, 3, 0, 0, 0}, Moon{9, -8, -3, 0, 0, 0}}, 100, 1940},
	}
	for _, test := range tests {
		testname := fmt.Sprintf("%v,%d,%d", test.moonSet, test.numberOfSteps, test.expectedEnergy)
		t.Run(testname, func(t *testing.T) {
			_, totalEnergy := runSimulation(test.moonSet, test.numberOfSteps)
			assert.Equal(t, test.expectedEnergy, totalEnergy)

		})
	}
}

func TestRepeatSteps(t *testing.T) {
	var tests = []struct {
		moonSet       []Moon
		expectedSteps int
	}{
		{[]Moon{Moon{-1, 0, 2, 0, 0, 0}, Moon{2, -10, -7, 0, 0, 0}, Moon{4, -8, 8, 0, 0, 0}, Moon{3, 5, -1, 0, 0, 0}}, 2772},
		{[]Moon{Moon{-8, -10, 0, 0, 0, 0}, Moon{5, 5, 10, 0, 0, 0}, Moon{2, -7, 3, 0, 0, 0}, Moon{9, -8, -3, 0, 0, 0}}, 4686774924},
	}
	for _, test := range tests {
		testname := fmt.Sprintf("%v,%d", test.moonSet, test.expectedSteps)
		t.Run(testname, func(t *testing.T) {
			totalSteps := runSimulationUntilRepeat(test.moonSet)
			assert.Equal(t, test.expectedSteps, totalSteps)
		})
	}
}
