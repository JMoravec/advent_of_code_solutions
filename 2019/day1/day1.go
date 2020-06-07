package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	total := 0
	file, err := os.Open("day1_input.txt")
	check(err)
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		currentModule, scanErr := strconv.Atoi(scanner.Text())
		check(scanErr)
		total += getFuelAmount(currentModule)
	}
	err = scanner.Err()
	check(err)
	fmt.Println(total)
}

func getFuelAmount(mass int) int {
	return (mass / 3) - 2
}
