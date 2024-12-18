
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightNOTAND COMMA F LBRACK LPAREN NOT OR RBRACK RPAREN T VARsentence : LPAREN declarations COMMA expr RPARENdeclarations : LBRACK RBRACK\n\t\t\t\t\t| LBRACK varlist RBRACKvarlist : varlist COMMA VAR\n\t\t\t   | VARexpr : T\n\t\t\t| Fexpr : NOT exprexpr : expr AND exprexpr : expr OR exprexpr : VAR'
    
_lr_action_items = {'LPAREN':([0,],[2,]),'$end':([1,16,],[0,-1,]),'LBRACK':([2,],[4,]),'COMMA':([3,6,7,8,14,20,],[5,-2,15,-5,-3,-4,]),'RBRACK':([4,7,8,20,],[6,14,-5,-4,]),'VAR':([4,5,12,15,17,18,],[8,13,13,20,13,13,]),'T':([5,12,17,18,],[10,10,10,10,]),'F':([5,12,17,18,],[11,11,11,11,]),'NOT':([5,12,17,18,],[12,12,12,12,]),'RPAREN':([9,10,11,13,19,21,22,],[16,-6,-7,-11,-8,-9,-10,]),'AND':([9,10,11,13,19,21,22,],[17,-6,-7,-11,-8,-9,17,]),'OR':([9,10,11,13,19,21,22,],[18,-6,-7,-11,-8,-9,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentence':([0,],[1,]),'declarations':([2,],[3,]),'varlist':([4,],[7,]),'expr':([5,12,17,18,],[9,19,21,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentence","S'",1,None,None,None),
  ('sentence -> LPAREN declarations COMMA expr RPAREN','sentence',5,'p_sentence','boolexpr1.py',76),
  ('declarations -> LBRACK RBRACK','declarations',2,'p_declarations','boolexpr1.py',82),
  ('declarations -> LBRACK varlist RBRACK','declarations',3,'p_declarations','boolexpr1.py',83),
  ('varlist -> varlist COMMA VAR','varlist',3,'p_varlist','boolexpr1.py',87),
  ('varlist -> VAR','varlist',1,'p_varlist','boolexpr1.py',88),
  ('expr -> T','expr',1,'p_expr_literal','boolexpr1.py',101),
  ('expr -> F','expr',1,'p_expr_literal','boolexpr1.py',102),
  ('expr -> NOT expr','expr',2,'p_expr_not','boolexpr1.py',106),
  ('expr -> expr AND expr','expr',3,'p_expr_and','boolexpr1.py',110),
  ('expr -> expr OR expr','expr',3,'p_expr_or','boolexpr1.py',114),
  ('expr -> VAR','expr',1,'p_expr_var','boolexpr1.py',118),
]
