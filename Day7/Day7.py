import sys
import copy
from itertools import permutations
sys.path.append('../Day5')
from Day5 import TEST_diagnostic_program
sys.path.append('../Day7')

def max_output_signal_first_star(program):
	max_output_signal = None # output_signals could be negative
	settings = list(range(5))
	for phase_settings in permutations(settings, len(settings)):
		output_signal = 0
		for phase in phase_settings:
			output_signal = TEST_diagnostic_program([phase, output_signal], program)

		if max_output_signal == None:
			max_output_signal = output_signal
		else:
			max_output_signal = max(max_output_signal, output_signal)
	
	return max_output_signal


def max_output_signal_second_star(program):
	max_output_signal = None
	settings = list(range(5,10))
	for phase_settings in permutations(settings, len(settings)):
		output_signal = TEST_diagnostic_program_revamped([0] + list(phase_settings), program)
		
		if max_output_signal == None:
			max_output_signal = output_signal
		else:
			max_output_signal = max(max_output_signal, output_signal)
	
	return max_output_signal

def TEST_diagnostic_program_revamped(input_instructions, program):
	*A, B, C, D, E = input_instructions
	input_instructions = [A, [B], [C], [D], [E]]
	amp_outputs = [[0] for i in range(len(input_instructions))]
	amp_index = 0
	
	with open(program) as f:
		_opcodes = list(map(int, f.read().split(',')))
		all_opcodes = [ copy.copy(_opcodes) for i in range(len(amp_outputs)) ] 
	
	amplifier_opcodes_index = [ 0 for i in range(len(amp_outputs)) ]

	
	while not any((all_opcodes[amp_index][i] % 100 == 99) for i in amplifier_opcodes_index):
		
		opcodes = all_opcodes[amp_index]
		i = amplifier_opcodes_index[amp_index]
		current_opcode = opcodes[i]

		print(current_opcode, i, amp_index, input_instructions[amp_index])

		modes = current_opcode // 100
		command = current_opcode % 100

		if command == 1:	
			first_parameter = opcodes[i+1] if modes % 2 == 1 else opcodes[opcodes[i+1]]
			second_parameter = opcodes[i+2] if modes //10 != 0 else  opcodes[opcodes[i+2]]
			third_parameter = opcodes[i+3] 

			opcodes[third_parameter] = first_parameter + second_parameter
			amplifier_opcodes_index[amp_index]+=4

		elif command == 2:
			first_parameter = opcodes[i+1] if modes % 2 == 1 else opcodes[opcodes[i+1]] 
			second_parameter = opcodes[i+2] if modes //10 != 0 else opcodes[opcodes[i+2]]
			third_parameter = opcodes[i+3] 

			opcodes[third_parameter] = first_parameter * second_parameter
			amplifier_opcodes_index[amp_index]+=4

		elif command == 3:
			#takes a single integer as input and save it to the position given by its only parameter
			if input_instructions[amp_index] == []: # waiting on the previous amplifier
				amp_index = (amp_index + 1) % len(amp_outputs)
				continue
			
			
			output = opcodes[i+1]
			opcodes[output] = input_instructions[amp_index].pop(0)
			amplifier_opcodes_index[amp_index]+=2

		elif command == 4:
			#outputs the value of its only parameter.
			value = opcodes[i+1] if modes % 2 == 1 else opcodes[opcodes[i+1]]
			out_value = value
			
			next_amp = (amp_index + 1) % len(amp_outputs) 
			input_instructions[next_amp].append(out_value)
			amp_outputs[amp_index].append(out_value)
			amplifier_opcodes_index[amp_index]+=2

		elif command == 5:
			first_parameter = opcodes[i+1] if modes % 2 == 1 else opcodes[opcodes[i+1]] 
			second_parameter = opcodes[i+2] if modes //10 != 0 else opcodes[opcodes[i+2]] 

			if first_parameter:
				amplifier_opcodes_index[amp_index] = second_parameter
			else:
				amplifier_opcodes_index[amp_index]+=3

		elif command == 6:
			first_parameter = opcodes[i+1] if modes % 2 == 1 else opcodes[opcodes[i+1]] 
			second_parameter = opcodes[i+2] if modes //10 != 0 else opcodes[opcodes[i+2]] 
			
			if not first_parameter:
				amplifier_opcodes_index[amp_index] = second_parameter
			else:
				amplifier_opcodes_index[amp_index]+=3

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

			amplifier_opcodes_index[amp_index]+=4
	

		elif command == 99:
			amp_index = (amp_index + 1) % len(amp_outputs)

		all_opcodes[amp_index] = opcodes

		
	return amp_outputs[-1][-1]

if __name__ == '__main__':
	#print(max_output_signal_first_star('input.txt'))
	#print(max_output_signal_second_star('input.txt'))
	print(max_output_signal_second_star('test1.txt'))
	#print(max_output_signal_second_star('test2.txt'))

	print(max_output_signal_second_star('test1.txt'))
	print(max_output_signal_second_star('test1.txt'))
	print(max_output_signal_second_star('test1.txt'))
