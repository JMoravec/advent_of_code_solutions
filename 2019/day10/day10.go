package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

/*
Asteroid helper type to hold the location of asteroids
*/
type Asteroid struct {
	x int
	y int
}

func getAsteroids(input []string) []Asteroid {
	allAsteroids := make([]Asteroid, 0)
	for yPos, xLine := range input {
		for xPos, character := range xLine {
			if character == '#' {
				allAsteroids = append(allAsteroids, Asteroid{xPos, yPos})
			}
		}
	}

	return allAsteroids
}

func getAsteroidVision(inputAsteroid Asteroid, allAsteroids []Asteroid) int {
	visibleAsteroids := make([]Asteroid, 0)
	for _, asteroid := range allAsteroids {
		if asteroid == inputAsteroid {
			continue
		}

		unitVector := getUnitVector(inputAsteroid, asteroid)

		if !inAsteroidArray(unitVector, visibleAsteroids) {
			visibleAsteroids = append(visibleAsteroids, unitVector)
		}

	}
	return len(visibleAsteroids)
}

func getUnitVector(testStation Asteroid, testAsteroid Asteroid) Asteroid {
	dx := testAsteroid.x - testStation.x
	dy := testAsteroid.y - testStation.y

	devisor := gcd(abs(dx), abs(dy))
	return Asteroid{dx / devisor, dy / devisor}
}

func getStation(allAsteroids []Asteroid) (Asteroid, int) {
	var bestStation Asteroid
	bestStationVision := 0
	for _, testStation := range allAsteroids {
		stationVision := getAsteroidVision(testStation, allAsteroids)
		if stationVision > bestStationVision {
			bestStation = testStation
			bestStationVision = stationVision
		}
	}
	return bestStation, bestStationVision
}

func inAsteroidArray(inputAsteroid Asteroid, allAsteroids []Asteroid) bool {
	for _, testAsteroid := range allAsteroids {
		if inputAsteroid == testAsteroid {
			return true
		}
	}
	return false
}

func abs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}

func gcd(a int, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func main() {
	file, err := os.Open("day10_input.txt")
	check(err)
	defer file.Close()
	textInput := make([]string, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		textInput = append(textInput, scanner.Text())
	}
	err = scanner.Err()
	check(err)
	locations := getAsteroids(textInput)
	_, numberOfAsteroids := getStation(locations)
	fmt.Println(numberOfAsteroids)
}
