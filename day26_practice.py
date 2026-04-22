# Day 26 - Nested Loops

# 1. Constant pattern
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()


# 2. Increasing pattern
for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()


# 3. Decreasing pattern
for i in range(3, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# 4. Number pattern (j)
for i in range(3):
    for j in range(3):
        print(j, end=" ")
    print()


# 5. Decreasing number pattern
for i in range(3):
    for j in range(3 - i):
        print(j, end=" ")
    print()


# 6. Character pattern
letters = ["A", "B", "C"]
for i in range(1, 4):
    for j in range(i):
        print(letters[j], end=" ")
    print()