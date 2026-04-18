text = "Python"

print(text)
print("The length of a string = " , len(text))
print(text[0])
print(text[-1])


name = "dhanush"

print(name.upper())
print(name.lower())
print(name.capitalize())
# print(name.isnumeric())

first = "Dhanush"
last = "Kumar"

full = first + " " + last + "hello"
print(full)


s = "Hello, World!"

print(s[0])          # H         → indexing
print(s[0:5])        # Hello     → slicing
print(s.upper())     # HELLO, WORLD!
print(s.replace("World", "Python"))  # Hello, Python!
print(len(s))        # 13
print(f"My name is {name}")  # f-string formatting




s = "hello World"
print(s.upper())        # "HELLO WORLD"
print(s.lower())        # "hello world"
print(s.title())        # "Hello World"
print(s.capitalize())   # "Hello world"
print(s.swapcase())     # "HELLO wORLD"

# Search & Check Methods
s = "hello world"
s.find("world")      # 6  (index), -1 if not found
s.index("world")     # 6  (raises ValueError if not found)
s.count("l")         # 3
s.startswith("hel")  # True
s.endswith("rld")    # True
s.in("ell" in s)     # True  ← using `in` operator


# Clean & Strip Methods
s = "  hello  "
s.strip()    # "hello"   (both sides)
s.lstrip()   # "hello  " (left only)
s.rstrip()   # "  hello" (right only)

s = "***hello***"
s.strip("*")  # "hello"  (strips specific chars)

# split and join
s = "apple,banana,cherry"
s.split(",")          # ["apple", "banana", "cherry"]
s.split(",", 1)       # ["apple", "banana,cherry"]  (max 1 split)

words = ["hello", "world"]
" ".join(words)       # "hello world"
"-".join(words)       # "hello-world"

# replace
s = "hello world world"
s.replace("world", "Python")       # "hello Python Python"
s.replace("world", "Python", 1)    # "hello Python world" (1 replacement)


