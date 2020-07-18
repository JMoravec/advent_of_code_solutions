package main

import (
	"fmt"
	"strconv"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIntcodeProgram(t *testing.T) {
	var tests = []struct {
		program  []int
		expected []int
	}{
		{[]int{1, 0, 0, 0, 99}, []int{2, 0, 0, 0, 99}},
		{[]int{2, 3, 0, 3, 99}, []int{2, 3, 0, 6, 99}},
		{[]int{2, 4, 4, 5, 99, 0}, []int{2, 4, 4, 5, 99, 9801}},
		{[]int{1, 1, 1, 4, 99, 5, 6, 0, 99}, []int{30, 1, 1, 4, 2, 5, 6, 0, 99}},
		{[]int{1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50}, []int{3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50}},
		{[]int{3, 0, 4, 0, 99}, []int{123, 0, 4, 0, 99}},
		{[]int{1002, 4, 3, 4, 33}, []int{1002, 4, 3, 4, 99}},
		{[]int{1101, 100, -1, 4, 0}, []int{1101, 100, -1, 4, 99}},
	}

	testInputFunc := func() int {
		return 123
	}

	testOutputFunc := func(value int) {
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%d,%d", test.program, test.expected)
		test.expected = append(test.expected, make([]int, 10000)...)
		t.Run(testname, func(t *testing.T) {
			endResult := runProgram(test.program, testInputFunc, testOutputFunc)
			assert.Equal(t, len(test.expected), len(endResult), "Lengths of the arrays should be equal")
			for i, actualValue := range endResult {
				assert.Equal(t, test.expected[i], actualValue, "Incorrect value")
			}
		})
	}
}

func TestIntcodeProgramInputOutput(t *testing.T) {
	var tests = []struct {
		program  []int
		input    int
		expected int
	}{
		{[]int{3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8}, 8, 1},
		{[]int{3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8}, 7, 0},
		{[]int{3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8}, 9, 0},
		{[]int{3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8}, 0, 0},
		{[]int{3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8}, -999, 0},
		{[]int{3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8}, 999, 0},
		{[]int{3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8}, 8, 0},
		{[]int{3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8}, 7, 1},
		{[]int{3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8}, 9, 0},
		{[]int{3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8}, 0, 1},
		{[]int{3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8}, -999, 1},
		{[]int{3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8}, 999, 0},
		{[]int{3, 3, 1108, -1, 8, 3, 4, 3, 99}, 8, 1},
		{[]int{3, 3, 1108, -1, 8, 3, 4, 3, 99}, 7, 0},
		{[]int{3, 3, 1108, -1, 8, 3, 4, 3, 99}, 9, 0},
		{[]int{3, 3, 1108, -1, 8, 3, 4, 3, 99}, 0, 0},
		{[]int{3, 3, 1108, -1, 8, 3, 4, 3, 99}, -999, 0},
		{[]int{3, 3, 1108, -1, 8, 3, 4, 3, 99}, 999, 0},
		{[]int{3, 3, 1107, -1, 8, 3, 4, 3, 99}, 8, 0},
		{[]int{3, 3, 1107, -1, 8, 3, 4, 3, 99}, 7, 1},
		{[]int{3, 3, 1107, -1, 8, 3, 4, 3, 99}, 9, 0},
		{[]int{3, 3, 1107, -1, 8, 3, 4, 3, 99}, 0, 1},
		{[]int{3, 3, 1107, -1, 8, 3, 4, 3, 99}, -999, 1},
		{[]int{3, 3, 1107, -1, 8, 3, 4, 3, 99}, 999, 0},
		{[]int{3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9}, 0, 0},
		{[]int{3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9}, 1, 1},
		{[]int{3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9}, -999, 1},
		{[]int{3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9}, 999, 1},
		{[]int{3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1}, 0, 0},
		{[]int{3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1}, 1, 1},
		{[]int{3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1}, -999, 1},
		{[]int{3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1}, 999, 1},
		{[]int{3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99}, 8, 1000},
		{[]int{3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99}, 7, 999},
		{[]int{3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99}, 9, 1001},
		{[]int{3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99}, 0, 999},
		{[]int{3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99}, -999, 999},
		{[]int{3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99}, 999, 1001},
		{[]int{104, 1125899906842624, 99}, 0, 1125899906842624},
	}

	for _, test := range tests {
		var output int
		testInputFunc := func() int {
			return test.input
		}
		testOutputFunc := func(value int) {
			output = value
		}
		testname := fmt.Sprintf("%d,%d", test.program, test.expected)
		t.Run(testname, func(t *testing.T) {
			runProgram(test.program, testInputFunc, testOutputFunc)
			assert.Equal(t, test.expected, output, "Test output should match expected")
		})
	}
}

func TestThisProgramOutputsItself(t *testing.T) {
	testProgram := []int{109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99}
	var output []int
	testInputFunc := func() int {
		return 0
	}
	testOutputFunc := func(value int) {
		output = append(output, value)
	}
	runProgram(testProgram, testInputFunc, testOutputFunc)
	for i, val := range testProgram {
		assert.Equal(t, val, output[i], "Test output should match expected")
	}
}

func TestThisProgramOutputsA16DigitNumber(t *testing.T) {
	testProgram := []int{1102, 34915192, 34915192, 7, 4, 7, 99, 0}
	var output int
	testInputFunc := func() int {
		return 0
	}
	testOutputFunc := func(value int) {
		output = value
	}
	runProgram(testProgram, testInputFunc, testOutputFunc)
	assert.Equal(t, 16, len(strconv.Itoa(output)), "Test output should match expected")
}
