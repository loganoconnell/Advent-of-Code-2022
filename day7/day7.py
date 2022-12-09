import re

previous_lines = []

file_system = {
    "fol_name": "",
    "subfolders": [],
    "size": 0
}

global_fs = file_system
global_fs["fol_name"] = "/"

def execute(lines, curr_fs):
    global last_curr
    global total

    if lines[0] == "cd /": return curr_fs
    elif lines[0] == "ls":
        for line in lines[1:]:
            if line.startswith("dir"):
                new_fs = file_system.copy()
                new_fs["fol_name"] = line[4:]
                new_fs["subfolders"] = []
                new_fs["size"] = 0
                curr_fs["subfolders"] += [new_fs]
            else:
                x = re.search("(\d*).*", line)
                curr_fs["size"] += int(x.group(1))

        # if curr_fs["size"] <= 100000:
            # total += 1

    elif lines[0].startswith("cd .."):
        curr_fs = last_curr.pop()
    elif lines[0].startswith("cd"):
        dir = lines[0][3:]
        last_curr.append(curr_fs)
        curr_fs = [folder for folder in curr_fs["subfolders"] if folder.get("fol_name") == dir][0]

    return curr_fs

curr_fs = global_fs
last_curr = [curr_fs]
total = 0

with open("day7.txt") as file:
    for line in file.readlines():

        curr = line.strip()
        
        if curr.startswith("$"):
            # we found a command, process other commands
            if previous_lines != []:
                curr_fs = execute(previous_lines, curr_fs)

                previous_lines.clear()

            previous_lines.append(curr[2:])
        else:
            previous_lines.append(curr)

    if previous_lines != []:
        curr_fs = execute(previous_lines, curr_fs)


def recursive_helper(folder):
    global total
    
    if folder["subfolders"] == []:
        if folder["size"] <= 100000:
            total += folder["size"]

        return folder["size"]
    else:
        x = sum(recursive_helper(folder) for folder in folder["subfolders"])
        if x + folder["size"] <= 100000:
            total += x + folder["size"]

        return x + folder["size"]

curr_folder = recursive_helper(global_fs)

print(f"PART 1: {total}")

total_space = 70000000
needed_for_update = 30000000
curr_disk_size = curr_folder
available_disk_size = total_space - curr_disk_size
needed = needed_for_update - available_disk_size

import sys
min_folder_size = sys.maxsize

def recursive_helper2(folder):
    global total
    global min_folder_size
    
    if folder["subfolders"] == []:
        x = folder["size"]
        if x >= needed and x < min_folder_size:
            min_folder_size = x

        return folder["size"]
    else:
        x = sum(recursive_helper2(folder) for folder in folder["subfolders"])
        x += folder["size"] if folder["fol_name"] != "/" else 0
        if x >= needed and x < min_folder_size:
            min_folder_size = x

        return x

curr_folder = recursive_helper2(global_fs)

print(f"PART 2: {min_folder_size}")