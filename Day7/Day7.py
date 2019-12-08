import sys
from itertools import permutations
sys.path.append('../Day5')
from Day5 import TEST_diagnostic_program
sys.path.append('../Day7')

def max_output_signal_first_star(program):
	max_output_signal = None # output_signals could be negative
	settings = list(range(5))
	for phase_settings in permutations(settings, len(settings)):
		A,B,C,D,E = phase_settings
		
		output_signal = 0
		for phase in phase_settings:
			output_signal = TEST_diagnostic_program([phase, output_signal], program)

		if max_output_signal == None:
			max_output_signal = output_signal
		else:
			max_output_signal = max(max_output_signal, output_signal)
	
	return max_output_signal

if __name__ == '__main__':
	print(max_output_signal_first_star('input.txt'))
