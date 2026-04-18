import os

# Get the folder where this python script is saved
current_folder = os.path.dirname(__file__)
# Create the full path to notes.txt
notes_file = os.path.join(current_folder, "notes.txt")

# Way 1 — read everything at once (most common)
with open(notes_file, "r") as f:
    content = f.read()
print(content)
# Hello from line 1
# Hello from line 2
# Hello from line 3


# Way 2 — read one line at a time (good for big files)
with open(notes_file, "r") as f:
    for line in f:
        print(line.strip())    # .strip() removes the \n at the end
# Hello from line 1
# Hello from line 2
# Hello from line 3


# Way 3 — read into a list (one item per line)
with open(notes_file, "r") as f:
    lines = f.readlines()
print(lines)
# ["Hello from line 1\n", "Hello from line 2\n", "Hello from line 3\n"]
print(lines[0])   # Hello from line 1



# Creates the file if it doesn't exist
# OVERWRITES if it already exists ⚠️
with open(notes_file, "w") as f:
    f.write("My first line\n")
    f.write("My second line\n")

with open(notes_file, "r") as f:
    lines = f.readlines()
print(lines)



# json
import json

my_data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding"]
}

# ── SAVE (freeze to file) ──────────────────────
with open("user.json", "w") as f:
    json.dump(my_data, f, indent=4)
# Creates user.json on your computer ✅


# ── LOAD (unfreeze from file) ──────────────────
with open("user.json", "r") as f:
    loaded = json.load(f)

print(loaded["name"])        # Alice
print(loaded["hobbies"][0])  # reading
