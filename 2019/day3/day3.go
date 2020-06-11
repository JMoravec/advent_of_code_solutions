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
	var line1 []string
	var line2 []string
	file, err := os.Open("day3_input.txt")
	check(err)
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	input := strings.Split(scanner.Text(), ",")
	for _, value := range input {
		line1 = append(line1, value)
	}
	scanner.Scan()
	input = strings.Split(scanner.Text(), ",")
	for _, value := range input {
		line2 = append(line2, value)
	}
	fmt.Println(getDistance(line1, line2))
}

func getDistance(line1 []string, line2 []string) int {
	line1Points := generatePoints(line1)
	line2Points := generatePoints(line2)

	touchedPoints := getTouchedPoints(line1Points, line2Points)
	smallestDistance := 99999999999
	for _, point := range touchedPoints {
		if point.steps < smallestDistance {
			smallestDistance = point.steps
		}
	}
	return smallestDistance
}

func getTouchedPoints(line1 []Point, line2 []Point) []Point {
	var touchedPoints []Point
	for _, line1Point := range line1 {
		for _, line2Point := range line2 {
			if line1Point.equal(&line2Point) {
				newPoint := Point{x: line1Point.x, y: line1Point.y, steps: (line1Point.steps + line2Point.steps)}
				touchedPoints = append(touchedPoints, newPoint)
			}
		}
	}

	return touchedPoints
}

func abs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}

func (p *Point) getManhatanDistance() int {
	return abs(p.x) + abs(p.y)
}

func (p1 *Point) equal(p2 *Point) bool {
	return p1.x == p2.x && p1.y == p2.y
}

func generatePoints(line []string) []Point {
	var points []Point
	currentStep := 0
	currentPoint := Point{x: 0, y: 0, steps: currentStep}
	for _, segment := range line {
		points = append(points, segmentToPoints(&currentPoint, segment, &currentStep)...)
		currentPoint = points[len(points)-1]
	}
	return points
}

func segmentToPoints(startPoint *Point, segment string, currentStep *int) []Point {
	var points []Point
	direction := string(segment[0])
	length, err := strconv.Atoi(segment[1:])
	check(err)

	for i := 1; i <= length; i++ {
		(*currentStep)++
		switch direction {
		case "U":
			newPoint := Point{x: startPoint.x, y: (startPoint.y + i), steps: *currentStep}
			points = append(points, newPoint)
		case "D":
			newPoint := Point{x: startPoint.x, y: (startPoint.y - i), steps: *currentStep}
			points = append(points, newPoint)
		case "R":
			newPoint := Point{x: (startPoint.x + i), y: startPoint.y, steps: *currentStep}
			points = append(points, newPoint)
		case "L":
			newPoint := Point{x: (startPoint.x - i), y: startPoint.y, steps: *currentStep}
			points = append(points, newPoint)
		}
	}

	return points
}

type Point struct {
	x     int
	y     int
	steps int
}
