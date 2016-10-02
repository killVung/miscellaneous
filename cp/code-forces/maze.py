sandbox = []
line = input()

wall = line.split(' ')[2]

for i in range(int(line.split(' ')[0])):
    sandbox.append([a for a in input()])

print(sandbox)
