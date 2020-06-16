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
	file, err := os.Open("day7_input.txt")
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
	fmt.Println(getMaxThruster(mainProgram))
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
	program[program[(*currentLocation)+1]] = inputValue
	*currentLocation += 2
}

func outputValue(program []int, currentLocation *int, opcode Opcode, outputMethod func(int)) {
	outputMethod(getOperand(program, (*currentLocation)+1, opcode.firstParam))
	*currentLocation += 2
}

func jumpTo(program []int, currentLocation *int, opcode Opcode, jumpOnNonZero bool) {
	testValue := getOperand(program, (*currentLocation)+1, opcode.firstParam)
	jumpToLocation := getOperand(program, (*currentLocation)+2, opcode.secondParam)

	if (jumpOnNonZero && testValue != 0) || (!jumpOnNonZero && testValue == 0) {
		*currentLocation = jumpToLocation
	} else {
		*currentLocation += 3
	}
}

func compareTo(program []int, currentLocation *int, opcode Opcode, lessThan bool) {
	firstValue := getOperand(program, (*currentLocation)+1, opcode.firstParam)
	secondValue := getOperand(program, (*currentLocation)+2, opcode.secondParam)

	storeValue := 0

	if (lessThan && firstValue < secondValue) || (!lessThan && firstValue == secondValue) {
		storeValue = 1
	}

	program[program[(*currentLocation)+3]] = storeValue
	*currentLocation += 4

}

func runProgram(program []int, inputMethod func() int, outputMethod func(int)) {
	currentLocation := 0
	exit := false
	for {
		opcode := processOpcode(program[currentLocation])
		switch opcode.opcode {
		case 1:
			applyTwoLengthOpCode(program, &currentLocation, opcode, add)
		case 2:
			applyTwoLengthOpCode(program, &currentLocation, opcode, multiply)
		case 3:
			getInput(program, &currentLocation, inputMethod)
		case 4:
			outputValue(program, &currentLocation, opcode, outputMethod)
		case 5:
			jumpTo(program, &currentLocation, opcode, true)
		case 6:
			jumpTo(program, &currentLocation, opcode, false)
		case 7:
			compareTo(program, &currentLocation, opcode, true)
		case 8:
			compareTo(program, &currentLocation, opcode, false)
		case 99:
			exit = true
		default:
			fmt.Println("ERROR: RECEIVED OPCODE: ", opcode)
			exit = true
		}

		if exit {
			break
		}
	}
}

func getMaxThruster(program []int) int {
	allInputs := getAllPermutations([]int{0, 1, 2, 3, 4})
	output := 0
	for _, input := range allInputs {
		testOutput := runMaxThrusterProgram(program, input)
		if testOutput > output {
			output = testOutput
		}
	}
	return output
}

func runMaxThrusterProgram(program []int, input []int) int {
	currentPhaseIndex := 0
	var currentOutput *int
	returnPhase := true

	currentOutput = new(int)
	*currentOutput = 0

	inputFunc := func() int {
		var result int
		if returnPhase {
			result = input[currentPhaseIndex]
		} else {
			result = *currentOutput
		}
		returnPhase = !returnPhase
		return result
	}
	outputFunc := func(result int) {
		*currentOutput = result
	}

	for i := range input {
		currentPhaseIndex = i
		runProgram(program, inputFunc, outputFunc)
	}
	return *currentOutput
}

func getAllPermutations(array []int) [][]int {
	var heapsMethod func(int, []int)
	result := [][]int{}
	heapsMethod = func(k int, internalArray []int) {
		if k == 1 {
			tmp := make([]int, len(internalArray))
			copy(tmp, internalArray)
			result = append(result, tmp)
		} else {
			heapsMethod(k-1, internalArray)

			for i := 0; i < k-1; i++ {
				if k%2 == 0 {
					tmp := internalArray[i]
					internalArray[i] = internalArray[k-1]
					internalArray[k-1] = tmp
				} else {
					tmp := internalArray[0]
					internalArray[0] = internalArray[k-1]
					internalArray[k-1] = tmp
				}
				heapsMethod(k-1, internalArray)
			}
		}
	}
	heapsMethod(len(array), array)
	return result
}
