# This function retrieves the value based on the parameter mode
def get_param(data, mode, index):
    if mode == 0:  # position mode
        return data[data[index]]
    elif mode == 1:  # immediate mode
        return data[index]
    else:
        raise ValueError(f"Unknown mode: {mode}")

def intcode(data, input_value):
    i = 0
    while i < len(data):
        opcode = data[i] % 100  # only the last two digits are the opcode
        modes = [data[i] // 100 // 10 ** n % 10 for n in range(3)]  # extract parameter modes

        if opcode == 99:  # halt
            break
        elif opcode == 1:  # addition
            data[data[i + 3]] = get_param(data, modes[0], i + 1) + get_param(data, modes[1], i + 2)
            i += 4
        elif opcode == 2:  # multiplication
            data[data[i + 3]] = get_param(data, modes[0], i + 1) * get_param(data, modes[1], i + 2)
            i += 4
        elif opcode == 3:  # input
            data[data[i + 1]] = input_value
            i += 2
        elif opcode == 4:  # output
            print(get_param(data, modes[0], i + 1))
            i += 2
        else:
            raise ValueError(f"Unknown opcode encountered: {opcode}")

# Read the data
with open('../data/05.txt', 'r') as file:
    data = file.read() 
    data = data.split(',')
    data = [int(i) for i in data]

# Run the program
intcode(data, input_value=1)
