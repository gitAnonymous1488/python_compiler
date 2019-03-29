

"""

declare enum
declare aggregate
declare union
declare variable
declare function
declare constant
delcare typedef
declare new


expression new
expression sizeof
expression int
expression float
expression string
expression name
expression compound
expression cast
expression call
expression index
expression field
expression unary
expression binary
expression ternary

statement new
statement declare
statement return
statement break
statement continue
statement block
statement if
statement while
statement do_while
statement for
statement switch
statement assign
statement init
statement expression


"""

tokens = None

def parse_if_statement():
	pass


def parse_while_statement():
	pass


def parse_for_statement():
	pass


def parse_assign_statement():
	pass

def parse_expression():
	pass


def parse_tokens(tokens):
	while tokens != []:
		curr = tokens.pop(0)
		if curr["KIND"] == "IF_STAT":

		print(curr)
	print("done")