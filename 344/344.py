
def convert_dec_to_bin(n):
	''' returns a string representation of a binary number '''
	return bin(n).lstrip('0b')

def get_baum_sweet(b_number):
	''' main function to generate baum_sweet sequence '''
	zeros_seen = 0
	prev = '1'
	has_baum_sweet_seq = 0
	for i in b_number:
		if i == '0':						# is current number zer0
			zeros_seen += 1					# update count of seen zeros
			if zeros_seen % 2 != 0:			# if count of seen zeros is odd set to one
				has_baum_sweet_seq = 1
			else:
				has_baum_sweet_seq = 0		# if even, set to zero
	return has_baum_sweet_seq
	
def pretty_answer(n):
	''' gives more descriptive answer to the solution '''
	pass

if __name__ == '__main__':
	# get number
	number = 1
	b_number =  convert_dec_to_bin(number)
	
	print '{} is {} in binary\nbaum-sweet sequence?: {}'.format(number, b_number, get_baum_sweet(b_number))
	
	# get sequence of baum-sweet values up to n
	for i in range(number+1):
		print get_baum_sweet(convert_dec_to_bin(i)),