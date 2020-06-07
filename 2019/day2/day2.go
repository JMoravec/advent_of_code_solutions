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
	var mainProgram []int
	file, err := os.Open("day2_input.txt")
	check(err)
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		input := strings.Split(scanner.Text(), ",")
		for _, value := range input {
			intValue, convertErr := strconv.Atoi(value)
			check(convertErr)
			mainProgram = append(mainProgram, intValue)
		}

	}
	err = scanner.Err()
	check(err)
	mainProgram[1] = 12
	mainProgram[2] = 2
	runProgram(mainProgram)
	fmt.Println(mainProgram[0])
}

func add(program []int, currentLocation *int) {
	operand1 := program[program[(*currentLocation)+1]]
	operand2 := program[program[(*currentLocation)+2]]
	result := operand1 + operand2
	program[program[(*currentLocation)+3]] = result
	*currentLocation += 4
}

func multiply(program []int, currentLocation *int) {
	operand1 := program[program[(*currentLocation)+1]]
	operand2 := program[program[(*currentLocation)+2]]
	result := operand1 * operand2
	program[program[(*currentLocation)+3]] = result
	*currentLocation += 4
}

func runProgram(program []int) {
	currentLocation := 0
	exit := false
	for {
		switch program[currentLocation] {
		case 1:
			add(program, &currentLocation)
		case 2:
			multiply(program, &currentLocation)
		case 99:
			exit = true
		}

		if exit {
			break
		}
	}
}
