import copy
def doTheThing(instructions):
    i = 0
    while i < len(instructions):
        op = int(instructions[i])
        if op == 99:
            break
        address1 = int(instructions[i + 1])
        address2 = int(instructions[i + 2])
        address3 = int(instructions[i + 3])
        operand1 = int(instructions[address1])
        operand2 = int(instructions[address2])
        if op == 1:
            instructions[address3] = str(operand1 + operand2)
        elif op == 2:
            instructions[address3] = str(operand1 * operand2)
        else:
            print("WTH?!" + str(i))
        i = i + 4
    
def findSolution(instructions, target):
    for noun in range(0,100):
        for verb in range(0,100):
            instructionsCopy = copy.deepcopy(instructions)
            instructionsCopy[1] = str(noun)
            instructionsCopy[2] = str(verb)
            doTheThing(instructionsCopy)
            if target == int(instructionsCopy[0]):
                print("Found it: noun = " + str(noun) + ", verb = " + str(verb))
                print("100 * noun + verb = " + str(100 * noun + verb))
                return True
    return False
def main():
    f = open("C:\\Users\\rblackwood\\Documents\\Advent of Code\\Day 2\\input2.txt","r")
    instructions = f.readline().split(",")
    doTheThing(instructions)
    print("After doing the thing: " + ",".join(instructions))

    # if findSolution(instructions, 19690720):
    #     print("MISSION ACCOMPLISHED!")
    
if __name__ == "__main__":
    main()