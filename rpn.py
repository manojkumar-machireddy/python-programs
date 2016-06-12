
def get_output(inp):
	priority = []
	operators = []
	final = []
	for char in inp:
		if( char == "(" ):
			priority.append(1);
		elif( char in  ['+','-','*','/']):
			operators.append(char)
		elif( char == ')'):
			final.append(operators.pop())
		else:
			final.append(char)
			
	return ''.join(final)
			


inp = raw_input("Enter string:")
outstring =  get_output(inp)
print outstring
