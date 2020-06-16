package main

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestOrbits(t *testing.T) {
	var tests = []struct {
		input    []string
		expected int
	}{
		{[]string{"COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"}, 42},
		{[]string{"E)J", "B)C", "C)D", "E)F", "COM)B", "B)G", "G)H", "D)E", "D)I", "J)K", "K)L"}, 42},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v,%d", test.input, test.expected)
		t.Run(testname, func(t *testing.T) {
			actual := getTotalOrbits(test.input)
			assert.Equal(t, test.expected, actual, "Incorrect value")
		})
	}
}
func TestOrbitTransfer(t *testing.T) {
	var tests = []struct {
		input    []string
		expected int
	}{
		{[]string{"COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN"}, 4},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v,%d", test.input, test.expected)
		t.Run(testname, func(t *testing.T) {
			actual := getOrbitTransfer(test.input)
			assert.Equal(t, test.expected, actual, "Incorrect value")
		})
	}
}
