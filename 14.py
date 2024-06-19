lines = []
print("Enter multiple lines of text (Enter an empty line to stop):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("You entered:")
for line in lines:
    print(line)
