package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	var orbits []string
	file, err := os.Open("day6_input.txt")
	check(err)
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		input := scanner.Text()
		orbits = append(orbits, input)
	}
	err = scanner.Err()
	check(err)
	fmt.Println(getOrbitTransfer(orbits))
}

type Orbit struct {
	name           string
	orbitsStr      string
	orbits         *Orbit
	numberOfOrbits int
}

func convertStrToOrbit(input string) Orbit {
	splitStr := strings.Split(input, ")")
	orbit := Orbit{name: splitStr[1], orbitsStr: splitStr[0]}
	return orbit
}

func setOrbits(allOrbits map[string]*Orbit) {
	for _, orbit := range allOrbits {
		if orbit.name != "COM" {
			orbit.orbits = allOrbits[orbit.orbitsStr]
		}
	}
}

func getTotalOrbits(orbits []string) int {
	allOrbits := make(map[string]*Orbit)
	comOrbit := Orbit{name: "COM", orbits: nil, numberOfOrbits: 0}
	allOrbits["COM"] = &comOrbit
	for _, orbit := range orbits {
		convertedOrbit := convertStrToOrbit(orbit)
		allOrbits[convertedOrbit.name] = &convertedOrbit
	}

	setOrbits(allOrbits)

	total := 0
	for _, orbit := range allOrbits {
		total += orbit.getNumberOfOrbits(allOrbits, "COM")
	}
	return total
}

func getOrbitTransfer(orbits []string) int {
	allOrbits := make(map[string]*Orbit)
	comOrbit := Orbit{name: "COM", orbits: nil, numberOfOrbits: 0}
	allOrbits["COM"] = &comOrbit
	for _, orbit := range orbits {
		convertedOrbit := convertStrToOrbit(orbit)
		allOrbits[convertedOrbit.name] = &convertedOrbit
	}
	setOrbits(allOrbits)

	commonOrbit := getCommonOrbit(allOrbits["YOU"], allOrbits["SAN"], allOrbits)
	numberOfOrbitsFirstToCommon := allOrbits["YOU"].getNumberOfOrbits(allOrbits, commonOrbit.name)
	numberOfOrbitsCommonToSan := allOrbits["SAN"].getNumberOfOrbits(allOrbits, commonOrbit.name)
	return numberOfOrbitsCommonToSan + numberOfOrbitsFirstToCommon - 2
}

func getCommonOrbit(firstOrbit *Orbit, secondOrbit *Orbit, allOrbits map[string]*Orbit) *Orbit {
	firstOrbitAllOrbits := getAllOrbits(firstOrbit, allOrbits)
	secondOrbitAllOrbits := getAllOrbits(secondOrbit, allOrbits)
	for _, orbit := range firstOrbitAllOrbits {
		for _, testOrbit := range secondOrbitAllOrbits {
			if orbit == testOrbit {
				return allOrbits[orbit]
			}
		}
	}
	return allOrbits["COM"]
}

func getAllOrbits(mainOrbit *Orbit, allOrbits map[string]*Orbit) []string {
	if mainOrbit.name == "COM" {
		return make([]string, 0)
	}
	return append([]string{mainOrbit.orbitsStr}, getAllOrbits(mainOrbit.orbits, allOrbits)...)
}

func (o *Orbit) getNumberOfOrbits(allOrbits map[string]*Orbit, endOrbit string) int {
	if o.numberOfOrbits != 0 || o.name == endOrbit {
		return o.numberOfOrbits
	}
	return 1 + allOrbits[o.name].orbits.getNumberOfOrbits(allOrbits, endOrbit)
}
