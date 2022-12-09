package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, _ := os.Open("day2.txt")

	scanner := bufio.NewScanner(file)

	vals := map[string]int{
		"A": 1,
		"B": 2,
		"C": 3,
		"X": 1,
		"Y": 2,
		"Z": 3,
	}

	loss := 0
	draw := 3
	win := 6

	total := 0

	for scanner.Scan() {
		curr_line := scanner.Text()
		opp := string(curr_line[0])
		me := string(curr_line[2])

		total += vals[me]

		if opp == "A" {
			if me == "X" {
				// draw
				total += draw
			} else if me == "Y" {
				// win
				total += win
			} else {
				// loss
				total += loss
			}
		} else if opp == "B" {
			if me == "X" {
				// loss
				total += loss
			} else if me == "Y" {
				// draw
				total += draw
			} else {
				// win
				total += win
			}
		} else {
			// opp has scissors
			if me == "X" {
				// win
				total += win
			} else if me == "Y" {
				// loss
				total += loss
			} else {
				// draw
				total += draw
			}
		}
	}

	fmt.Printf("PART 1: %d\n", total)

	file, _ = os.Open("day2.txt")

	scanner = bufio.NewScanner(file)

	total = 0

	for scanner.Scan() {
		curr_line := scanner.Text()
		opp := string(curr_line[0])
		me := string(curr_line[2])

		if opp == "A" {
			if me == "X" {
				// need scissors to lose
				total += vals["Z"] + loss
			} else if me == "Y" {
				// need rock to draw
				total += vals["X"] + draw
			} else {
				// need paper to win
				total += vals["Y"] + win
			}
		} else if opp == "B" {
			if me == "X" {
				// need rock to lose
				total += vals["X"] + loss
			} else if me == "Y" {
				// need paper to draw
				total += vals["Y"] + draw
			} else {
				// need scissors to win
				total += vals["Z"] + win
			}
		} else {
			// opp has scissors
			if me == "X" {
				// need paper to lose
				total += vals["Y"] + loss
			} else if me == "Y" {
				// need scissors to draw
				total += vals["Z"] + draw
			} else {
				// need rock to win
				total += vals["X"] + win
			}
		}
	}

	fmt.Printf("PART 2: %d\n", total)
}
