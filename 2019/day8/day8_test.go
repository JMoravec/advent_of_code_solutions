package main

import (
	"fmt"
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestImageToInt(t *testing.T) {
	var tests = []struct {
		input    string
		expected []int
	}{
		{"123456789012", []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2}},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v,%d", test.input, test.expected)
		t.Run(testname, func(t *testing.T) {
			actual := imageToInt(strings.Split(test.input, ""))

			assert.Equal(t, test.expected, actual, "Incorrect value")
		})
	}
}

func TestSplitImage(t *testing.T) {
	var tests = []struct {
		input    string
		expected [][][]int
	}{
		{"123456789012", [][][]int{{{1, 2, 3}, {4, 5, 6}}, {{7, 8, 9}, {0, 1, 2}}}},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v,%d", test.input, test.expected)
		t.Run(testname, func(t *testing.T) {
			imageInt := imageToInt(strings.Split(test.input, ""))
			actual := splitImage(imageInt, 3, 2)

			assert.Equal(t, test.expected, actual, "Incorrect value")
		})
	}
}
