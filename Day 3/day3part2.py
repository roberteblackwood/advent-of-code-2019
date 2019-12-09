def dothepath(wirepath):
    path = set()
    x = 0
    y = 0
    steps = {}
    # print(wirepath)
    totalmovements = 0
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
                totalmovements += 1
                point = (x, y)
                path.add(point)
                steps[point] = totalmovements
        elif direction == 'L':
            for x2 in range(0, positions):
                # print("Moving left 1")
                x -= 1
                totalmovements += 1
                point = (x, y)
                path.add(point)
                steps[point] = totalmovements
        elif direction == 'U':
            for y1 in range(0, positions):
                # print("Moving up 1")
                y += 1
                totalmovements += 1
                point = (x, y)
                path.add(point)
                steps[point] = totalmovements
        elif direction == 'D':
            for y2 in range(0, positions):
                # print("Moving down 1")
                y -= 1
                totalmovements += 1
                point = (x, y)
                path.add(point)
                steps[point] = totalmovements
        else:
            print("Bad things are happening...")
    return path, steps

def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    wirepaths = []
    for line in lines:
        wirepaths.append(line.strip().split(","))
        # print(wirepaths)

    path1 = dothepath(wirepaths[0])
    print(path1[1])
    path2 = dothepath(wirepaths[1])
    print(path2[1])
    shared = path1[0].intersection(path2[0])
    print(shared)
    answer = -1
    for point in shared:
        # print(point)
        tempsteps1 = path1[1][point]
        tempsteps2 = path2[1][point]
        tempsteps = tempsteps1 + tempsteps2
        # print(str(tempsum))
        if answer < 0 or tempsteps < answer:
            answer = tempsteps
            print("Found intersection " + str(point) + " with shorter path " + str(tempsteps) + " (" + str(tempsteps1) + " + " + str(tempsteps2) + ")")
    print("Answer: " + str(answer))


if __name__ == "__main__":
    main()
