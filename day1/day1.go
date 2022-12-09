package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	file, _ := os.Open("day1.txt")

	final, curr_sum := []int{}, 0

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		curr_val := scanner.Text()

		if curr_val == "" {
			final = append(final, curr_sum)
			curr_sum = 0
		} else {
			curr_int, _ := strconv.Atoi(curr_val)
			curr_sum = curr_sum + curr_int
		}
	}

	sort.Sort(sort.Reverse(sort.IntSlice(final)))

	fmt.Printf("PART 1: %d\n", final[0])
	fmt.Printf("PART 2: %d\n", (final[0] + final[1] + final[2]))
}
