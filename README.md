#BOOL Expression language Compiler

Implements a compiler for the following EBNF Grammar using Python and ply (lexer):

EBNF grammar
<program>	  : ( <declarations> , <expr> )
<declarations> : [ ]
<declarations> : [ <varlist> ]
<varlist>	  : <var>
<varlist>	  : <var> , <varlist>
<expr>		 : <expr> & <expr>
<expr>		 : <expr> | <expr>
<expr>		 : ~ <expr>
<expr>		 : <literal> 
<expr>		 : <var>
<literal>	  : t
<literal>	  : f
<var>		  : a...z	 but not t or f obviously
