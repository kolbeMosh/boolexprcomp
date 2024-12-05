#*******************************************************************************
#
#      filename:  interpreter.py
#
#   description:  Implements an intrepreter for the BOOL Expression Grammar.
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

from typing import Union, List 
from BoolExprADT import *

def eval1(expr: BoolExpr, env: dict = None) -> bool:
	#Recursively evaluates, a BoolExpr as a boolean expression.
	#The env parameter. is a dictionary that maps variable names to their boolean values.
	if env is None:
		env={}
	
	if isinstance(expr, Literal):
		return expr.value
	elif isinstance(expr, Variable):
		if expr.name in env:
			return env[expr.name]
		else:
			return False
	elif isinstance(expr, Operator):
		if expr.operator == '&':
			ho0 = eval1(expr.operands[0], env)
			ho1 = eval1(expr.operands[1], env)
			return ho0 and ho1
		elif expr.operator == '|':
			ho0 = eval1(expr.operands[0], env)
			ho1 = eval1(expr.operands[1], env)
			return ho0 or ho1
		elif expr.operator == '~':
			ho0 = eval1(expr.operands[0], env)
			return not ho0
		else:
			raise ValueError(f"Unknown operator '{expr.operator}'")
	else:
		raise TypeError(f"Unknown expression type: {type(expr)}")
