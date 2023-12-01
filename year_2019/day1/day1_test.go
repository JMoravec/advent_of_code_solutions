package main

import (
	"fmt"
	"testing"
)

func TestGetFuelAmount(t *testing.T) {
	var tests = []struct {
		mass     int
		expected int
	}{
		{12, 2},
		{14, 2},
		{1969, 966},
		{100756, 50346},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%d,%d", test.mass, test.expected)
		t.Run(testname, func(t *testing.T) {
			actual := getFuelAmount(test.mass)
			if actual != test.expected {
				t.Errorf("got %d, want %d", actual, test.expected)
			}
		})
	}
}
