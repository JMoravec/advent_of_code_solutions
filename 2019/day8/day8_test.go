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
		{"0222112222120000", []int{0, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 0, 0, 0, 0}},
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
		width    int
		height   int
		expected [][][]int
	}{
		{"123456789012", 3, 2, [][][]int{{{1, 2, 3}, {4, 5, 6}}, {{7, 8, 9}, {0, 1, 2}}}},
		{"0222112222120000", 2, 2, [][][]int{{{0, 2}, {2, 2}}, {{1, 1}, {2, 2}}, {{2, 2}, {1, 2}}, {{0, 0}, {0, 0}}}},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v,%d", test.input, test.expected)
		t.Run(testname, func(t *testing.T) {
			imageInt := imageToInt(strings.Split(test.input, ""))
			actual := splitImage(imageInt, test.width, test.height)

			assert.Equal(t, test.expected, actual, "Incorrect value")
		})
	}
}

func TestGetFinalImage(t *testing.T) {
	var tests = []struct {
		input    string
		width    int
		height   int
		expected [][]int
	}{
		{"0222112222120000", 2, 2, [][]int{{0, 1}, {1, 0}}},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v,%d", test.input, test.expected)
		t.Run(testname, func(t *testing.T) {
			imageInt := imageToInt(strings.Split(test.input, ""))
			imageSplit := splitImage(imageInt, test.width, test.height)
			actual := getDecodedImage(imageSplit)

			assert.Equal(t, test.expected, actual, "Incorrect value")
		})
	}
}
