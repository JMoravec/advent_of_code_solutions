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
	file, err := os.Open("day5_input.txt")
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
	inputFunc := func() int {
		//reader := bufio.NewReader(os.Stdin)
		//fmt.Print("Enter text: ")
		//text, err := reader.ReadString('\n')
		//check(err)
		//value, err := strconv.Atoi(strings.TrimSpace(text))
		//check(err)
		//return value
		return 1
	}

	outputFunc := func(value int) {
		fmt.Println("", value)
	}
	runProgram(mainProgram, inputFunc, outputFunc)
}

type ParamMode int

const (
	PositionMode  ParamMode = 0
	ImmediateMode ParamMode = 1
)

type Opcode struct {
	opcode      int
	firstParam  ParamMode
	secondParam ParamMode
	thirdParam  ParamMode
}

func getMode(input byte) ParamMode {
	if string(input) == "0" {
		return PositionMode
	}
	return ImmediateMode
}

func processOpcode(op int) Opcode {
	var result Opcode
	strOp := strconv.Itoa(op)
	if len(strOp) == 1 {
		result.opcode = op
		result.firstParam = PositionMode
		result.secondParam = PositionMode
		result.thirdParam = PositionMode
		return result
	}

	var err error
	result.opcode, err = strconv.Atoi(strOp[len(strOp)-2:])
	check(err)

	if len(strOp) > 2 {
		result.firstParam = getMode(strOp[len(strOp)-3])
	} else {
		result.firstParam = PositionMode
	}

	if len(strOp) > 3 {
		result.secondParam = getMode(strOp[len(strOp)-4])
	} else {
		result.secondParam = PositionMode
	}

	if len(strOp) > 4 {
		result.thirdParam = getMode(strOp[len(strOp)-5])
	} else {
		result.thirdParam = PositionMode
	}

	return result
}

func applyTwoLengthOpCode(program []int, currentLocation *int, opcode Opcode, method func(int, int) int) {
	operand1 := getOperand(program, (*currentLocation)+1, opcode.firstParam)
	operand2 := getOperand(program, (*currentLocation)+2, opcode.secondParam)
	result := method(operand1, operand2)
	program[program[(*currentLocation)+3]] = result
	*currentLocation += 4
}

func getOperand(program []int, location int, mode ParamMode) int {
	if mode == PositionMode {
		return program[program[location]]
	}
	return program[location]
}

func add(operand1 int, operand2 int) int {
	return operand1 + operand2
}

func multiply(operand1 int, operand2 int) int {
	return operand1 * operand2
}

func getInput(program []int, currentLocation *int, inputMethod func() int) {
	inputValue := inputMethod()
	//fmt.Println("In getInput", program[(*currentLocation)+1])
	//fmt.Println("In getInput", program[program[(*currentLocation)+1]])
	program[program[(*currentLocation)+1]] = inputValue
	*currentLocation += 2
	//program[55555555555] = 1
}

func outputValue(program []int, currentLocation *int, opcode Opcode, outputMethod func(int)) {
	outputMethod(getOperand(program, (*currentLocation)+1, opcode.firstParam))
	*currentLocation += 2
}

func runProgram(program []int, inputMethod func() int, outputMethod func(int)) {
	currentLocation := 0
	exit := false
	for {
		//fmt.Println("", program)
		opcode := processOpcode(program[currentLocation])
		//fmt.Println("", opcode)
		//fmt.Println("", currentLocation)
		//fmt.Println("", program[currentLocation])
		//fmt.Println("", program)
		switch opcode.opcode {
		case 1:
			applyTwoLengthOpCode(program, &currentLocation, opcode, add)
		case 2:
			applyTwoLengthOpCode(program, &currentLocation, opcode, multiply)
		case 3:
			getInput(program, &currentLocation, inputMethod)
		case 4:
			outputValue(program, &currentLocation, opcode, outputMethod)
		case 99:
			exit = true
		}

		if exit {
			break
		}
	}
}
