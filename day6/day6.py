with open("day6.txt") as file:
    for line in file.readlines():
        curr = list(line.strip())
        for index, char in enumerate(curr):
            curr_inner = set([char, curr[index + 1], curr[index + 2], curr[index + 3]])
            if len(curr_inner) == 4:
                # One for zero indexing, 3 for 3 chars in front
                print(f"PART 1: {index + 4}")
                break


with open("day6.txt") as file:
    for line in file.readlines():
        curr = list(line.strip())
        for index, char in enumerate(curr):
            curr_inner = set([char, curr[index + 1], curr[index + 2], curr[index + 3], curr[index + 4], curr[index + 5], curr[index + 6], curr[index + 7], curr[index + 8], curr[index + 9], curr[index + 10], curr[index + 11], curr[index + 12], curr[index + 13]])
            if len(curr_inner) == 14:
                # One for zero indexing, 13 for 13 chars in front
                print(f"PART 2: {index + 14}")
                break