def TEST_diagnostic_program(input_instruction):
	with open('input.txt') as f:
		opcodes = f.read().split(',')
		opcodes = list(map(int, opcodes))

	out_value = None
	current_opcode = opcodes[0]
	i = 0
	while current_opcode % 100 != 99:
			
		modes = current_opcode // 100
		command = current_opcode % 100

		if command == 1:	
			first_parameter = opcodes[i+1] if modes % 2 == 1 else opcodes[opcodes[i+1]]
			second_parameter = opcodes[i+2] if modes //10 != 0 else  opcodes[opcodes[i+2]]
			third_parameter = opcodes[i+3] # It is stated that parameters that an instruction writes to will never be in immediate mode

			opcodes[third_parameter] = first_parameter + second_parameter
			i+=4

		elif command == 2:
			first_parameter = opcodes[i+1] if modes % 2 == 1 else opcodes[opcodes[i+1]] 
			second_parameter = opcodes[i+2] if modes //10 != 0 else opcodes[opcodes[i+2]]
			third_parameter = opcodes[i+3] # It is stated that parameters that an instruction writes to will never be in immediate mode

			opcodes[third_parameter] = first_parameter * second_parameter
			i+=4

		elif command == 3:
			#takes a single integer as input and save it to the position given by its only parameter
			output = opcodes[i+1]
			opcodes[output] = input_instruction
			i+=2

		elif command == 4:
			#outputs the value of its only parameter.
			value = opcodes[i+1] if modes % 2 == 1 else opcodes[opcodes[i+1]]
			out_value = value
			i+=2

		elif command == 5:
			first_parameter = opcodes[i+1] if modes % 2 == 1 else opcodes[opcodes[i+1]] 
			second_parameter = opcodes[i+2] if modes //10 != 0 else opcodes[opcodes[i+2]] 

			if first_parameter:
				i = second_parameter
			else:
				i+=3

		elif command == 6:
			first_parameter = opcodes[i+1] if modes % 2 == 1 else opcodes[opcodes[i+1]] 
			second_parameter = opcodes[i+2] if modes //10 != 0 else opcodes[opcodes[i+2]] 
			
			if not first_parameter:
				i = second_parameter
			else:
				i+=3

		elif command == 7:
			first_parameter = opcodes[i+1] if modes % 2 == 1 else opcodes[opcodes[i+1]] 
			second_parameter = opcodes[i+2] if modes //10 != 0 else opcodes[opcodes[i+2]] 
			third_parameter = opcodes[i+3]

			if first_parameter < second_parameter:
				opcodes[third_parameter] = 1
			else:
				opcodes[third_parameter] = 0

			i+=4

		elif command == 8:
			first_parameter = opcodes[i+1] if modes % 2 == 1 else opcodes[opcodes[i+1]] 
			second_parameter = opcodes[i+2] if modes //10 != 0 else opcodes[opcodes[i+2]] 
			third_parameter = opcodes[i+3]

			if first_parameter == second_parameter:
				opcodes[third_parameter] = 1
			else:
				opcodes[third_parameter] = 0

			i+=4

		current_opcode = opcodes[i]

	if out_value == None: 
		print('error')
	return out_value


if __name__ == '__main__':
	print(TEST_diagnostic_program(int(input('input instruction : '))))
