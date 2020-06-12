package main

import (
	"fmt"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	total := 0
	for i := 138307; i <= 654504; i++ {
		if isPassword(strconv.Itoa(i)) {
			total++
		}
	}
	fmt.Println(total)
}

func isPassword(input string) bool {
	return isSixDigits(input) && hasTwoAdjacent(input) && neverDecreases(input)
}

func isSixDigits(input string) bool {
	return len(input) == 6
}

func hasTwoAdjacent(input string) bool {
	testLetter := input[0]
	for i := 1; i < len(input); i++ {
		letter := input[i]
		if testLetter == letter {
			return true
		}
		testLetter = letter
	}
	return false
}

func neverDecreases(input string) bool {
	testLetter, _ := strconv.Atoi(string(input[0]))
	for i := 1; i < len(input); i++ {
		currentLetter, _ := strconv.Atoi(string(input[i]))
		if testLetter > currentLetter {
			return false
		}
		testLetter = currentLetter
	}
	return true
}
