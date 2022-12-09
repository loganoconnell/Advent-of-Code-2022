matrix = []

with open("day8.txt") as file:
    for index, line in enumerate(file.readlines()):
        curr = line.strip()
        matrix.append([])
        
        for tree in list(curr):
            matrix[index].append(int(tree))

total = 0

for row, tree_row in enumerate(matrix):
    for col, tree in enumerate(tree_row):
        if row == 0 or row == len(matrix) - 1:
            # on horizontal edge
            total += 1
        elif col == 0 or col == len(tree_row) - 1:
            # on vertical edge
            total += 1
        else:
            # left, right, up, down
            cols_for_rows_above = [row[col] for row in matrix[:row]]
            cols_for_rows_below = [row[col] for row in matrix[row + 1:]]
            if max(matrix[row][:col]) < tree or max(matrix[row][col + 1:]) < tree or max(cols_for_rows_above) < tree or max(cols_for_rows_below) < tree:
                total += 1

print(f"PART 1: {total}")

total2 = 0

for row, tree_row in enumerate(matrix):
    for col, tree in enumerate(tree_row):
        if row == 0 or row == len(matrix) - 1:
            # on horizontal edge
            continue
        elif col == 0 or col == len(tree_row) - 1:
            continue
        else:
            # left, right, up, down
            rows_for_cols_left = matrix[row][:col][::-1]
            rows_for_cols_right = matrix[row][col + 1:]
            cols_for_rows_above = [row[col] for row in matrix[:row]][::-1]
            cols_for_rows_below = [row[col] for row in matrix[row + 1:]]

            score = []
            curr_score = 0
            for list in [rows_for_cols_left, rows_for_cols_right, cols_for_rows_above, cols_for_rows_below]:
                for tree_inner in list:
                    if tree_inner < tree:
                        curr_score += 1
                    else:
                        curr_score += 1
                        break

                score.append(curr_score)
                curr_score = 0

            final_score = 1

            for score in score:
                final_score *= score

            if final_score > total2:
                total2 = final_score

            # if max(]) < tree or max() < tree or max(cols_for_rows_above) < tree or max(cols_for_rows_below) < tree:
            #     print(f"FOUND HERE: {tree_row} {tree}")
            #     total += 1

print(f"PART 2: {total2}")