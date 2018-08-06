import text_utilities, optimisations
def go(token_list):
	token_list = optimisations.tokenizer_optimize(text_utilities.bake_lit(text_utilities.remove_parn(token_list, "lst")))

	result, multiplication, addition, substraction, division, modulo,\
	power, ampersand, comma, factorial, setvalue, greater, \
	smaller, compare, different, less_equal, greater_equal, \
	plus_equal, divide_equal, mul_equal, minus_equal, pow_equal, \
	mod_equal, concatenate, func, and_op, or_op, not_op, in_op, func_first = [],[],[],[],[],[],[],[],[],[],[],[],[],\
	[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

	adder, counter_complete, opnd_parn = 0, 0, 0

	for x in token_list:
		counter_complete += len(x)
		if x == "(" or x == ")":
			if x == "(": opnd_parn += 1
			elif x == ")": opnd_parn -= 1

		if opnd_parn > 0: continue
		if x == "*": multiplication.append(counter_complete-1)
		elif x == "+": addition.append(counter_complete-1)
		elif x == "-": substraction.append(counter_complete-1)
		elif x == "/": division.append(counter_complete-1)
		elif x == "%": modulo.append(counter_complete-1)
		elif x == "^": power.append(counter_complete-1)
		elif x == "&": ampersand.append(counter_complete-1)
		elif x == ",": comma.append(counter_complete-1)
		elif x == "!": factorial.append(counter_complete-1)
		elif x == "=": setvalue.append(counter_complete-1)
		elif x == ">": greater.append(counter_complete-1)
		elif x == "<": smaller.append(counter_complete-1)
		elif x == "@": func.append(counter_complete-1)
		elif x == "$": func_first.append(counter_complete-1)
		elif x == "==": compare.append(counter_complete-2)
		elif x == "!=": different.append(counter_complete-2)
		elif x == "<=": less_equal.append(counter_complete-2)
		elif x == ">=":	greater_equal.append(counter_complete-2)
		elif x == "+=":	plus_equal.append(counter_complete-2)
		elif x == "/=":	divide_equal.append(counter_complete-2)
		elif x == "*=":	mul_equal.append(counter_complete-2)
		elif x == "-=":	minus_equal.append(counter_complete-2)
		elif x == "^=":	pow_equal.append(counter_complete-2)
		elif x == "%=": mod_equal.append(counter_complete-2)
		elif x == "&=": concatenate.append(counter_complete-2)
		elif x == "&&": and_op.append(counter_complete-2)
		# 5 + 5 * 6

	sorted_op_lst, found_op, parse_1 = ["$", ",", "&&", "==", "&=", "!=", "<=", ">=", "+=", "/=", "*=", "-=", "^=", "%=" ,"=", ">", \
	"<", "&", "^", "*", "/", "%", "-", "+", "@", "!"], False, "(null)"

	sorted_opIdxLst_lst = [func_first, comma, and_op, compare, concatenate, different, less_equal, greater_equal, \
	plus_equal, divide_equal, mul_equal,minus_equal, pow_equal, mod_equal, setvalue, greater, smaller, ampersand, \
	power, multiplication, division, modulo, substraction, addition, func, factorial]

	for counter, browse_in in enumerate(sorted_op_lst):
		if browse_in in token_list and text_utilities.check_if_contains(browse_in, \
		text_utilities.erase_btwn_parn(token_list)) in sorted_opIdxLst_lst[counter]:
			operator = browse_in
			if operator == "$": operator = "@"
			parse_1, found_op = parse_expr(text_utilities.list_to_str(token_list), operator, sorted_opIdxLst_lst[counter]), True
			break

	if not found_op:
		if len(token_list) == 0: parse_1 = ""
		else: parse_1 = text_utilities.list_to_str(text_utilities.remove_parn(token_list, "lst"))

	return parse_1

	"""
	1 - Parenthesis
	2 - Power
	3 - Multiplication/Division/Modulo
	4 - Addition/Substraction
	"""

def parse_expr(expr, operator, operatorIndexes):
		token_list, result, adder, multi_str = text_utilities.str_to_list(expr), operator, 0, False
		for counter, x in enumerate(operatorIndexes):
			if counter == 0 and len(operatorIndexes) > 0: operatorIndexes.append(len(token_list))

			result_to_put = text_utilities.list_to_str(token_list[adder: x])
			trigger_operators, triggered = ["$", "&&", "==", "&=", "!=", "<=", ">=", "+=", "/=", "*=", "-=", "^=", "%=" ,"=", ">", "<", \
			",", "&", "^", "*", "/", "%", "-", "+", "!", "(", ")", "@"], False
			trigger_op = ""

			for x2 in trigger_operators:
				if x2 in result_to_put:
					triggered, trigger_op = True, x2
					break

			if triggered:
				if not text_utilities.check_if_type(result_to_put, "str") and \
				not text_utilities.check_if_type(result_to_put, "char"):
					arg_to_put = text_utilities.remspaces_bn(result_to_put)
					if len(operator) > 1 and counter > 0: arg_to_put = arg_to_put[len(operator)-1:len(arg_to_put)]
					result_to_put = go(arg_to_put)
					multi_str = True
					pass
			if operator == "@" and result_to_put.strip() == "":
				adder = x + 1
				continue

			# result_to_put = result_to_put.replace("\t", "\\t")

			if not multi_str: result += "\n~" + result_to_put.strip()
			else:
				for x2 in result_to_put.split("\n"):
					result += "\n~" + text_utilities.remspaces_bn(x2)

			adder = x + 1

		return result
