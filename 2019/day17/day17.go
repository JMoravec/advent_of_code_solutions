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

func main() {
	var mainProgram []int
	file, err := os.Open("day17_input.txt")
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

	movementArray := "A,A,B,C,B,C,B,A,C,A\n"
	aMovement := "R,8,L,12,R,8\n"
	bMovement := "L,10,L,10,R,8\n"
	cMovement := "L,12,L,12,L,10,R,10\n"
	totalString := movementArray + aMovement + bMovement + cMovement + "n\n"
	intInput := make([]int, len(totalString))

	for i, char := range totalString {
		intInput[i] = int(char)
	}
	fmt.Println(intInput)

	currentInput := 0

	inputFunc := func() int {
		output := intInput[currentInput]
		currentInput++
		return output
	}

	/* part 1
	//Checked Height is 37 tiles and width is 60
	var totalArea [37][60]int
	currentXPos := 0
	currentYPos := 0
	*/

	outputFunc := func(value int) {
		/* part 1
		totalArea[currentYPos][currentXPos] = value
		if value == 10 {
			currentXPos = 0
			currentYPos++
		} else {
			currentXPos++
		}
		*/
		fmt.Print("\n", value)
	}

	// Set to move mode
	mainProgram[0] = 2

	intcode.RunProgram(mainProgram, inputFunc, outputFunc)

	/* part 1
	for i := range totalArea {
		for j := range totalArea[i] {
			fmt.Print(string(totalArea[i][j]))
		}
	}

	intersectionAlignment := 0

	for i := 1; i < len(totalArea)-1; i++ {
		for j := 1; j < len(totalArea[i])-1; j++ {
			if totalArea[i][j] == 35 && totalArea[i-1][j] == 35 && totalArea[i+1][j] == 35 && totalArea[i][j-1] == 35 && totalArea[i][j+1] == 35 {
				intersectionAlignment += i * j
			}
		}
	}
	fmt.Println(intersectionAlignment)
	*/
}
