with open("day1.txt") as file:
    final = []
    curr_sum = 0

    for line in [line.rstrip() for line in file.readlines()]:
        if line == "":
            final.append(curr_sum)
            curr_sum = 0
        else:
            curr_sum += int(line)

print(f"PART 1: {max(final)}")

sort = sorted(final)
final_three = sort[len(sort) - 3:]
print(f"PART 2: {sum(final_three)}")