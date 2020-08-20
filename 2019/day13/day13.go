package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	"../intcode"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type currentOutput int

const (
	X    currentOutput = iota
	Y    currentOutput = iota
	TILE currentOutput = iota
)

type tileId int

const (
	EMPTY             tileId = 0
	WALL              tileId = 1
	BLOCK             tileId = 2
	HORIZONTAL_PADDLE tileId = 3
	BALL              tileId = 4
)

func (id *tileId) getString() string {
	switch *id {
	case EMPTY:
		return " "
	case WALL:
		return "|"
	case BLOCK:
		return "="
	case HORIZONTAL_PADDLE:
		return "-"
	case BALL:
		return "o"
	default:
		return ""
	}
}

func intTotileID(input int) tileId {
	switch input {
	case 0:
		return EMPTY
	case 1:
		return WALL
	case 2:
		return BLOCK
	case 3:
		return HORIZONTAL_PADDLE
	case 4:
		return BALL
	default:
		return EMPTY
	}
}

func printScreen(screen [][]tileId) {
	for i := range screen {
		for _, tile := range screen[i] {
			fmt.Print(tile.getString())
		}
		fmt.Print("\n")
	}
}

func getTotalBlocks(screen [][]tileId) int {
	totalBlocks := 0
	for i := range screen {
		for _, tile := range screen[i] {
			if tile == BLOCK {
				totalBlocks++
			}
		}
	}
	return totalBlocks
}

func main() {
	var mainProgram []int
	file, err := os.Open("day13_input.txt")
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

	currentOut := X

	screen := make([][]tileId, 26)
	for i := range screen {
		screen[i] = make([]tileId, 50)
	}

	xPos := 0
	yPos := 0

	inputFunc := func() int {
		reader := bufio.NewReader(os.Stdin)
		fmt.Print("Enter text: ")
		text, inputErr := reader.ReadString('\n')
		check(inputErr)
		inputInt, intErr := strconv.Atoi(text)
		check(intErr)
		return inputInt
	}

	outputFunc := func(value int) {
		if currentOut == X {
			currentOut = Y
			xPos = value
		} else if currentOut == Y {
			currentOut = TILE
			yPos = value
		} else {
			currentOut = X
			screen[yPos][xPos] = intTotileID(value)
		}
	}
	intcode.RunProgram(mainProgram, inputFunc, outputFunc)
	printScreen(screen)
	fmt.Println("Total Blocks: ", getTotalBlocks(screen))
}
