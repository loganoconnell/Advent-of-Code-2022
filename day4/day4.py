total_part1 = 0
total_part2 = 0

with open("day4.txt") as file:
    for line in file.readlines():
        parts = line.strip().split(",")
        first, second = parts[0], parts[1]

        first_parts = first.split("-")
        first_first, first_second = int(first_parts[0]), int(first_parts[1])
        second_parts = second.split("-")
        second_first, second_second = int(second_parts[0]), int(second_parts[1])

        if first_first <= second_first and first_second >= second_second:
            total_part1 += 1
        elif second_first <= first_first and second_second >= first_second:
            total_part1 += 1

        part2 = set(range(first_first, first_second + 1))
        part2 = part2.intersection(range(second_first, second_second + 1))
        
        if list(part2) != []:
            total_part2 += 1

print(f"PART 1: {total_part1}")
print(f"PART 2: {total_part2}")