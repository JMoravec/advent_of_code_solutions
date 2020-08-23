package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	file, err := os.Open("day14_input.txt")
	check(err)
	defer file.Close()
	textInput := make([]string, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		textInput = append(textInput, scanner.Text())
	}
	err = scanner.Err()
	check(err)

	reactions := createReactionHash(textInput)
	actualOreNeeded := calculateAmountOfOre(1, reactions)
	fmt.Println(actualOreNeeded)
}

func stringToReaction(input string) Reaction {

	inputReactions := make([]OrderAmount, 0)

	re := regexp.MustCompile(`(.+) => (\d+ \w+)`)
	submatchall := re.FindStringSubmatch(input)
	outputReaction := stringToOrderAmount(submatchall[2])

	inputRe := regexp.MustCompile(`(\d+ \w+)`)
	inputsFound := inputRe.FindAllString(submatchall[1], -1)

	for _, value := range inputsFound {
		inputReactions = append(inputReactions, stringToOrderAmount(value))
	}

	return Reaction{inputReactions, outputReaction}
}

func stringToOrderAmount(input string) OrderAmount {
	splitString := strings.Split(input, " ")
	amount, err := strconv.Atoi(splitString[0])
	check(err)
	return OrderAmount{amount, Chemical(splitString[1])}
}

type ReactionHash map[Chemical]Reaction

func reactionsToMap(reactions []Reaction) ReactionHash {
	hashMap := make(map[Chemical]Reaction)

	for _, reaction := range reactions {
		hashMap[reaction.output.chem] = reaction
	}

	return ReactionHash(hashMap)
}

func addToStorage(storage map[Chemical]int, amount OrderAmount) {
	_, ok := storage[amount.chem]
	if ok {
		storage[amount.chem] += amount.amount
	} else {
		storage[amount.chem] = amount.amount
	}
}

func (order *OrderAmount) processOrder(reactions ReactionHash, storage map[Chemical]int) int {
	if order.chem == "ORE" {
		return order.amount
	}

	reaction := reactions[order.chem]

	if storage[order.chem] > 0 {
		if storage[order.chem] >= order.amount {
			storage[order.chem] -= order.amount
			return 0
		}
		order.amount -= storage[order.chem]
		storage[order.chem] = 0
		return order.processOrder(reactions, storage)
	}

	batches := (order.amount-1)/reaction.output.amount + 1
	newInputs := make([]OrderAmount, len(reaction.inputs))
	var oreNeeded int
	for i, input := range reaction.inputs {
		newInputs[i] = OrderAmount{batches * input.amount, input.chem}
		oreNeeded += newInputs[i].processOrder(reactions, storage)
	}

	if batches*reaction.output.amount-order.amount > 0 {
		storage[order.chem] += batches*reaction.output.amount - order.amount
	}

	return oreNeeded
}

func createReactionHash(textReactions []string) ReactionHash {
	allReactions := make([]Reaction, 0)
	for _, reaction := range textReactions {
		allReactions = append(allReactions, stringToReaction(reaction))
	}

	return reactionsToMap(allReactions)
}

func calculateAmountOfOre(amount int, reactions ReactionHash) int {
	oreNeeded := 0
	queue := make([]OrderAmount, 1)
	queue[0] = OrderAmount{amount, "FUEL"}
	storage := make(map[Chemical]int)
	oreNeeded = queue[0].processOrder(reactions, storage)
	return oreNeeded
}

type Chemical string

type OrderAmount struct {
	amount int
	chem   Chemical
}

type Reaction struct {
	inputs []OrderAmount
	output OrderAmount
}
