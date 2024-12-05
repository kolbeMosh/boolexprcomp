#*******************************************************************************
#
#      filename:  compiler.py
#
#   description:  Creates a C++ file that evaluates a BoolExpr
#
#        author:  Mosher, Kolbe and Martinez, Michael
# AMU e-mail id:  kolbe.mosher@my.avemaria.edu, michael.martinez@my.avemaria.edu
#
#        course:  CSCI 370: Programming Languages
#    instructor:  Dr. Perugini
#    assignment:  Quiz III
#
#      assigned:  November 27, 2024
#           due:  December 5, 2024
#
#*******************************************************************************

from BoolExprADT import *
import repl
import boolexpr1

def compile_expr(expr: BoolExpr, env: dict = None) -> None:
	if env is None: env = {}
	
	if isinstance(expr, Literal): repl.translated_string += 'true' if expr.value else 'false'
	elif isinstance(expr, Variable): repl.translated_string += expr.name
	elif isinstance(expr, Operator):
		if expr.operator == '&':
			repl.translated_string.append('(')
			compile_expr(expr.operands[0], env)
			repl.translated_string.append(' && ')
			compile_expr(expr.operands[1], env)
			repl.translated_string.append(')')
		elif expr.operator == '|':
			repl.translated_string.append('(')
			compile_expr(expr.operands[0], env)
			repl.translated_string.append(' || ')
			compile_expr(expr.operands[1], env)
			repl.translated_string.append(')')
		elif expr.operator == '~':
			repl.translated_string.append('!')
			compile_expr(expr.operands[0], env)
	else: raise ValueError(f"What is this? What? Is? This?: {type(expr)}")

def write_cpp_output(lineno: int) -> None:
	
	with open(f"{lineno}.cpp", "w") as file:
		file.write("#include <iostream>\n")
		file.write("using namespace std;\n\n")
		file.write("int main() {\n")

		for var in boolexpr1.true_vars:
			file.write(f"	bool {var} = true;\n")
		for var in boolexpr1.false_vars:
			file.write(f"	bool {var} = false;\n")

		file.write(f"	bool result = {repl.translated_string};\n")
		file.write("	cout << (result ? \"true\" : \"false\") << endl;\n")
		file.write("	return 0;\n")
		file.write("}\n")
