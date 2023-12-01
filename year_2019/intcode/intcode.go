package intcode

import (
	"fmt"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

// paramMode is a helper type to determine where the program should get the operand or set the result
type paramMode int

const (
	// positionMode is for a pointer to a point in memory
	positionMode paramMode = 0
	// immediateMode is the value as stated in memory
	immediateMode paramMode = 1
	// relativeMode is a pointer relative to the Relative Base + this value
	relativeMode paramMode = 2
)

// opcode is a struct that contains the full operation -> opcode + params into a seperated format
type opcode struct {
	opcode      int
	firstParam  paramMode
	secondParam paramMode
	thirdParam  paramMode
}

func getMode(input byte) paramMode {
	if string(input) == "0" {
		return positionMode
	} else if string(input) == "1" {
		return immediateMode
	}

	return relativeMode
}

func processOpcode(op int) opcode {
	var result opcode
	strOp := strconv.Itoa(op)
	if len(strOp) == 1 {
		result.opcode = op
		result.firstParam = positionMode
		result.secondParam = positionMode
		result.thirdParam = positionMode
		return result
	}

	var err error
	result.opcode, err = strconv.Atoi(strOp[len(strOp)-2:])
	check(err)

	if len(strOp) > 2 {
		result.firstParam = getMode(strOp[len(strOp)-3])
	} else {
		result.firstParam = positionMode
	}

	if len(strOp) > 3 {
		result.secondParam = getMode(strOp[len(strOp)-4])
	} else {
		result.secondParam = positionMode
	}

	if len(strOp) > 4 {
		result.thirdParam = getMode(strOp[len(strOp)-5])
	} else {
		result.thirdParam = positionMode
	}

	return result
}

func applyTwoLengthOpCode(program []int, currentLocation *int, opcode opcode, method func(int, int) int, relativeBase int) {
	operand1 := getOperand(program, (*currentLocation)+1, opcode.firstParam, relativeBase)
	operand2 := getOperand(program, (*currentLocation)+2, opcode.secondParam, relativeBase)
	result := method(operand1, operand2)
	if opcode.thirdParam == relativeMode {
		program[program[(*currentLocation)+3]+relativeBase] = result
	} else {
		program[program[(*currentLocation)+3]] = result
	}
	*currentLocation += 4
}

func getOperand(program []int, location int, mode paramMode, relativeBase int) int {
	if mode == positionMode {
		return program[program[location]]
	} else if mode == immediateMode {
		return program[location]
	}

	return program[program[location]+relativeBase]

}

func add(operand1 int, operand2 int) int {
	return operand1 + operand2
}

func multiply(operand1 int, operand2 int) int {
	return operand1 * operand2
}

func getInput(program []int, currentLocation *int, opcode opcode, inputMethod func() int, relativeBase int) {
	inputValue := inputMethod()
	if opcode.firstParam == relativeMode {
		program[program[(*currentLocation)+1]+relativeBase] = inputValue
	} else {
		program[program[(*currentLocation)+1]] = inputValue
	}
	*currentLocation += 2
}

func outputValue(program []int, currentLocation *int, opcode opcode, outputMethod func(int), relativeBase int) {
	outputMethod(getOperand(program, (*currentLocation)+1, opcode.firstParam, relativeBase))
	*currentLocation += 2
}

func jumpTo(program []int, currentLocation *int, opcode opcode, jumpOnNonZero bool, relativeBase int) {
	testValue := getOperand(program, (*currentLocation)+1, opcode.firstParam, relativeBase)
	jumpToLocation := getOperand(program, (*currentLocation)+2, opcode.secondParam, relativeBase)

	if (jumpOnNonZero && testValue != 0) || (!jumpOnNonZero && testValue == 0) {
		*currentLocation = jumpToLocation
	} else {
		*currentLocation += 3
	}
}

func compareTo(program []int, currentLocation *int, opcode opcode, lessThan bool, relativeBase int) {
	firstValue := getOperand(program, (*currentLocation)+1, opcode.firstParam, relativeBase)
	secondValue := getOperand(program, (*currentLocation)+2, opcode.secondParam, relativeBase)

	storeValue := 0

	if (lessThan && firstValue < secondValue) || (!lessThan && firstValue == secondValue) {
		storeValue = 1
	}

	if opcode.thirdParam == relativeMode {
		program[program[(*currentLocation)+3]+relativeBase] = storeValue
	} else {
		program[program[(*currentLocation)+3]] = storeValue
	}
	*currentLocation += 4

}
func setRelativeBase(program []int, currentLocation *int, opcode opcode, relativeBase *int) {
	*relativeBase = *relativeBase + getOperand(program, (*currentLocation)+1, opcode.firstParam, *relativeBase)
	*currentLocation += 2
}

/*
RunProgram runs the given intcode program using the given input and output methods for
input and output respectively
*/
func RunProgram(program []int, inputMethod func() int, outputMethod func(int)) []int {
	// add extra memory
	program = append(program, make([]int, 10000)...)
	//set initial values
	currentLocation := 0
	exit := false
	relativeBase := 0
	for {
		opcode := processOpcode(program[currentLocation])
		switch opcode.opcode {
		case 1:
			applyTwoLengthOpCode(program, &currentLocation, opcode, add, relativeBase)
		case 2:
			applyTwoLengthOpCode(program, &currentLocation, opcode, multiply, relativeBase)
		case 3:
			getInput(program, &currentLocation, opcode, inputMethod, relativeBase)
		case 4:
			outputValue(program, &currentLocation, opcode, outputMethod, relativeBase)
		case 5:
			jumpTo(program, &currentLocation, opcode, true, relativeBase)
		case 6:
			jumpTo(program, &currentLocation, opcode, false, relativeBase)
		case 7:
			compareTo(program, &currentLocation, opcode, true, relativeBase)
		case 8:
			compareTo(program, &currentLocation, opcode, false, relativeBase)
		case 9:
			setRelativeBase(program, &currentLocation, opcode, &relativeBase)
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
	return program
}
