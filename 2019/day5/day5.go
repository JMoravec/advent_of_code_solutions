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
	exit := false
	inputFunc := func() int {
		reader := bufio.NewReader(os.Stdin)
		fmt.Print("Enter text: ")
		text, _ := reader.ReadString('\n')
		value, _ := strconv.Atoi(text)
		return value
	}
	outputFunc := func(value int) {
		fmt.Printf("%v", value)
	}
	for noun := 0; noun < 100; noun++ {
		for verb := 0; verb < 100; verb++ {
			copyProgram := make([]int, len(mainProgram))
			copy(copyProgram, mainProgram)
			copyProgram[1] = noun
			copyProgram[2] = verb
			runProgram(copyProgram, inputFunc, outputFunc)
			if copyProgram[0] == 19690720 {
				exit = true
				fmt.Println(100*noun + verb)
				break
			}
		}
		if exit {
			break
		}
	}
}

func add(program []int, currentLocation *int, opcode string) {
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

func getInput(program []int, currentLocation *int, inputMethod func() int) {
	inputValue := inputMethod()
	program[program[(*currentLocation)+1]] = inputValue
	*currentLocation += 2
}

func outputValue(program []int, currentLocation *int, outputMethod func(int)) {
	outputMethod(program[(*currentLocation)+1])
	*currentLocation += 2
}

func runProgram(program []int, inputMethod func() int, outputMethod func(int)) {
	currentLocation := 0
	exit := false
	for {
		switch program[currentLocation] {
		case 1:
			add(program, &currentLocation)
		case 2:
			multiply(program, &currentLocation)
		case 3:
			getInput(program, &currentLocation, inputMethod)
		case 4:
			outputValue(program, &currentLocation, outputMethod)
		case 99:
			exit = true
		}

		if exit {
			break
		}
	}
}
