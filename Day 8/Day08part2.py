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

    flattened = []
    i = 0
    while i < width * height:
        flattened.append(5)
        i += 1
    i = len(layers) - 1
    while i >= 0:
        print("i: " + str(i))
        j = 0
        while j < len(layers[i]):
            print("j: " + str(j))
            if layers[i][j] != 2:
                flattened[j] = layers[i][j]
            j += 1
        i -= 1
    i = 0
    print(flattened)
    while i < len(flattened):
        x = 0
        row = ""
        while x < width:
            if flattened[i] == 0:
                row += ' '
            elif flattened[i] == 1:
                row += '█'
            x += 1
            i += 1
        print(row)





if __name__ == '__main__':
    main()