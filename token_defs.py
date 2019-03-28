# 
# 	WHAT WILL MY TOKEN OBJS LOOK LIKE?
# 
# 
# 

token_defs_operations = {
	"ASSIGNMENT": 		"=" 	,
	"EQUALITY":			"==" 	,
	"NOT_EQUALITY":		"!="	,
	"LESS_EQUAL":		"<="	,
	"LESS_THAN":		"<"		,
	"GRT_THAN":			">"		,
	"GRT_EQUAL":		">="	,
	"BIT_AND":			"&" 	,
	"AND":				"&&"	,
	"BIT_OR":			"|" 	,
	"OR": 				"||"	,
	"NOT":				"!" 	,
	"OPAR":				"(" 	,
	"CPAR": 			")" 	,
	"OSQ": 				"[" 	,
	"CSQ":				"]" 	,
	"ADD": 				"+" 	,
	"SUB":				"-" 	,
	"MULT":				"*" 	,
	"DIV":				"/" 	,
	"MOD":				"%" 	,
	"DECIMAL": 			"."
}

decimal_prefix = {
	"EXPONENT": "E",
	"NEG_SIGN": "-",
	"POS_SIGN": "+",
	"DECIMAL": "."
}

token_str_def = {
	"STR_QUOTE": 		"\""
}


key_words = [
	""
]


def create_int_token(token):
	return {
		"KIND": "INTEGER",
		"VALUE": token
	}

def create_float(token):
	return {
		"KIND": "FLOAT",
		"VALUE": token
	}

def create_str(token):
	return {
		"KIND": "STRING",
		"VALUE": token
	}

def create_id(token):
	if token in key_words:
		pass
	return {
		"KIND": "ID",
		"VALUE": token
	}

def create_operation(token):
	if token == token_defs_operations["ASSIGNMENT"]:
		return {"KIND": "ASSIGNMENT", "VALUE": token}
	elif token == token_defs_operations["EQUALITY"]:
		return {"KIND": "EQUALITY", "VALUE": token}
	elif token == token_defs_operations["NOT_EQUALITY"]:
		return {"KIND": "NOT_EQUALITY", "VALUE": token}
	elif token == token_defs_operations["LESS_EQUAL"]:
		return {"KIND": "LESS_EQUAL", "VALUE": token}
	elif token == token_defs_operations["LESS_THAN"]:
		return {"KIND": "LESS_THAN", "VALUE": token}
	elif token == token_defs_operations["GRT_THAN"]:
		return {"KIND": "GRT_THAN", "VALUE": token}
	elif token == token_defs_operations["GRT_EQUAL"]:
		return {"KIND": "GRT_EQUAL", "VALUE": token}
	elif token == token_defs_operations["BIT_AND"]:
		return {"KIND": "BIT_AND", "VALUE": token}
	elif token == token_defs_operations["AND"]:
		return {"KIND": "AND", "VALUE": token}
	elif token == token_defs_operations["BIT_OR"]:
		return {"KIND": "BIT_OR", "VALUE": token}
	elif token == token_defs_operations["OR"]:
		return {"KIND": "OR", "VALUE": token}
	elif token == token_defs_operations["NOT"]:
		return {"KIND": "NOT", "VALUE": token}
	elif token == token_defs_operations["OPAR"]:
		return {"KIND": "OPAR", "VALUE": token}
	elif token == token_defs_operations["CPAR"]:
		return {"KIND": "CPAR", "VALUE": token}
	elif token == token_defs_operations["OSQ"]:
		return {"KIND": "OSQ", "VALUE": token}
	elif token == token_defs_operations["CSQ"]:
		return {"KIND": "CSQ", "VALUE": token}
	elif token == token_defs_operations["ADD"]:
		return {"KIND": "ADD", "VALUE": token}
	elif token == token_defs_operations["SUB"]:
		return {"KIND": "SUB", "VALUE": token}
	elif token == token_defs_operations["MULT"]:
		return {"KIND": "MULT", "VALUE": token}
	elif token == token_defs_operations["DIV"]:
		return {"KIND": "DIV", "VALUE": token}
	elif token == token_defs_operations["MOD"]:
		return {"KIND": "MOD", "VALUE": token}
	elif token == token_defs_operations["DECIMAL"]:
		return {"KIND": "DECIMAL", "VALUE": token}




