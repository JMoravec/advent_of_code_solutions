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

type point struct {
	x int
	y int
}

func (currentPoint *point) moveForward(directionToGo direction) {
	switch directionToGo {
	case UP:
		currentPoint.y++
	case DOWN:
		currentPoint.y--
	case LEFT:
		currentPoint.x--
	case RIGHT:
		currentPoint.x++
	}
}

type direction int
type Color int

const (
	BLACK Color = 0
	WHITE Color = 1
)

const (
	UP    direction = iota
	DOWN  direction = iota
	LEFT  direction = iota
	RIGHT direction = iota
)

func (currentDirection direction) turnRight() direction {
	switch currentDirection {
	case UP:
		return RIGHT
	case DOWN:
		return LEFT
	case RIGHT:
		return DOWN
	case LEFT:
		return UP
	default:
		return UP
	}
}

func (currentDirection direction) turnLeft() direction {
	switch currentDirection {
	case UP:
		return LEFT
	case DOWN:
		return RIGHT
	case RIGHT:
		return UP
	case LEFT:
		return DOWN
	default:
		return UP
	}
}

func getProgram(filename string) []int {
	var mainProgram []int
	file, err := os.Open("day11_input.txt")
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
	return mainProgram
}

type pointArray []point

func (allPoints pointArray) contains(testPoint point) bool {
	for _, point := range allPoints {
		if point == testPoint {
			return true
		}
	}
	return false
}

func printPanel(panel [][]int) {
	for i := len(panel) - 1; i >= 0; i-- {
		row := panel[i]
		for _, value := range row {
			if value == 0 {
				fmt.Printf(".")
			} else {
				fmt.Printf("#")
			}
		}
		fmt.Printf("\n")
	}
}

func main() {
	panel := make([][]int, 10)
	for i := range panel {
		panel[i] = make([]int, 70)
	}

	currentLocation := point{10, 6}

	panel[currentLocation.y][currentLocation.x] = 1

	paintedPoints := make(pointArray, 0)

	mainProgram := getProgram("day11_input.txt")

	inputFunc := func() int {
		return panel[currentLocation.y][currentLocation.x]
	}

	paintOutput := true
	currentDirection := UP

	outputFunc := func(value int) {
		if paintOutput {
			panel[currentLocation.y][currentLocation.x] = value
			if !paintedPoints.contains(currentLocation) {
				paintedPoints = append(paintedPoints, currentLocation)
			}
		} else {
			if value == 0 {
				currentDirection = currentDirection.turnLeft()
			} else {
				currentDirection = currentDirection.turnRight()
			}
			currentLocation.moveForward(currentDirection)
		}
		paintOutput = !paintOutput
	}
	runProgram(mainProgram, inputFunc, outputFunc)
	fmt.Println(len(paintedPoints))
	printPanel(panel)
}

// ParamMode is a helper type to determine where the program should get the operand or set the result
type ParamMode int

const (
	// PositionMode is for a pointer to a point in memory
	PositionMode ParamMode = 0
	// ImmediateMode is the value as stated in memory
	ImmediateMode ParamMode = 1
	// RelativeMode is a pointer relative to the Relative Base + this value
	RelativeMode ParamMode = 2
)

// Opcode is a struct that contains the full operation -> opcode + params into a seperated format
type Opcode struct {
	opcode      int
	firstParam  ParamMode
	secondParam ParamMode
	thirdParam  ParamMode
}

func getMode(input byte) ParamMode {
	if string(input) == "0" {
		return PositionMode
	} else if string(input) == "1" {
		return ImmediateMode
	}

	return RelativeMode
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

func applyTwoLengthOpCode(program []int, currentLocation *int, opcode Opcode, method func(int, int) int, relativeBase int) {
	operand1 := getOperand(program, (*currentLocation)+1, opcode.firstParam, relativeBase)
	operand2 := getOperand(program, (*currentLocation)+2, opcode.secondParam, relativeBase)
	result := method(operand1, operand2)
	if opcode.thirdParam == RelativeMode {
		program[program[(*currentLocation)+3]+relativeBase] = result
	} else {
		program[program[(*currentLocation)+3]] = result
	}
	*currentLocation += 4
}

func getOperand(program []int, location int, mode ParamMode, relativeBase int) int {
	if mode == PositionMode {
		return program[program[location]]
	} else if mode == ImmediateMode {
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

func getInput(program []int, currentLocation *int, opcode Opcode, inputMethod func() int, relativeBase int) {
	inputValue := inputMethod()
	if opcode.firstParam == RelativeMode {
		program[program[(*currentLocation)+1]+relativeBase] = inputValue
	} else {
		program[program[(*currentLocation)+1]] = inputValue
	}
	*currentLocation += 2
}

func outputValue(program []int, currentLocation *int, opcode Opcode, outputMethod func(int), relativeBase int) {
	outputMethod(getOperand(program, (*currentLocation)+1, opcode.firstParam, relativeBase))
	*currentLocation += 2
}

func jumpTo(program []int, currentLocation *int, opcode Opcode, jumpOnNonZero bool, relativeBase int) {
	testValue := getOperand(program, (*currentLocation)+1, opcode.firstParam, relativeBase)
	jumpToLocation := getOperand(program, (*currentLocation)+2, opcode.secondParam, relativeBase)

	if (jumpOnNonZero && testValue != 0) || (!jumpOnNonZero && testValue == 0) {
		*currentLocation = jumpToLocation
	} else {
		*currentLocation += 3
	}
}

func compareTo(program []int, currentLocation *int, opcode Opcode, lessThan bool, relativeBase int) {
	firstValue := getOperand(program, (*currentLocation)+1, opcode.firstParam, relativeBase)
	secondValue := getOperand(program, (*currentLocation)+2, opcode.secondParam, relativeBase)

	storeValue := 0

	if (lessThan && firstValue < secondValue) || (!lessThan && firstValue == secondValue) {
		storeValue = 1
	}

	if opcode.thirdParam == RelativeMode {
		program[program[(*currentLocation)+3]+relativeBase] = storeValue
	} else {
		program[program[(*currentLocation)+3]] = storeValue
	}
	*currentLocation += 4

}
func setRelativeBase(program []int, currentLocation *int, opcode Opcode, relativeBase *int) {
	*relativeBase = *relativeBase + getOperand(program, (*currentLocation)+1, opcode.firstParam, *relativeBase)
	*currentLocation += 2
}

func runProgram(program []int, inputMethod func() int, outputMethod func(int)) []int {
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
