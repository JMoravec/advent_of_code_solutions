package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
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
	inputValue := textInput[0]
	offset, err := strconv.Atoi(inputValue[0:7])
	check(err)
	finalValue := runAlot(inputValue, offset)
	fmt.Println(finalValue[0:8])
}

func strToIntArray(inputValue string) []int {
	output := make([]int, len(inputValue))
	var err error
	for i, char := range inputValue {
		output[i], err = strconv.Atoi(string(char))
		check(err)
	}
	return output
}

func intArrayToStr(input []int) string {
	output := ""
	for _, value := range input {
		output += strconv.Itoa(value)
	}
	return output
}

func runAlot(inputValue string, offset int) []int {
	outputValue := strings.Repeat(inputValue, 10000)[offset:]
	inputIntArray := strToIntArray(outputValue)

	for i := 0; i < 100; i++ {
		currentTotal := 0
		for j := len(outputValue) - 1; j >= 0; j-- {
			currentTotal += inputIntArray[j]
			inputIntArray[j] = currentTotal % 10
		}
	}
	return inputIntArray
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
