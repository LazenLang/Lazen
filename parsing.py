import text_utilities
def go(token_list):
	token_list = text_utilities.str_to_list(text_utilities.remove_parn(text_utilities.list_to_str(token_list)))

	result, multiplication, addition, substraction, division, modulo, power = [],[],[],[],[],[],[]
	adder, counter_complete, opnd_parn = 0, False, 0

	for x in token_list:
		counter_complete += len(x)
		if x == "(" or x == ")":
			if x == "(":
				if not opnd_parn:
					opnd_parn = True
			elif x == ")":
				if opnd_parn:
					opnd_parn = False
		if opnd_parn:
			continue
		if x == "*":
			multiplication.append(counter_complete-1)
		elif x == "+":
			addition.append(counter_complete-1)
		elif x == "-":
			substraction.append(counter_complete-1)
		elif x == "/":
			division.append(counter_complete-1)
		elif x == "%":
			modulo.append(counter_complete-1)
		elif x == "^":
			power.append(counter_complete-1)
			# 5 + 5 * 6

	parse_1 = "NULL"

	if "^" in token_list and text_utilities.check_if_contains("^", text_utilities.erase_btwn_parn(token_list)) in power:
		parse_1 = parse_math_expr(text_utilities.list_to_str(token_list), "^", power)
	elif "*" in token_list and text_utilities.check_if_contains("*", text_utilities.erase_btwn_parn(token_list)) in multiplication:
		parse_1 = parse_math_expr(text_utilities.list_to_str(token_list), "*", multiplication)
	elif "/" in token_list and text_utilities.check_if_contains("/", text_utilities.erase_btwn_parn(token_list)) in division:
		parse_1 = parse_math_expr(text_utilities.list_to_str(token_list), "/", division)
	elif "%" in token_list and text_utilities.check_if_contains("%", text_utilities.erase_btwn_parn(token_list)) in modulo:
		parse_1 = parse_math_expr(text_utilities.list_to_str(token_list), "%", modulo)
	elif "-" in token_list and text_utilities.check_if_contains("-", text_utilities.erase_btwn_parn(token_list)) in substraction:
		parse_1 = parse_math_expr(text_utilities.list_to_str(token_list), "-", substraction)
	elif "+" in token_list and text_utilities.check_if_contains("+", text_utilities.erase_btwn_parn(token_list)) in addition:
		parse_1 = parse_math_expr(text_utilities.list_to_str(token_list), "+", addition)
	else:
		if not len(token_list) == 0:
			parse_1 = go(text_utilities.list_to_str(token_list) + "+0")
		else:
			parse_1 = ""
	return parse_1

	"""
	1 - Parenthesis
	2 - Power
	3 - Multiplication/Division/Modulo
	4 - Addition/Substraction
	"""

def parse_math_expr(expr, operator, operatorIndexes):
		token_list, result, adder, multi_str = text_utilities.str_to_list(expr), operator, 0, False
		for counter, x in enumerate(operatorIndexes):

			if counter == 0 and len(operatorIndexes) > 0:
				operatorIndexes.append(len(token_list))

			result_to_put = text_utilities.list_to_str(token_list[adder: x])
			if "+" in result_to_put or "-" in result_to_put or "*" in result_to_put or "/" in result_to_put or "^" in result_to_put or "%" in result_to_put:
				result_to_put = go(text_utilities.str_to_list(result_to_put))
				multi_str = True
			if not multi_str:
				result += "\n\t" + result_to_put
			else:
				for x2 in result_to_put.split("\n"):
					result += "\n\t" + x2
			adder = x + 1

		return result
