package main

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestGetDistance(t *testing.T) {
	var tests = []struct {
		input    string
		expected bool
	}{
		{"111111", true},
		{"223450", false},
		{"123789", false},
		{"555", false},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%s,%t", test.input, test.expected)
		t.Run(testname, func(t *testing.T) {
			actual := isPassword(test.input)
			assert.Equal(t, test.expected, actual, "Expected value to be correct")
		})
	}
}
