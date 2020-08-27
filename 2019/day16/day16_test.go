package main

import (
	"fmt"
	"strconv"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCalculateOutputDiget(t *testing.T) {
	var tests = []struct {
		inputValue  string
		outputDigit int
		expected    int
	}{
		{"12345678", 0, 4},
		{"12345678", 1, 8},
		{"12345678", 2, 2},
		{"12345678", 3, 2},
		{"12345678", 4, 6},
		{"12345678", 5, 1},
		{"12345678", 6, 5},
		{"12345678", 7, 8},
		{"48226158", 0, 3},
		{"48226158", 1, 4},
		{"48226158", 2, 0},
		{"48226158", 3, 4},
		{"48226158", 4, 0},
		{"48226158", 5, 4},
		{"48226158", 6, 3},
		{"48226158", 7, 8},
		{"34040438", 0, 0},
		{"34040438", 1, 3},
		{"34040438", 2, 4},
		{"34040438", 3, 1},
		{"34040438", 4, 5},
		{"34040438", 5, 5},
		{"34040438", 6, 1},
		{"34040438", 7, 8},
	}
	for _, test := range tests {
		testname := fmt.Sprintf("%s,%d:%d", test.inputValue, test.outputDigit, test.expected)
		t.Run(testname, func(t *testing.T) {
			assert.Equal(t, test.expected, calculatePhaseDigit(test.inputValue, test.outputDigit))
		})
	}
}

func TestPhase(t *testing.T) {
	var tests = []struct {
		inputValue string
		phases     int
		expected   string
	}{
		{"12345678", 1, "48226158"},
		{"12345678", 2, "34040438"},
		{"12345678", 3, "03415518"},
		{"12345678", 4, "01029498"},
		{"80871224585914546619083218645595", 100, "24176176"},
		{"19617804207202209144916044189917", 100, "73745418"},
		{"69317163492948606335995924319873", 100, "52432133"},
	}
	for _, test := range tests {
		testname := fmt.Sprintf("%s,%d:%s", test.inputValue, test.phases, test.expected)
		t.Run(testname, func(t *testing.T) {
			assert.Equal(t, test.expected, calculatePhase(test.inputValue, test.phases)[0:8])
		})
	}
}

func TestRunAlot(t *testing.T) {
	var tests = []struct {
		inputValue string
		expected   string
	}{
		{"03036732577212944063491565474664", "84462026"},
		{"02935109699940807407585447034323", "78725270"},
		{"03081770884921959731165446850517", "53553731"},
	}
	for _, test := range tests {
		offset, _ := strconv.Atoi(test.inputValue[0:7])
		testname := fmt.Sprintf("%s:%s", test.inputValue, test.expected)
		t.Run(testname, func(t *testing.T) {
			assert.Equal(t, test.expected, intArrayToStr(runAlot(test.inputValue, offset)[0:8]))
		})
	}
}
