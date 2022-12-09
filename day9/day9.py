import re

curr_poss_h = [0, 0]
curr_poss_t = [0, 0]

visited_loc_t = set([f"{curr_poss_t[0]}-{curr_poss_t[1]}"])

def apply_orientation(orientation, poss):
    # poss = [x, y]
    if orientation == "L":
        return [poss[0] - 1, poss[1]]
    elif orientation == "R":
        return [poss[0] + 1, poss[1]]
    elif orientation == "U":
        return [poss[0], poss[1] + 1]
    elif orientation == "D":
        return [poss[0], poss[1] - 1]

with open("day9.txt") as file:
    for index, line in enumerate(file.readlines()):
        curr = line.strip()

        x = re.search("(\w) (\d*)", curr)

        orientation = x.group(1)
        moves = int(x.group(2))

        # print(f"\nSTARTING {orientation} {moves}")

        # go_next = ""

        for i in range(moves):
            next_poss_h = apply_orientation(orientation, curr_poss_h)

            if abs(next_poss_h[0] - curr_poss_t[0]) > 1 or  abs(next_poss_h[1] - curr_poss_t[1]) > 1:
                # outside box
                curr_poss_t = curr_poss_h

            # try diagonals first
            # if (next_poss_h[0] - curr_poss_t[0] == -1 and next_poss_h[1] - curr_poss_t[1] == 1) or go_next == "LU":
            #     # move to the left and up
            #     if go_next != "":
            #         curr_poss_t[0] -= 1
            #         curr_poss_t[1] += 1

            # elif (next_poss_h[0] - curr_poss_t[0] == -1 and next_poss_h[1] - curr_poss_t[1] == -1) or go_next == "LD":
            #     # move to the left and down
            #     if go_next != "":
            #         curr_poss_t[0] -= 1
            #         curr_poss_t[1] -= 1

            #         go_next = ""
            #     else:
            #         go_next = "LD"
            # elif (next_poss_h[0] - curr_poss_t[0] == 1 and next_poss_h[1] - curr_poss_t[1] == -1) or go_next == "RD":
            #     # move to the right and down
            #     if go_next != "":
            #         curr_poss_t[0] += 1
            #         curr_poss_t[1] -= 1

            #         go_next = ""
            #     else:
            #         go_next = "RD"
            # elif (next_poss_h[0] - curr_poss_t[0] == 1 and next_poss_h[1] - curr_poss_t[1] == 1) or go_next == "RU":
            #     # move to the right and up
            #     if go_next != "":
            #         curr_poss_t[0] += 1
            #         curr_poss_t[1] += 1

            #         go_next = ""
            #     else:
            #         go_next = "RU"
            # # now try normal moves
            # elif curr_poss_h[0] - curr_poss_t[0] == -1 and next_poss_h[0] - curr_poss_h[0] != 1:
            #     # move to the left (if H is NOT moving to right)
            #     curr_poss_t[0] -= 1
            #     go_next = ""
            # elif curr_poss_h[0] - curr_poss_t[0] == 1 and next_poss_h[0] - curr_poss_h[0] != -1:
            #     # move to the right
            #     curr_poss_t[0] += 1
            #     go_next = ""
            # elif curr_poss_h[1] - curr_poss_t[1] == 1 and next_poss_h[1] - curr_poss_t[1] != 1:
            #     # move up
            #     curr_poss_t[1] += 1
            #     go_next = ""
            # elif curr_poss_h[1] - curr_poss_t[1] == -1 and next_poss_h[1] - curr_poss_t[1] != -1:
            #     # move down
            #     curr_poss_t[1] -= 1
            #     go_next = ""
            # else:
            #     go_next = ""

            curr_poss_h = next_poss_h

            # print(f"Move: {orientation} {moves}, num: {i} H: {curr_poss_h} T: {curr_poss_t}")

            visited_loc_t |= set([f"{curr_poss_t[0]}-{curr_poss_t[1]}"])

# print(visited_loc_t)
print(f"PART 1: {len(visited_loc_t)}")

import re

curr_poss_h = [0, 0]
curr_poss_1_9 = [(0,0)] * 9
hist_poss_1_9 = [{(0,0)} for _ in range(9)]

def sign(num):
    return 1 if num > 0 else -1

def apply_orientation(orientation, poss):
    # poss = [x, y]
    if orientation == "L":
        return [poss[0] - 1, poss[1]]
    elif orientation == "R":
        return [poss[0] + 1, poss[1]]
    elif orientation == "U":
        return [poss[0], poss[1] + 1]
    elif orientation == "D":
        return [poss[0], poss[1] - 1]

with open("day9.txt") as file:
    for index, line in enumerate(file.readlines()):
        curr = line.strip()

        x = re.search("(\w) (\d*)", curr)

        orientation = x.group(1)
        moves = int(x.group(2))

        # print(f"\nSTARTING {orientation} {moves}")

        # go_next = ""

        for i in range(moves):
            curr_poss_h = apply_orientation(orientation, curr_poss_h)

            last_poss_prev = curr_poss_h

            for i, history_t in enumerate(hist_poss_1_9):
                x, y = curr_poss_1_9[i][0], curr_poss_1_9[i][1]
                dx, dy = x - last_poss_prev[0], y - last_poss_prev[1]
                
                if (abs(dx) > 0 and abs(dy) > 1) or (abs(dx) > 1 and abs(dy) > 0):
                    # diagonal prev or need to jump
                    curr_poss_1_9[i] = x - sign(dx), y - sign(dy)
                elif abs(dx) > 1:
                    # left or right prev
                    curr_poss_1_9[i] = x - sign(dx), y
                elif abs(dy) > 1:
                    # up or down prev
                    curr_poss_1_9[i] = x, y - sign(dy)
        
                last_poss_prev = curr_poss_1_9[i]
                history_t.add(curr_poss_1_9[i])

        #     curr_poss_head = curr_poss_h
        #     next_poss_head = next_poss_h

        #     curr_poss_tail = curr_poss_1_9[0]

        #     for i in range(len(curr_poss_1_9)):
        #         temp_curr_head = curr_poss_tail.copy()

        #         if abs(next_poss_head[0] - curr_poss_tail[0]) > 1 or abs(next_poss_head[1] - curr_poss_tail[1]) > 1:
        #             # outside box
        #             curr_poss_tail = curr_poss_head

        #         curr_poss_1_9[i] = curr_poss_tail

        #         curr_poss_head = temp_curr_head
        #         next_poss_head = curr_poss_tail

        #         if i != 8:
        #             curr_poss_tail = curr_poss_1_9[i + 1]

            # last_item_curr = curr_poss_h
            # last_item_next = next_poss_h

            # curr_poss_1_9_copy = curr_poss_1_9.copy()

            # lastChanged = False
            # lastChangedCoords = None

            # for index, item in enumerate(curr_poss_1_9_copy):
            #     curr_poss = curr_poss_1_9[index]

            #     print(index + 1, curr_poss, last_item_curr, last_item_next, lastChanged)
            #     if abs(last_item_next[0] - curr_poss[0]) > 1 or abs(last_item_next[1] - curr_poss[1]) > 1:
            #         # outside box
            #         # print("yes", lastChanged)
            #         if not lastChanged:
            #             curr_poss_1_9[index] = last_item_curr
            #         else:
            #             # previous was a diagonal, which way did it jump?
            #             # if abs(last_item_curr[0] - curr_poss[0]) == 1 and abs(last_item_curr[1] - curr_poss[1]) == 1:
            #             if abs(curr_poss_1_9[index - 1][0] - curr_poss[0]) > 1 or abs(curr_poss_1_9[index - 1][1] - curr_poss[1]) > 1:
            #                 curr_poss_1_9[index] = [curr_poss[0] + lastChangedCoords[0], curr_poss[1] + lastChangedCoords[1]]
            #             else:
            #                 curr_poss_1_9[index] = last_item_curr
            #                 lastChanged = False
            #                 lastChangedCoords = None

            #         # we went on a diagonal, record!
            #         if abs(curr_poss_1_9[index][0] - curr_poss[0]) == 1 and abs(curr_poss_1_9[index][1] - curr_poss[1]) == 1:
            #             lastChanged = True
            #             lastChangedCoords = [curr_poss_1_9[index][0] - curr_poss[0], curr_poss_1_9[index][1] - curr_poss[1]]
            #     else:
            #         lastChanged = False

            #     last_item_curr = curr_poss
            #     last_item_next = curr_poss_1_9[index]

            # # try diagonals first
            # # if (next_poss_h[0] - curr_poss_t[0] == -1 and next_poss_h[1] - curr_poss_t[1] == 1) or go_next == "LU":
            # #     # move to the left and up
            # #     if go_next != "":
            # #         curr_poss_t[0] -= 1
            # #         curr_poss_t[1] += 1

            # # elif (next_poss_h[0] - curr_poss_t[0] == -1 and next_poss_h[1] - curr_poss_t[1] == -1) or go_next == "LD":
            # #     # move to the left and down
            # #     if go_next != "":
            # #         curr_poss_t[0] -= 1
            #         curr_poss_t[1] -= 1

            #         go_next = ""
            #     else:
            #         go_next = "LD"
            # elif (next_poss_h[0] - curr_poss_t[0] == 1 and next_poss_h[1] - curr_poss_t[1] == -1) or go_next == "RD":
            #     # move to the right and down
            #     if go_next != "":
            #         curr_poss_t[0] += 1
            #         curr_poss_t[1] -= 1

            #         go_next = ""
            #     else:
            #         go_next = "RD"
            # elif (next_poss_h[0] - curr_poss_t[0] == 1 and next_poss_h[1] - curr_poss_t[1] == 1) or go_next == "RU":
            #     # move to the right and up
            #     if go_next != "":
            #         curr_poss_t[0] += 1
            #         curr_poss_t[1] += 1

            #         go_next = ""
            #     else:
            #         go_next = "RU"
            # # now try normal moves
            # elif curr_poss_h[0] - curr_poss_t[0] == -1 and next_poss_h[0] - curr_poss_h[0] != 1:
            #     # move to the left (if H is NOT moving to right)
            #     curr_poss_t[0] -= 1
            #     go_next = ""
            # elif curr_poss_h[0] - curr_poss_t[0] == 1 and next_poss_h[0] - curr_poss_h[0] != -1:
            #     # move to the right
            #     curr_poss_t[0] += 1
            #     go_next = ""
            # elif curr_poss_h[1] - curr_poss_t[1] == 1 and next_poss_h[1] - curr_poss_t[1] != 1:
            #     # move up
            #     curr_poss_t[1] += 1
            #     go_next = ""
            # elif curr_poss_h[1] - curr_poss_t[1] == -1 and next_poss_h[1] - curr_poss_t[1] != -1:
            #     # move down
            #     curr_poss_t[1] -= 1
            #     go_next = ""
            # else:
            #     go_next = ""

            # curr_poss_h = next_poss_h

            # print(f"Move: {orientation} {moves}, num: {i} H: {curr_poss_h} T: {curr_poss_1_9}")

            # visited_loc_t |= set([f"{curr_poss_1_9[8][0]}+{curr_poss_1_9[8][1]}"])

# print(hist_poss_1_9[-1])
print(f"PART 2: {len(hist_poss_1_9[-1])}")