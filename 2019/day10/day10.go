package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
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

type asteroidToStation struct {
	asteroid Asteroid
	distance float64
}

type byDistance []asteroidToStation

func (a byDistance) Len() int           { return len(a) }
func (a byDistance) Less(i, j int) bool { return a[i].distance < a[j].distance }
func (a byDistance) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }

func shootAsteroids(allAsteroids []Asteroid, station Asteroid) []Asteroid {
	shotAsteroids := make([]Asteroid, len(allAsteroids)-1)
	asteroidAngles := getAsteroidAngleMap(allAsteroids, station)
	sortedAngles := getSortedAngles(asteroidAngles)
	i := 0
	for i < len(shotAsteroids) {
		for _, angle := range sortedAngles {
			testAsteroid := asteroidAngles[angle]
			if !(testAsteroid == nil || len(testAsteroid) == 0) {
				shotAsteroids[i] = testAsteroid[0].asteroid
				if len(testAsteroid) == 1 {
					asteroidAngles[angle] = nil
				} else {
					asteroidAngles[angle] = testAsteroid[1:]
				}
				i++
			}
		}
	}

	return shotAsteroids
}

func getSortedAngles(asteroidAngles map[float64][]asteroidToStation) []float64 {
	sortedAngles := make([]float64, len(asteroidAngles))
	i := 0
	for k := range asteroidAngles {
		sortedAngles[i] = k
		i++
	}
	sort.Float64s(sortedAngles)
	return sortedAngles
}

func getAsteroidAngleMap(allAsteroids []Asteroid, station Asteroid) map[float64][]asteroidToStation {
	asteroidAngles := make(map[float64][]asteroidToStation)
	for _, asteroid := range allAsteroids {
		if station == asteroid {
			continue
		}
		angle, distance := getAngleToStation(station, asteroid)
		if asteroidAngles[angle] == nil {
			asteroidAngles[angle] = make([]asteroidToStation, 1)
			asteroidAngles[angle][0] = asteroidToStation{asteroid, distance}
		} else {
			asteroidAngles[angle] = append(asteroidAngles[angle], asteroidToStation{asteroid, distance})
		}
	}

	for _, asteroids := range asteroidAngles {
		sort.Sort(byDistance(asteroids))
	}
	return asteroidAngles
}

func getAngleToStation(station Asteroid, asteroid Asteroid) (float64, float64) {
	relativeToStationAsteroid := Asteroid{asteroid.x - station.x, station.y - asteroid.y}

	angle := math.Atan2(float64(relativeToStationAsteroid.x), float64(relativeToStationAsteroid.y))
	if angle < 0 {
		angle = (2 * math.Pi) + angle
	}
	distance := math.Sqrt(math.Pow(float64(relativeToStationAsteroid.x), 2) + math.Pow(float64(relativeToStationAsteroid.y), 2))

	return angle, distance
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
	station, numberOfAsteroids := getStation(locations)
	fmt.Println("Number of Asteroids the station can see: ", numberOfAsteroids)
	shotAsteroids := shootAsteroids(locations, station)
	fmt.Println("200th shot asteroid: ", shotAsteroids[199])
}
