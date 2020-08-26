package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	file, err := os.Open("day16_input.txt")
	check(err)
	defer file.Close()
	textInput := make([]string, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		textInput = append(textInput, scanner.Text())
	}
	err = scanner.Err()
	check(err)
	fmt.Println(calculatePhase(textInput[0], 100)[0:8])
}

func getDigitsForInt(number int) int {
	if number < 10 {
		return 1
	} else {
		return 1 + getDigitsForInt(number/10)
	}
}

func stringToDigitSlice(inputValue string) []int {
	intArray := make([]int, len(inputValue))
	for i, char := range inputValue {
		var err error
		if string(char) != "-" {
			intArray[i], err = strconv.Atoi(string(char))
			check(err)
		} else {
			intArray[i] = -1
		}
	}
	return intArray
}

func calculatePhase(inputValue string, phases int) string {
	nextDigit := ""
	for i := range inputValue {
		nextDigit += strconv.Itoa(calculatePhaseDigit(inputValue, i))
	}
	if phases-1 == 0 {
		return nextDigit
	}
	return calculatePhase(nextDigit, phases-1)
}

func calculatePhaseDigit(inputValue string, outputDigit int) int {
	basePattern := []int{0, 1, 0, -1}
	digits := stringToDigitSlice(inputValue)
	patternForDigit := make([]int, len(digits))
	i := 0
	currentPatternIndex := 0
	firstPosition := true
	for i < len(digits) {
		for j := 0; j < outputDigit+1 && i < len(digits); j++ {
			if !firstPosition {
				patternForDigit[i] = basePattern[currentPatternIndex]
				i++
			} else {
				firstPosition = false
			}
		}
		currentPatternIndex++
		if currentPatternIndex >= len(basePattern) {
			currentPatternIndex = 0
		}
	}

	total := 0
	for i, val := range digits {
		total += val * patternForDigit[i]
	}
	answer := stringToDigitSlice(strconv.Itoa(total))
	return answer[len(answer)-1]
}
