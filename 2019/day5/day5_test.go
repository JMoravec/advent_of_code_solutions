package main

import (
	"fmt"
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
		t.Run(testname, func(t *testing.T) {
			runProgram(test.program, testInputFunc, testOutputFunc)
			assert.Equal(t, len(test.expected), len(test.program), "Lengths of the arrays should be equal")
			for i, actualValue := range test.program {
				assert.Equal(t, test.expected[i], actualValue, "Incorrect value")
			}
		})
	}
}
