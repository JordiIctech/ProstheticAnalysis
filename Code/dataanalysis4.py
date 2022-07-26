import csv
import statistics

with open("Images\\Analyzed\\BP0.csv", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
print(data[0])
print(len(data))
del data[0]

# --------------------------------------------------------------------------------
x = 0
while x < len(data):  #Delete empty spaces

    if not data[x]:
        print(data[x])
        del data[x]

    else:
        x = x + 1

x1 = data[0]
y1 = data[1]
x2 = data[2]
y2 = data[3]

print(x1)
print(x2)
print(data)
print(len(data))

for i in range(0, len(x1)):  # Make strings into integers
    x1[i] = int(x1[i])

for i in range(0, len(y1)):
    y1[i] = int(y1[i])

for i in range(0, len(x2)):
    x2[i] = int(x2[i])

for i in range(0, len(y2)):
    y2[i] = int(y2[i])

print(x1)
print(x2)
print(data)
print(len(data))

# -----------------------------------------------------------


