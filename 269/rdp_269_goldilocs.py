import os.path
import sys
if __name__ == '__main__':
	#inputFile = os.path.normpath(r'input.txt')
	inputFile = os.path.normpath(r'input_challenge.txt')
	
	with open('output.txt', 'w') as fw:
		with open(inputFile, 'r') as fr:
			read_data = fr.readlines()
		# slurp input to list of strings delimited by space and newline
		
		output = []
		for i in range(len(read_data) ): #Forgot about enumerate :)
			if i == 0:
				g_weight, g_max_temp = read_data[i].strip('\n').split(' ')
				continue
			else:
				weight, temp = read_data[i].strip('\n').split(' ')
				
			if int(weight) >= int(g_weight) and int(temp) <= int(g_max_temp):
				output.append((i, weight, temp))
				
		for i in output:
			fw.write(str(i) + '\n')
	