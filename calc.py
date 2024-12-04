import ply.lex as lex
import ply.yacc as yacc

# EBNF grammar
# <program>     ::= <statement> SEMICOLON
# <statement>   ::= <expr>
# <statement>   ::= print <expr>
# <statement>   ::= <VARIABLE> = <expr>
# <expr>        ::= <INTEGER>
# <expr>        ::= <VARIABLE>
# <expr>        ::= - <expr>
# <expr>        ::= <expr> + <expr>
# <expr>        ::= <expr> - <expr>
# <expr>        ::= <expr> * <expr>
# <expr>        ::= <expr> / <expr>
# <expr>        ::= <expr> ^ <expr>
# <expr>        ::= ( <expr> )
# <VARIABLE>    ::= a...z (single lowercase letters)
# <INTEGER>     ::= 0 | [1-9][0-9]*
# <PRINT>       ::= 'print'


#################### BEGIN Lexer/Scanner Specification ####################

# List of token names
tokens = (
   'INTEGER',
   'VARIABLE',
   'PRINT',
   'PLUS',
   'MINUS',
   'LPAREN',
   'RPAREN',
   'EQUALS',
   'TIMES',
   'DIVIDE',
   'EXP',
   'SEMICOLON'
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXP = r'\^'
t_SEMICOLON = r';'

# Ignored characters (whitespace)
t_ignore = ' \t'

# Ensure PRINT is recognized as a keyword before VARIABLE
# Token for PRINT keyword
def t_PRINT(t):
   r'print'
   return t

# Token for variables (single lowercase letters a-z)
def t_VARIABLE(t):
   r'[a-z]'
   return t

# Token for integers (including 0)
def t_INTEGER(t):
   r'0|[1-9][0-9]*'
   t.value = int(t.value)  # Convert matched text to an integer
   return t

# Lexer rule for newlines (for line counting)
def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)
   #return t

# Error handling rule
def t_error(t):
   print(f"Invalid character '{t.value[0]}'")
   t.lexer.skip(1)

#################### END Lexer/Scanner Specification ####################

# Build the lexer
lexer = lex.lex()

#################### BEGIN Grammar Pattern-Action Rules ####################

# Symbol table for storing variable values
symtab = {}

# Precedence rules for the operators
precedence = (
   ('right', 'EQUALS'),
   ('left', 'PLUS', 'MINUS'),
   ('left', 'TIMES', 'DIVIDE'),
   ('right', 'EXP'),  # Higher precedence for exponentiation
)

# Grammar rules
def p_program(p):
   '''program : statement SEMICOLON'''
   #print(f"Parsing program: statement={p[1]}, semicolon={p[2]}")
   p[0] = p[1] # Return the statement value

def p_statement_expr(p):
   '''statement : expr'''
   #print(f"Parsing program: statement={p[1]}")
   p[0] = p[1]

def p_statement_print(p):
   '''statement : PRINT expr'''
   print(p[2])
   p[0] = None # Assign a default value to signify the statement is valid

def p_statement_assign(p):
   '''statement : VARIABLE EQUALS expr'''
   global symtab
   #print(f"Assigning: {p[1]} = {p[3]}")
   symtab[p[1]] = p[3]
   p[0] = None # Assign a default value to signify the statement is valid

def p_expr_integer(p):
   '''expr : INTEGER'''
   #print(f"Integer: {p[1]}")
   p[0] = p[1] # manipulating the value stack

def p_expr_variable(p):
   '''expr : VARIABLE'''
   global symtab
   #print(f"Accessing variable '{p[1]}', value = {symtab[p[1]]}")
   if p[1] not in symtab:
       raise NameError(f"Variable '{p[1]}' is not defined.")
       symtab[p[1]] = 0
   p[0] = symtab[p[1]]

def p_expr_negate(p):
   '''expr : MINUS expr %prec EXP'''
   p[0] = -p[2]

def p_expr_binop(p):
   '''expr : expr PLUS expr
           | expr MINUS expr
           | expr TIMES expr
           | expr DIVIDE expr'''
   if p[2] == '+':
      p[0] = p[1] + p[3]
   elif p[2] == '-':
      p[0] = p[1] - p[3]
   elif p[2] == '*':
      p[0] = p[1] * p[3]
   elif p[2] == '/':
      p[0] = p[1] / p[3]

def p_expr_exp(p):
   '''expr : expr EXP expr'''
   p[0] = p[1] ** p[3]

def p_expr_group(p):
   '''expr : LPAREN expr RPAREN'''
   p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
   if p:
      print(f"Syntax error at '{p.value}' (type: {p.type})")
   else:
      print("Syntax error at EOF")

#################### END Grammar Pattern-Action Rules ####################

yacc.yacc(debug=True, write_tables=True)
# Build the parser
parser = yacc.yacc()

# Print all tokens for debugging purposes
def print_tokens(input_str):
   lexer.input(input_str)
   for tok in lexer:
      print(tok)

# Main function
if __name__ == "__main__":
   import sys
   args = sys.argv[1:]

   # Parse command-line arguments for -i option
   for arg in args:
      if arg == '-i':
         iFlag = True
      else:
         print(f"Invalid option: {arg}")
         sys.exit(1)

   if len(sys.argv) == 1:
      print('Calc> ', flush=True, end='')

   for line in sys.stdin:
      line = line[:-1]      # remove trailing newline
      #line = line.strip()   # remove trailing newline

      try:
         # for debugging purposes
         #print("Tokens:")
         #print_tokens(line)
         #print(f"Symbol Table: {symtab}")
         result = parser.parse(line)
         #print (result)
         if result or result == None:
            #print('"{}" is a program'.format(line))
         
            if len(sys.argv) == 1:
               print('Calc> ', flush=True, end='')
         else:
            print('"{}" is not a program'.format(line))
      except SyntaxError:
         print('"{}" contains lexical units which are not lexemes '
               'and, thus, is not a program.'.format(line))
      except EOFError as e:
         sys.exit(0)
      except Exception as e:
         print(e)
         sys.exit(-1)
