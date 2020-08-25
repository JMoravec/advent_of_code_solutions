package main

import (
	"bufio"
	"errors"
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

type Point struct {
	X int
	Y int
}

type Tile int

const (
	WALL    Tile = 0
	EMPTY   Tile = 1
	OXYGEN  Tile = 2
	PLAYER  Tile = 3
	UNKNOWN Tile = 4
)

type Direction int

const (
	NORTH Direction = 1
	SOUTH Direction = 2
	WEST  Direction = 3
	EAST  Direction = 4
)

func (p *Point) moveDirection(direction Direction) {
	switch direction {
	case NORTH:
		p.Y--
	case SOUTH:
		p.Y++
	case EAST:
		p.X++
	case WEST:
		p.X--
	}
}

func (p *Point) copyFrom(p2 *Point) {
	p.X = p2.X
	p.Y = p2.Y
}

func (p *Point) getNeighborPoints() []Point {
	points := make([]Point, 4)
	points[0] = Point{p.X, p.Y - 1}
	points[1] = Point{p.X, p.Y + 1}
	points[2] = Point{p.X + 1, p.Y}
	points[3] = Point{p.X - 1, p.Y}
	return points
}

func (p *Point) generateQueuePoints(queue *[]Point, vistedPoints map[Point]bool) {
	for _, point := range p.getNeighborPoints() {
		if visted, ok := vistedPoints[point]; !ok || !visted {
			addToQueue(queue, point)
		}
	}
}

func (p *Point) isPointNear(p2 *Point) bool {
	if p.X == p2.X && (p.Y-1 == p2.Y || p.Y+1 == p2.Y) {
		return true
	} else if p.Y == p2.Y && (p.X-1 == p2.X || p.X+1 == p2.X) {
		return true
	}
	return false
}

func (p *Point) getDirectionToPoint(p2 *Point) Direction {
	if p.Y+1 == p2.Y {
		return SOUTH
	} else if p.Y-1 == p2.Y {
		return NORTH
	} else if p.X+1 == p2.X {
		return EAST
	} else if p.X-1 == p2.X {
		return WEST
	}
	return NORTH
}

func printMap(fullMap map[Point]Tile, playerPosition Point, maxX int, maxY int, minX int, minY int) {
	arrayMap := make([][]Tile, maxY-minY+1)
	for i := range arrayMap {
		arrayMap[i] = make([]Tile, maxX-minX+1)
		for j := range arrayMap[i] {
			arrayMap[i][j] = UNKNOWN
		}
	}

	for key, value := range fullMap {
		arrayMap[key.Y-minY][key.X-minX] = value
	}

	arrayMap[playerPosition.Y-minY][playerPosition.X-minX] = PLAYER

	for _, row := range arrayMap {
		for _, value := range row {
			switch value {
			case WALL:
				fmt.Print("#")
			case EMPTY:
				fmt.Print(".")
			case OXYGEN:
				fmt.Print("o")
			case PLAYER:
				fmt.Print("D")
			case UNKNOWN:
				fmt.Print(" ")
			}
		}
		fmt.Print("\n")
	}
	fmt.Print("----------------------------\n")
}

func getNextInQueue(queue *[]Point) *Point {
	if len(*queue) == 0 {
		return nil
	}
	nextInQueue := (*queue)[0]
	*queue = (*queue)[1:]
	return &nextInQueue
}

func addToQueue(queue *[]Point, point Point) {
	*queue = append(*queue, Point{0, 0})
	copy((*queue)[1:], (*queue)[0:])
	(*queue)[0] = point
}

//func bfs(graph *map[Point][]Point) {
//}

func max(a int, b int) int {
	if a >= b {
		return a
	}
	return b
}

func maxDepth(graph *map[Point][]Point, pointToStart *Point) int {
	deepest := 0
	for _, point := range (*graph)[*pointToStart] {
		deepest = max(deepest, maxDepth(graph, &point))
	}
	return deepest + 1

}

func main() {
	var mainProgram []int
	file, err := os.Open("day15_input.txt")
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

	droidMap := make(map[Point]Tile)
	droidPosition := Point{0, 0}
	potentialMovePosition := Point{0, 0}
	droidMap[droidPosition] = EMPTY
	var maxX, maxY, minX, minY int

	queueToVisit := make([]Point, 0)
	visitedPoints := make(map[Point]bool)
	visitedPoints[droidPosition] = true
	droidPosition.generateQueuePoints(&queueToVisit, visitedPoints)
	pathToOrigin := make([]Point, 0)
	pointGraph := make(map[Point][]Point)
	movingBack := false
	//var oxygenPosition Point

	inputFunc := func() int {
		for {
			directionToMove, err := getMovement(&potentialMovePosition, &droidPosition,
				&queueToVisit, &visitedPoints, &movingBack, pathToOrigin)
			if err == nil {
				if potentialMovePosition.X > maxX {
					maxX = potentialMovePosition.X
				}
				if potentialMovePosition.Y > maxY {
					maxY = potentialMovePosition.Y
				}
				if potentialMovePosition.X < minX {
					minX = potentialMovePosition.X
				}
				if potentialMovePosition.Y < minY {
					minY = potentialMovePosition.Y
				}
				return int(*directionToMove)
			}
			// Map is complete
			//fmt.Println(maxDepth())
			//bfs(&pointGraph)
			panic(1)
		}

	}

	outputFunc := func(value int) {
		returnedTile := Tile(value)
		droidMap[potentialMovePosition] = returnedTile
		visitedPoints[potentialMovePosition] = true
		switch returnedTile {
		case EMPTY:
			if movingBack {
				pathToOrigin = pathToOrigin[0 : len(pathToOrigin)-1]
			} else {
				pathToOrigin = append(pathToOrigin, droidPosition)
				addToGraph(&pointGraph, &droidPosition, &potentialMovePosition)
				potentialMovePosition.generateQueuePoints(&queueToVisit, visitedPoints)
			}
			droidPosition.copyFrom(&potentialMovePosition)
		case OXYGEN:
			pathToOrigin = append(pathToOrigin, droidPosition)
			addToGraph(&pointGraph, &droidPosition, &potentialMovePosition)
			potentialMovePosition.generateQueuePoints(&queueToVisit, visitedPoints)

			droidPosition.copyFrom(&potentialMovePosition)
			fmt.Println("Found OXYGEN at ", droidPosition)
			fmt.Println(len(pathToOrigin))
			fmt.Println("")
		}
		printMap(droidMap, droidPosition, maxX, maxY, minX, minY)
	}
	intcode.RunProgram(mainProgram, inputFunc, outputFunc)
}

func connectionInConnections(connections []Point, connectionToCheck *Point) bool {
	foundConnection := false
	for _, connection := range connections {
		if connection == *connectionToCheck {
			foundConnection = true
			break
		}
	}
	return foundConnection
}

func addToGraph(graph *map[Point][]Point, p *Point, connectionPoint *Point) {
	if _, ok := (*graph)[*p]; !ok {
		(*graph)[*p] = make([]Point, 1)
		(*graph)[*p][0] = *connectionPoint
	} else {
		if !connectionInConnections((*graph)[*p], connectionPoint) {
			(*graph)[*p] = append((*graph)[*p], *connectionPoint)
		}
	}
}

func getMovement(potentialMovePosition *Point, droidPosition *Point,
	queue *[]Point, visted *map[Point]bool, moveBack *bool, pathToOrigin []Point) (*Direction, error) {

	/*
		reader := bufio.NewReader(os.Stdin)
		fmt.Print("Enter text: ")
		text, inputErr := reader.ReadString('\n')
		check(inputErr)

		//text := "h\n"

		var directionToMove Direction

		//vim movement
		switch strings.Trim(text, "\n") {
		case "h":
			directionToMove = WEST
		case "j":
			directionToMove = SOUTH
		case "k":
			directionToMove = NORTH
		case "l":
			directionToMove = EAST
		default:
			// raw number input
			inputInt, intErr := strconv.Atoi(strings.Trim(text, "\n"))
			if intErr != nil {
				return nil, intErr
			} else if inputInt < 1 || inputInt > 4 {
				return nil, errors.New("Error input")
			}
			directionToMove = Direction(inputInt)
		}
	*/
	var directionToMove Direction
	pointToVisit := getNextInQueue(queue)
	if pointToVisit == nil {
		return nil, errors.New("No more points left")
	}
	if droidPosition.isPointNear(pointToVisit) {
		directionToMove = droidPosition.getDirectionToPoint(pointToVisit)
		*moveBack = false
	} else {
		addToQueue(queue, *pointToVisit)
		directionToMove = droidPosition.getDirectionToPoint(&pathToOrigin[len(pathToOrigin)-1])
		*moveBack = true
	}

	potentialMovePosition.copyFrom(droidPosition)
	potentialMovePosition.moveDirection(directionToMove)

	return &directionToMove, nil
}
