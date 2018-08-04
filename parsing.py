import text_utilities
def go(token_list):
	token_list = text_utilities.remove_parn(token_list, "lst")

	result, multiplication, addition, substraction, division, modulo,\
	power, ampersand, comma, factorial = [],[],[],[],[],[],[],[],[],[]

	adder, counter_complete, opnd_parn = 0, 0, 0

	for x in token_list:
		counter_complete += len(x)
		if x == "(" or x == ")":
			if x == "(":
				opnd_parn += 1
			elif x == ")":
				opnd_parn -= 1
		if opnd_parn > 0:
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
		elif x == "&":
			ampersand.append(counter_complete-1)
		elif x == ",":
			comma.append(counter_complete-1)
		elif x == "!":
			factorial.append(counter_complete-1)
			# 5 + 5 * 6

	parse_1 = "NULL"

	# , & ^ * / % - +
	sorted_op_lst, found_op = [",", "&", "^", "*", "/", "%", "-", "+", "!"], False
	sorted_opIdxLst_lst = [comma, ampersand, power, multiplication, division, modulo, substraction, \
							addition, factorial]

	for counter, browse_in in enumerate(sorted_op_lst):
		if browse_in in token_list and text_utilities.check_if_contains(browse_in, \
		text_utilities.erase_btwn_parn(token_list)) in sorted_opIdxLst_lst[counter]:
			parse_1, found_op = parse_math_expr(text_utilities.list_to_str(token_list), browse_in, sorted_opIdxLst_lst[counter]), True
			break

	if not found_op:
		if not len(token_list) == 0:
			if not text_utilities.check_if_type(text_utilities.list_to_str(token_list), "str") \
			and not text_utilities.check_if_type(text_utilities.list_to_str(token_list), "char"):
				parse_1 = go(text_utilities.list_to_str(text_utilities.remove_parn(token_list, "lst")) + "+0")
			else:
				parse_1 = go(text_utilities.list_to_str(text_utilities.remove_parn(token_list, "lst")) + "&\"\"")
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
			if "+" in result_to_put or "-" in result_to_put or "*" in result_to_put or \
			"/" in result_to_put or "^" in result_to_put or "%" in result_to_put or \
			"(" in result_to_put or ")" in result_to_put or "!" in result_to_put or \
			"," in result_to_put or "&" in result_to_put:

				if not text_utilities.check_if_type(result_to_put, "str") and \
				not text_utilities.check_if_type(result_to_put, "char"):
					result_to_put = go(text_utilities.str_to_list(result_to_put))
					multi_str = True
					pass

			if not multi_str:
				result += "\n\t" + result_to_put
			else:
				for x2 in result_to_put.split("\n"):
					result += "\n\t" + x2
			adder = x + 1

		return result
