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
