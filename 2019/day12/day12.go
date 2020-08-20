package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type Moon struct {
	x    int
	y    int
	z    int
	velX int
	velY int
	velZ int
}

func textToMoon(input string) Moon {
	re := regexp.MustCompile(`<x=(-*\d+), y=(-*\d+), z=(-*\d+)>`)
	matches := re.FindStringSubmatch(input)
	x, err := strconv.Atoi(matches[1])
	check(err)
	y, err := strconv.Atoi(matches[2])
	check(err)
	z, err := strconv.Atoi(matches[3])
	check(err)
	return Moon{x, y, z, 0, 0, 0}
}

func (moon *Moon) applyGravity(moonB *Moon) {
	applyGravityToVelocity(moon.x, moonB.x, &moon.velX, &moonB.velX)
	applyGravityToVelocity(moon.y, moonB.y, &moon.velY, &moonB.velY)
	applyGravityToVelocity(moon.z, moonB.z, &moon.velZ, &moonB.velZ)
}

func (moon *Moon) applyVelocity() {
	moon.x += moon.velX
	moon.y += moon.velY
	moon.z += moon.velZ
}

func (moon *Moon) copy() Moon {
	return Moon{moon.x, moon.y, moon.z, moon.velX, moon.velY, moon.velZ}
}

func applyGravityToVelocity(firstValue int, secondValue int, firstVelocity *int, secondVelocity *int) {
	if firstValue < secondValue {
		(*firstVelocity)++
		(*secondVelocity)--
	} else if firstValue > secondValue {
		(*firstVelocity)--
		(*secondVelocity)++
	}
}

func timeStep(moons []Moon) ([]Moon, error) {
	if len(moons) != 4 {
		return moons, errors.New("Length of moons is not 4")
	}
	for i := range moons {
		for j := range moons[i+1:] {
			moons[i].applyGravity(&moons[i+1+j])
		}
	}
	for i := range moons {
		moons[i].applyVelocity()
	}
	return moons, nil
}

func runSimulationUntilRepeat(moons []Moon) int {
	moonInitialState := make([]Moon, len(moons))
	for i, moon := range moons {
		moonInitialState[i] = moon.copy()
	}
	xRepeatSteps, yRepeatSteps, zRepeatSteps := 0, 0, 0

	for i := 1; xRepeatSteps == 0 || yRepeatSteps == 0 || zRepeatSteps == 0; i++ {
		var err error
		moons, err = timeStep(moons)
		check(err)
		if xRepeatSteps == 0 && checkXState(moons, moonInitialState) {
			xRepeatSteps = i
		}
		if yRepeatSteps == 0 && checkYState(moons, moonInitialState) {
			yRepeatSteps = i
		}
		if zRepeatSteps == 0 && checkZState(moons, moonInitialState) {
			zRepeatSteps = i
		}
	}

	return lcm(lcm(xRepeatSteps, yRepeatSteps), zRepeatSteps)
}

func lcm(x, y int) int {
	return abs(x*y) / gcd(x, y)
}

func gcd(x, y int) int {
	for y != 0 {
		x, y = y, x%y
	}
	return x
}

func checkXState(moons []Moon, initialState []Moon) bool {
	sameState := true
	for i := range moons {
		if moons[i].x != initialState[i].x || moons[i].velX != initialState[i].velX {
			sameState = false
			break
		}
	}
	return sameState
}
func checkYState(moons []Moon, initialState []Moon) bool {
	sameState := true
	for i := range moons {
		if moons[i].y != initialState[i].y || moons[i].velY != initialState[i].velY {
			sameState = false
			break
		}
	}
	return sameState
}
func checkZState(moons []Moon, initialState []Moon) bool {
	sameState := true
	for i := range moons {
		if moons[i].z != initialState[i].z || moons[i].velZ != initialState[i].velZ {
			sameState = false
			break
		}
	}
	return sameState
}

func runSimulation(moons []Moon, numberOfSteps int) ([]Moon, int) {
	for i := 0; i < numberOfSteps; i++ {
		var err error
		moons, err = timeStep(moons)
		check(err)
	}
	return moons, getTotalEnergy(moons)
}
func getTotalEnergy(moons []Moon) int {
	total := 0
	for _, moon := range moons {
		total += (abs(moon.x) + abs(moon.y) + abs(moon.z)) * (abs(moon.velX) + abs(moon.velY) + abs(moon.velZ))
	}
	return total
}

func abs(input int) int {
	if input < 0 {
		return -input
	}
	return input
}

func main() {
	file, err := os.Open("day12_input.txt")
	check(err)
	defer file.Close()
	textInput := make([]string, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		textInput = append(textInput, scanner.Text())
	}
	err = scanner.Err()
	check(err)

	moonSet := make([]Moon, len(textInput))
	for i := range textInput {
		moonSet[i] = textToMoon(textInput[i])
	}
	_, totalEnergy := runSimulation(moonSet, 1000)
	stepsToRepeat := runSimulationUntilRepeat(moonSet)
	fmt.Println(totalEnergy)
	fmt.Println(stepsToRepeat)
}
