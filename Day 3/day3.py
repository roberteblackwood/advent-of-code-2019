def dothepath(wirepath):
    path = set()
    x = 0
    y = 0
    # print(wirepath)
    for move in wirepath:
        # print(move)
        direction = move[0]
        # print("direction: " + direction)
        positions = int(move[1::])
        # print("positions: " + str(positions))
        if direction == 'R':
            for x1 in range(0, positions):
                # print("Moving right 1")
                x += 1
                path.add((x, y))
        elif direction == 'L':
            for x2 in range(0, positions):
                # print("Moving left 1")
                x -= 1
                path.add((x, y))
        elif direction == 'U':
            for y1 in range(0, positions):
                # print("Moving up 1")
                y += 1
                path.add((x, y))
        elif direction == 'D':
            for y2 in range(0, positions):
                # print("Moving down 1")
                y -= 1
                path.add((x, y))
        else:
            print("Bad things are happening...")
    return path

def main():
    f = open("sample1.txt", "r")
    lines = f.readlines()
    wirepaths = []
    for line in lines:
        wirepaths.append(line.strip().split(","))
        # print(wirepaths)

    path1 = dothepath(wirepaths[0])
    # print(path1)
    path2 = dothepath(wirepaths[1])
    # print(path2)
    shared = path1.intersection(path2)
    print(shared)
    answer = -1
    for point in shared:
        # print(point)
        tempsum = abs(point[0]) + abs(point[1])
        # print(str(tempsum))
        if answer < 0 or tempsum < answer:
            answer = tempsum
            print("Found closer intersection at " + str(point) + " with sum " + str(answer))



if __name__ == "__main__":
    main()
