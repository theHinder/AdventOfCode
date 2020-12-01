f = open("input1.txt", "r")
expense = []
for x in f:
  expense.append(int(x))

for x in expense:
    for y in expense:
        if x + y == 2020:
            print(x * y)

for x in expense:
    for y in expense:
        for z in expense:
            if x + y + z == 2020:
                print(x * y * z)