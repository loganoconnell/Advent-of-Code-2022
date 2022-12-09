import re

arr = [
    list("WDGBHRV"),
    list("JNGCRF"),
    list("LSFHDNJ"),
    list("JDSV"),
    list("SHDRQWNV"),
    list("PGHCM"),
    list("FJBGLZHC"),
    list("SJR"),
    list("LGSRBNVM")
]

arr2 = [
    list("WDGBHRV"),
    list("JNGCRF"),
    list("LSFHDNJ"),
    list("JDSV"),
    list("SHDRQWNV"),
    list("PGHCM"),
    list("FJBGLZHC"),
    list("SJR"),
    list("LGSRBNVM")
]

total_part1 = ""
total_part2 = ""

with open("day5.txt") as file:
    for index, line in enumerate(file.readlines()):
        if index < 10:
            continue

        else:
            curr = line.strip()
            x = re.search("move (\d*) from (\d*) to (\d*)", curr)
            num = int(x.group(1))
            start = int(x.group(2))
            end = int(x.group(3))

            add = arr[start - 1][len(arr[start - 1]) - num:]

            arr[start - 1] = arr[start - 1][:len(arr[start - 1]) - num]

            for item in add[::-1]:
                arr[end - 1].append(item)

    for list in arr:
        total_part1 += list[len(list) - 1:][0]

print(f"PART 1: {total_part1}")

with open("day5.txt") as file:
    for index, line in enumerate(file.readlines()):
        if index < 10:
            continue

        else:
            curr = line.strip()
            x = re.search("move (\d*) from (\d*) to (\d*)", curr)
            num = int(x.group(1))
            start = int(x.group(2))
            end = int(x.group(3))

            add = arr2[start - 1][len(arr2[start - 1]) - num:]

            arr2[start - 1] = arr2[start - 1][:len(arr2[start - 1]) - num]

            for item in add:
                arr2[end - 1].append(item)

    for list in arr2:
        total_part2 += list[len(list) - 1:][0]

print(f"PART 2: {total_part2}")