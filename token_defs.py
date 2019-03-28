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

def create_id(token):
	return {
		"KIND": "ID",
		"VALUE": token
	}

def create_str(token):
	return {
		"KIND": "STRING",
		"VALUE": token
	}



