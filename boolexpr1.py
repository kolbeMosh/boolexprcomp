#*******************************************************************************
#
#      filename:  boolexpr1.py
#
#   description:  Converts a string into an AST.
#
#        author:  Mosher, Kolbe and Michael, Martinez
# AMU e-mail id:  Kolbe.mosher@my.avemaria.edu, Michael.Martinez@my.avemaria.edu
#
#        course:  CSCI 370: Introduction to Computer Programming
#    instructor:  Dr. Perugini
#    assignment:  Quiz III
#
#      assigned:  November 27, 2024
#           due:  December 05, 2024
#
#*********************************************************************

from repl import *
import ply.lex as lex
import ply.yacc as yacc
from BoolExprADT import *
import sys

# EBNF grammar
# <program>	  : ( <declarations> , <expr> )
# <declarations> : [ ]
# <declarations> : [ <varlist> ]
# <varlist>	  : <var>
# <varlist>	  : <var> , <varlist>
# <expr>		 : <expr> & <expr>
# <expr>		 : <expr> | <expr>
# <expr>		 : ~ <expr>
# <expr>		 : <literal>
# <expr>		 : <var>
# <literal>	  : t
# <literal>	  : f
# <var>		  : a...z	 but not t or f obviously

#################### BEGIN Lexer/Scanner Specification ####################

# Token list
tokens = (
   'VAR',
   'T', 'F',
   'AND', 'OR', 'NOT',
   'LPAREN', 'RPAREN',
   'LBRACK', 'RBRACK',
   'COMMA'
)

# Token regex definitions
t_T = r't'
t_F = r'f'
t_VAR = r'[a-eg-su-z]'
t_AND = r'\&'
t_OR = r'\|'
t_NOT = r'~'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_COMMA = r','

# Ignore spaces and tabs
t_ignore = ' \t'

# Error handling for lexer
def t_error(t):
   raise SyntaxError(f"Illegal character/lexeme '{t.value[0]}'")
   #print(f"Illegal character/lexeme '{t.value[0]}'")
   t.lexer.skip(1)

#################### END Lexer/Scanner Specification ####################

# Build the lexer
lexer = lex.lex()

precedence = (
   ('left', 'OR'),
   ('left', 'AND'),
   ('right', 'NOT'),
)

#################### BEGIN Grammar Pattern-Action Rules ####################

true_vars = {}
false_vars = {}

global_ast = ""

# Grammar rules
def p_sentence(p):
	'''sentence : LPAREN declarations COMMA expr RPAREN'''
	global global_ast
	p[0] = p[4]
	global_ast = p[0]

def p_declarations(p):
	'''declarations : LBRACK RBRACK
					| LBRACK varlist RBRACK'''
	pass

def p_varlist(p):
	'''varlist : varlist COMMA VAR
			   | VAR'''
	global true_vars
	#Unsure if this works##################
	#pass
	if len(p) > 3:
		true_vars[p[3]] = True
		p[0] = True
	else:
		true_vars[p[1]] = True
		p[0] = True
	

def p_expr_literal(p):
	'''expr : T
			| F'''
	p[0] = Literal(value=p[1] in "Ttτ")

def p_expr_not(p):
	'''expr : NOT expr'''
	p[0] = Operator('~', [p[2]])

def p_expr_and(p):
	'''expr : expr AND expr'''
	p[0] = Operator('&', [p[1], p[3]])

def p_expr_or(p):
	'''expr : expr OR expr'''
	p[0] = Operator('|', [p[1], p[3]])

def p_expr_var(p):
	'''expr : VAR'''
	if not p[1] in true_vars:
		false_vars[p[1]] = False
	p[0] = Variable(p[1])

# Error rule for syntax errors
def p_error(p):
	if p:
		print(f"Syntax error at '{p.value}'")
	else:
		print("Syntax error at EOF")

#################### END Grammar Pattern-Action Rules ####################

# Build the parser
parser = yacc.yacc()

# Function for checking if a variable is false
def false_var(var: str) -> bool:
   return var not in true_vars.keys()

#print(parser.parse('([] , f | t & f | ~ t)'))
# main entry point
if __name__ == "__main__":
	main()

"""
for i, line in enumerate(sys.stdin):
	true_vars = set()
	line = line.strip()
	print(f'{len(line)} -> {line}')
	print(f'{i+1}) {parser.parse(line)}')
"""

# print(parser.parse("([q], p & q | f)"))
