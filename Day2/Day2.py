def first_star():
    with open('input.txt', 'r') as f:
        opcodes = f.read().split(',')
        opcodes = list(map(int, opcodes))
    
    # replace position 1
    opcodes[1] = 12

    # replace position 2
    opcodes[2] = 2

    current_opcode = opcodes[0]
    i = 0

    while current_opcode != 99:
        if current_opcode == 1:
            opcodes[opcodes[i+3]] = opcodes[opcodes[i+1]] + opcodes[opcodes[i+2]]

        elif current_opcode == 2:
            opcodes[opcodes[i+3]] = opcodes[opcodes[i+1]] * opcodes[opcodes[i+2]]

        i += 4
        current_opcode = opcodes[i]

    return opcodes[0]

def second_star():
    for j in range(0, 100):
        for k in range(0, 100):
            with open('input.txt', 'r') as f:
                opcodes = f.read().split(',')
                opcodes = list(map(int, opcodes))
            opcodes[1] = j
            opcodes[2] = k

            current_opcode = opcodes[0]
            i = 0

            while current_opcode != 99:
                if current_opcode == 1:
                    opcodes[opcodes[i+3]] = opcodes[opcodes[i+1]] + opcodes[opcodes[i+2]]

                elif current_opcode == 2:
                    opcodes[opcodes[i+3]] = opcodes[opcodes[i+1]] * opcodes[opcodes[i+2]]

                i += 4
                current_opcode = opcodes[i]

            if opcodes[0] == 19690720:
                return 100 * j + k

    

if __name__ == '__main__':
    print(first_star())
    print(second_star())
