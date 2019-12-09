def main():
    width = 25
    height = 6
    f = open("input.txt", "r")
    line = f.readline()
    linecounter = 0
    layers = {}
    layer = 0
    lowestzerocount = 1000000
    lowestzerolayer = 1000000
    while linecounter < len(line) and line[linecounter] != '\n':
        layers[layer] = []
        zerocount = 0

        y = 0
        while y < height:
            x = 0
            while x < width:
                print(linecounter)
                num = int(line[linecounter])
                layers[layer].append(num)
                if num == 0:
                    zerocount = zerocount + 1
                linecounter = linecounter + 1
                x = x + 1
            y = y + 1
        if lowestzerocount > zerocount:
            lowestzerocount = zerocount
            lowestzerolayer = layer
        layer = layer + 1
    print(layers)
    print(str(lowestzerocount) + " at " + str(lowestzerolayer))
    ones = 0
    twos = 0
    i = 0
    while i < len(layers[lowestzerolayer]):
        if layers[lowestzerolayer][i] == 1:
            ones += 1
        if layers[lowestzerolayer][i] == 2:
            twos += 1
        i += 1
    print(ones * twos)



if __name__ == '__main__':
    main()