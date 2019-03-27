import sys


def is_digit(char):
	return 48 <= ord(char) <= 57

def is_alpha(char):
	return (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122)

def get_next_char():
	c = sys.stdin.read(1)
	if len(c) == 0:
		return chr(3)
	return c

def next_token(starting_char=None):
	if starting_char is None:
		token_str = get_next_char()
	else:
		token_str = starting_char

	if is_digit(token_str):
		next_digit = get_next_char()
		while is_digit(next_digit):
			token_str += next_digit
			next_digit = get_next_char()
		return token_str, next_digit
	elif is_alpha(token_str):
	 	next_alpha = get_next_char()
	 	while is_alpha(next_alpha):
	 		token_str += next_alpha
	 		next_alpha = get_next_char()
	 	return token_str, next_alpha
	return None, None




if __name__ == "__main__":
	token, next_char = next_token()
	while token is not None:
		print(token)
		token, next_char = next_token(next_char)
	