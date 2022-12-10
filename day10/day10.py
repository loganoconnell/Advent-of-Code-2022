import re

cycle = 1
x = 1
signal_strength = 0

arr = [["." for _ in range(40)] for _ in range(6)]

def print_crt():
    global arr
    
    for line in arr:
        print("".join(line))

def take_measurements():
    global x, signal_strength, cycle

    if cycle % 40 == 20:
        # print(f"TAKING MEASUREMENTS AT CYCLE: {cycle}, x={x}")
        signal_strength += cycle * x

def draw_crt_pixel():
    global x, arr, cycle

    crt_pos = (cycle - 1) % 40
    line = int((cycle - 1) / 40)
    # print(cycle, line, crt_pos, x)

    if x < 0 or x > 39:
        return
    else:
        # is sprite where it should be?
        if crt_pos == x or crt_pos == x + 1 or crt_pos == x - 1:
            # sprite is within view of CRT
            # print("HERE", line, crt_pos)
            # print(arr[line][crt_pos])
            arr[line][crt_pos] = "#"
            # print(arr[line][crt_pos])

# print_crt()

with open("day10.txt") as file:
    for line in file.readlines():
        curr = line.strip()

        # print(f"STARTING CYCLE: {cycle}")

        if curr.startswith("noop"):
            # start noop cycle
            
            # take measurements
            take_measurements()
            draw_crt_pixel()

            # end noop cycle
        else:
            # must be addx
            match = re.search("addx (-?\d*)", curr)
            to_add = int(match.group(1))

            # take measurements during first cycle
            take_measurements()
            draw_crt_pixel()

            cycle += 1
            # print(f"STARTING CYCLE (2): {cycle}")

            # take measurements during second cycle
            take_measurements()
            draw_crt_pixel()

            # update x post second cycle
            x += to_add

        # print(f"ENDING CYCLE: {cycle}")
        cycle += 1

print(f"PART 1: {signal_strength}")

print_crt()