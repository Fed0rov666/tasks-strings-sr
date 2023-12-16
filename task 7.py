N = int(input())
positions = []
for i in range(N):
    line = input()
    if 'кот' in line:
        index = line.find('кот') + 1
        positions.append((i+1, index))

for pos in positions:
    print(pos[0], pos[1])
