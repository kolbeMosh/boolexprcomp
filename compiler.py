from BoolExprADT import *
import repl
import boolexpr1

# Function to compile a BoolExpr expression into a C++ code string
def compile_expr(expr: BoolExpr, env: dict = None) -> None:
	if env is None:
		env = {}
	if isinstance(expr, Literal):
		repl.translated_string += 'true' if expr.value else 'false'
	elif isinstance(expr, Variable):
		repl.translated_string += expr.name
	elif isinstance(expr, Operator):
		if expr.operator == '&':
			repl.translated_string += '('
			compile_expr(expr.operands[0], env)
			repl.translated_string += ' && '
			compile_expr(expr.operands[1], env)
			repl.translated_string += ')'
		elif expr.operator == '|':
			repl.translated_string += '('
			compile_expr(expr.operands[0], env)
			repl.translated_string += ' || '
			compile_expr(expr.operands[1], env)
			repl.translated_string += ')'
		elif expr.operator == '~':
			repl.translated_string += '!'
			compile_expr(expr.operands[0], env)
	else:
		raise ValueError(f"Unsupported node: {type(expr)}")


# Writes compiled string translated_string to a file <lineno>.cpp
def write_cpp_output(lineno: int) -> None:
	#global translated_string, true_vars, false_vars
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
