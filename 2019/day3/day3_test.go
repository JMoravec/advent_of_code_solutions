package main

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestGetDistance(t *testing.T) {
	var tests = []struct {
		line1    []string
		line2    []string
		expected int
	}{
		{[]string{"R8", "U5", "L5", "D3"}, []string{"U7", "R6", "D4", "L4"}, 6},
		{[]string{"R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"}, []string{"U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"}, 159},
		{[]string{"R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"}, []string{"U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"}, 135},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%s,%s,%d", test.line1, test.line2, test.expected)
		t.Run(testname, func(t *testing.T) {
			actual := getDistance(test.line1, test.line2)
			assert.Equal(t, test.expected, actual, "Expected distance to be the same")
		})
	}
}
