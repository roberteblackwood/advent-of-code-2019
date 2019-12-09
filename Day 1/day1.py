def computefuel(mass):
    fuel = (mass // 3) - 2
    print("Processing recursively: " + str(mass) + " -> " + str(fuel))
    if fuel > 0:
        return fuel + computefuel(fuel)
    return 0


def main():
    s = 0
    f = open("input1.txt", "r")
    lines = f.readlines()
    for line in lines:
        mass = int(line)
        fuel = computefuel(mass)
        s = s + fuel
        # print("Processed: " + str(mass) + " - " + str(fuel))
    print("***Sum: " + str(s))


if __name__ == "__main__":
    main()
