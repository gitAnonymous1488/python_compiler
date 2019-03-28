import sys
import token_defs
import buffer_wrapper

file_contents = buffer_wrapper.read_ahead(sys.stdin.read())
token_list = buffer_wrapper.token_list()

# ########################################

def get_read_ahead():
	return file_contents

def get_next_char():
	c = file_contents.get_char()
	if len(c) == 0:
		return chr(3)
	return c

def bookmark():
	file_contents.bookmark()

def reset_to_bookmark():
	file_contents.reset_to_bookmark()

def set_bookmark(pos):
	file_contents.set_bookmark(pos)

def get_bookmark():
	return file_contents.bookmark_pos

def get_position():
	return file_contents.pos

# ########################################

def get_token_list():
	return token_list

def add_token_to_list(token):
	token_list.add_token(token)

def get_next_token():
	return token_list.get_next_token()

# #######################################


def ignore(char):
	return ord(char) in [ord(x) for x in " \n\t\r"]

def is_digit(char):
	return ord("0") <= ord(char) <= ord("9")

def is_alpha(char):
	return (ord("a") <= ord(char) <= ord("z")) or \
			(ord("A") <= ord(char) <= ord("Z")) or \
			(ord(char) in [ord("_")])


# 
# <float>  -> <digit-list> <decimal-part> <exp> |
# 			  <digit-list> <decimal-part>	 	|
# 			  <decimal-part> <exp>			|
# 			  <decimal-list> <exp> 			|
# 			  <decimal-list> '.' <exp>
# 
# <decimal-part> -> '.' <decimal-list>
# 
# 
def scan_float():
	bookmark()
	float_beginning = get_bookmark()

	token_str = get_next_char()

	next_digit = get_next_char()

	# <digit-list>
	while is_digit(next_digit):
		token_str += next_digit
		next_digit = get_next_char()

	if next_digit == token_defs.decimal_prefix["DECIMAL"]:

		token_str += next_digit
		next_digit = get_next_char()

		# <digit-list>
		while is_digit(next_digit):
			token_str += next_digit
			next_digit = get_next_char()

		if next_digit == token_defs.decimal_prefix["EXPONENT"]:

			token_str += next_digit
			next_digit = get_next_char()

			if next_digit in "+-":
				token_str += next_digit
				next_digit = get_next_char()

			# <digit-list>
			while is_digit(next_digit):
				token_str += next_digit
				next_digit = get_next_char()


		set_bookmark(get_position() - 1)

		return token_defs.create_float(token_str)
	return None


# 
# <integer>  -> <digit> <integer> 	|
# 				<digit>	
# 
# <digit> 	-> '0' | '1' | ... 		| '9'
# 
# 
def scan_int():
	bookmark()
	int_beginning = get_bookmark()

	token_str = get_next_char()

	# <float>
	# <decimal-part> <exp>
	if token_str == token_defs.decimal_prefix["DECIMAL"]:
		set_bookmark(int_beginning)
		reset_to_bookmark()
		return scan_float()

	# <integer>
	# <integer>  -> <digit> <integer> 	|
	# 				<digit>
	next_digit = get_next_char()
	while is_digit(next_digit):
		token_str += next_digit
		next_digit = get_next_char()


	# 
	# <float>  -> <digit-list> <dec-part> <exp> |
	# 			  <digit-list> <dec-part>	 	|
	# 			  <digit-list> <exp> 			|
	# 			  <digit-list> '.' <exp>
	# 
	if next_digit == token_defs.decimal_prefix["DECIMAL"] or \
	   	next_digit == token_defs.decimal_prefix["EXPONENT"]:
		set_bookmark(int_beginning)
		reset_to_bookmark()
		return scan_float()

	# 
	# 	MADE IT HERE BECAUSE IT DOESNT MATCH ANYTHING
	# 

	set_bookmark(get_position() - 1)
	reset_to_bookmark()

	return token_defs.create_int_token(token_str)


def next_token():
	bookmark()
	token_str = get_next_char()

	if is_digit(token_str):
		reset_to_bookmark()
		return scan_int()

	elif token_str == token_defs.token_defs["DECIMAL"]:
		reset_to_bookmark()
		return scan_float()

	elif is_alpha(token_str):
		bookmark()
		next_alpha = get_next_char()
		while is_alpha(next_alpha):
			bookmark()
			token_str += next_alpha
			next_alpha = get_next_char()
		reset_to_bookmark()
		return token_str
		
	elif ignore(token_str):
		return next_token()

	elif token_str == token_defs.token_defs["ASSIGNMENT"]:
		bookmark()
		next_relation = get_next_char()
		if next_relation == token_defs.token_defs["ASSIGNMENT"]:
			token_str += next_relation
		else:
			reset_to_bookmark()
		return token_str

	elif token_str == token_defs.token_defs["NOT"]:
		bookmark()
		next_relation = get_next_char()
		if next_relation == token_defs.token_defs["ASSIGNMENT"]:
			token_str += next_relation
		else:
			reset_to_bookmark()
		return token_str

	elif token_str == token_defs.token_defs["NOT"]:
		bookmark()
		next_relation = get_next_char()
		if next_relation == token_defs.token_defs["ASSIGNMENT"]:
			token_str += next_relation
		else:
			reset_to_bookmark()
		return token_str

	elif token_str == token_defs.token_defs["LESS_THAN"]:
		bookmark()
		next_relation = get_next_char()
		if next_relation == token_defs.token_defs["ASSIGNMENT"]:
			token_str += next_relation
		else:
			reset_to_bookmark()
		return token_str

	elif token_str == token_defs.token_defs["GRT_THAN"]:
		bookmark()
		next_relation = get_next_char()
		if next_relation == token_defs.token_defs["ASSIGNMENT"]:
			token_str += next_relation
		else:
			reset_to_bookmark()
		return token_str

	elif token_str == token_defs.token_defs["BIT_AND"]:
		bookmark()
		next_relation = get_next_char()
		if next_relation == token_defs.token_defs["BIT_AND"]:
			token_str += next_relation
		else:
			reset_to_bookmark()
		return token_str

	elif token_str == token_defs.token_defs["BIT_OR"]:
		bookmark()
		next_relation = get_next_char()
		if next_relation == token_defs.token_defs["BIT_OR"]:
			token_str += next_relation
		else:
			reset_to_bookmark()
		return token_str

	elif token_str == token_defs.token_defs["OPAR"]:
		return token_str

	elif token_str == token_defs.token_defs["CPAR"]:
		return token_str

	elif token_str == token_defs.token_defs["OSQ"]:
		return token_str

	elif token_str == token_defs.token_defs["CSQ"]:
		return token_str

	elif token_str == token_defs.token_defs["ADD"]:
		return token_str

	elif token_str == token_defs.token_defs["SUB"]:
		return token_str

	elif token_str == token_defs.token_defs["MULT"]:
		return token_str

	elif token_str == token_defs.token_defs["DIV"]:
		return token_str

	elif token_str == token_defs.token_defs["MOD"]:
		return token_str

	return None




if __name__ == "__main__":
	c = 0
	token = next_token()
	while token is not None:
		print(token)
		add_token_to_list(token)
		token = next_token()
	