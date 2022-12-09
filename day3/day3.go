package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func alphaNum(letter rune) int {
	char := int(letter)
	char -= 64

	if unicode.IsLower(letter) {
		return char - 32
	} else {
		return char + 26
	}
}

func intersection(a, b []string) (c []string) {
	m := make(map[string]bool)

	for _, item := range a {
		m[item] = true
	}

	for _, item := range b {
		if _, ok := m[item]; ok {
			c = append(c, item)
		}
	}
	return
}

func main() {
	file, _ := os.Open("day3.txt")

	scanner := bufio.NewScanner(file)

	total := 0

	for scanner.Scan() {
		curr_line := scanner.Text()

		first_half := curr_line[len(curr_line)/2:]
		second_half := curr_line[:len(curr_line)/2]

		chars_in_first_half := []string{}
		chars_in_second_half := []string{}

		for i := 0; i < len(first_half); i++ {
			in_first := false
			for j := 0; j < len(chars_in_first_half); j++ {
				if string(first_half[i]) == string(chars_in_first_half[j]) {
					in_first = true
				}
			}

			if !in_first {
				chars_in_first_half = append(chars_in_first_half, string(first_half[i]))
			}

			in_second := false
			for j := 0; j < len(chars_in_second_half); j++ {
				if string(second_half[i]) == string(chars_in_second_half[j]) {
					in_second = true
				}
			}

			if !in_second {
				chars_in_second_half = append(chars_in_second_half, string(second_half[i]))
			}
		}

		// fmt.Println(intersection(chars_in_first_half, chars_in_second_half))

		diff := []rune(intersection(chars_in_first_half, chars_in_second_half)[0])[0]
		// fmt.Println(alphaNum(diff))

		total += alphaNum(diff)
	}

	fmt.Printf("PART 1: %d\n", total)

	file, _ = os.Open("day3.txt")

	scanner = bufio.NewScanner(file)

	total = 0
	curr_count := 0
	list_common_strings := [][]string{}

	for scanner.Scan() {
		curr_line := scanner.Text()
		// fmt.Println(curr_line)

		if curr_count == 3 {
			// == 2, we have 3 strings
			// fmt.Println(list_common_strings)

			diff1 := intersection(list_common_strings[0], list_common_strings[1])
			// fmt.Println(diff1)
			diff2 := intersection(diff1, list_common_strings[2])
			// fmt.Println(diff2)
			diff3 := []rune(diff2[0])[0]
			// fmt.Println(alphaNum(diff3))

			total += alphaNum(diff3)
			// fmt.Println(total)
			list_common_strings = [][]string{}
			curr_count = 0
		}

		chars_in_line := []string{}

		for i := 0; i < len(curr_line); i++ {
			inside := false
			for j := 0; j < len(chars_in_line); j++ {
				if string(curr_line[i]) == string(chars_in_line[j]) {
					inside = true
				}
			}

			if !inside {
				chars_in_line = append(chars_in_line, string(curr_line[i]))
			}
		}

		list_common_strings = append(list_common_strings, chars_in_line)

		curr_count += 1
	}

	if curr_count == 3 {
		// == 2, we have 3 strings
		// fmt.Println(list_common_strings)

		diff1 := intersection(list_common_strings[0], list_common_strings[1])
		// fmt.Println(diff1)
		diff2 := intersection(diff1, list_common_strings[2])
		// fmt.Println(diff2)
		diff3 := []rune(diff2[0])[0]
		// fmt.Println(alphaNum(diff3))

		total += alphaNum(diff3)
		// fmt.Println(total)
		list_common_strings = [][]string{}
		curr_count = 0
	}

	fmt.Printf("PART 2: %d\n", total)
}
