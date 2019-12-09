def dothepath(wirepath):
    path = {}
    for move in path[0]:
        if move[0]
    print(path)

def main():
    f = open("sample1.txt", "r")
    lines = f.readlines()
    wirepaths = []
    for line in lines:
        wirepaths.append(line.strip().split(","))

    dothepath(wirepaths[0])
    dothepath(wirepaths[1])


if __name__ == "__main__":
    main()
