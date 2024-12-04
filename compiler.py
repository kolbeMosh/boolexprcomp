from BoolExprADT import *
import repl
import boolexpr1

# Function to compile a BoolExpr expression into a C++ code string
def compile_expr(expr: BoolExpr, env: dict = None) -> None:

# Writes compiled string translated_string to a file <lineno>.cpp
def write_cpp_output(lineno: int) -> None:
    #global translated_string, true_vars, false_vars
    with open(f"{lineno}.cpp", "w") as file:
        file.write("#include <iostream>\n")
        file.write("using namespace std;\n\n")
        file.write("int main() {\n")

        for var in boolexpr1.true_vars:
            file.write(f"    bool {var} = true;\n")
        for var in boolexpr1.false_vars:
            file.write(f"    bool {var} = false;\n")

        file.write(f"    bool result = {repl.translated_string};\n")
        file.write("    cout << (result ? \"true\" : \"false\") << endl;\n")
        file.write("    return 0;\n")
        file.write("}\n")