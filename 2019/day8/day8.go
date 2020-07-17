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
	var image []string
	file, err := os.Open("day8_input.txt")
	check(err)
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		text := scanner.Text()
		image = strings.Split(text, "")
	}
	err = scanner.Err()
	check(err)
	imageInt := imageToInt(image)
	layeredImage := splitImage(imageInt, 25, 6)
	leastZeros := numDigits{99999, 99999, 99999}
	for _, val := range layeredImage {
		totalDigits := getNumDigetsForLayer(val)
		if totalDigits.zeros < leastZeros.zeros {
			leastZeros = totalDigits
		}
	}
	fmt.Println(leastZeros.ones * leastZeros.twos)
}

type numDigits struct {
	zeros int
	ones  int
	twos  int
}

func getNumDigetsForLayer(layer [][]int) numDigits {
	digits := numDigits{0, 0, 0}
	for _, row := range layer {
		for _, digit := range row {
			switch digit {
			case 0:
				digits.zeros++
			case 1:
				digits.ones++
			case 2:
				digits.twos++
			}
		}
	}
	return digits
}

func splitImage(image []int, width int, height int) [][][]int {
	amountOfLayers := len(image) / (width * height)
	returnImage := make([][][]int, amountOfLayers)
	for i := range returnImage {
		returnImage[i] = make([][]int, height)
		for j := range returnImage[i] {
			returnImage[i][j] = make([]int, width)
			for k := range returnImage[i][j] {
				returnImage[i][j][k] = image[(i*height*width)+(j*width)+k]
			}
		}
	}
	return returnImage
}

func imageToInt(image []string) []int {
	var returnImage []int
	for _, val := range image {
		intVal, err := strconv.Atoi(val)
		check(err)
		returnImage = append(returnImage, intVal)
	}
	return returnImage
}
