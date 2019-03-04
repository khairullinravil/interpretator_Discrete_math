#!/usr/bin/env python
# coding: utf-8

# lexer

import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = (
    'NAME',
    'PLUS',
    'MULT',
    'LAMBDA',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'POINT',
    'ARROW',
    'COLON',
    'NAT',
    'NEWLINE',
)

t_NEWLINE = r'\n+'
t_NAME = r'x\d+'
t_COLON = r':'
t_NAT = r'NAT'
t_ARROW = r'->'
t_PLUS = r'\+'
t_MULT = r'\*'
t_NUMBER = r'\d+'
t_LAMBDA = r'lambda'
t_POINT = r'\. '
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = r' '

def t_error(t):
    print(f"ERROR unexpected symbol '{t.value[0]}', at lexer.py line 40")
    t.lexer.skip(1)

lexer = lex.lex()

import ply.yacc as yacc
from expressions import *

precedence = (
    ('left', 'EXP'),
    ('right', 'RPAREN'),
)

def p_program1(t):
    'program : context'
    t[0] = Program(None)

def p_program2(t):
    'program : expression'
    t[0] = Program(t[1])

def p_program3(t):
    'program : context NEWLINE program'
    t[0] = Program(t[3])

def p_context1(t):
    'context : NAME COLON type'
    context[t[1]] = t[3]

def p_context2(t):
    'context : context NEWLINE context'

def p_expression1(t):
    'expression : NUMBER'
    t[0] = NodeExpression(t[1], 1)

def p_expression2(t):
    '''
    expression : MULT
               | PLUS
    '''
    t[0] = NodeExpression(t[1], 3)

def p_expression3(t):
    'expression : NAME'
    t[0] = NodeExpression(t[1])

def p_expression4(t):
    'expression : expression expression %prec EXP'
    t[0] = NodeApplication(t[1], t[2])

def p_type1(t):
    'type : NAT'
    t[0] = 1

def p_type2(t):
    'type : type ARROW type'
    t[0] = t[1] + t[3]

def p_lambda(t):
    'lambda : LAMBDA NAME POINT expression'
    if not t[2] in context:
        sys.exit(f'{t[2]} does not exist in context, at lexer.py line 102')
    t[0] = (t[2], t[4])

def p_beta1(t):
    'expression : LPAREN lambda RPAREN expression'
    t[0] = NodeBeta(t[2][1], t[4], t[2][0])

def p_beta2(t):
    'expression : lambda'
    t[0] = NodeLambda(t[1][0], t[1][1])

parser = yacc.yacc()