import ast
from src.trumpscript.constants import *


def error():
    print("YOURE FIRED")
    exit(0)
def parse(inputTokens):
    global tokens
    tokens = inputTokens
    parse_stmt(0)

def parse_stmt(idx):
    if tokType(idx) == T_Make:
        if tokType(idx+1) != T_Word:
            error()
        id = tokVal(idx+1)
        parse_value(idx+2)


def parse_expr(idx):


def parse_value(idx):
#    if not(tokType(idx) == T_Word | tokType(idx) == T_False | tokType(idx) == T_True | tokType(idx) == T_Not | tokType(idx) == T_):
    if tokType(idx) == T_Not:
        value = parse_value(idx+1)
        expr = ast.UnaryOp(op = ast.Not(), operand = value)
        return ast.Expr(expr)
    futureType = tokType(idx+1)
    if futureType == T_And:
        expr = ast.BinOp(left = rawValue(idx), op = ast.And(), right = parse_value(idx+2))
        return ast.Expr(expr)
    elif futureType == T_Or:
        expr = ast.BinOp(left = rawValue(idx), op = ast.Or(), right = parse_value(idx+2))
        return ast.Expr(expr)
    elif futureType == T_Plus:
        expr = ast.BinOp(left = rawValue(idx), op = ast.Add(), right = parse_value(idx+2))
        return ast.Expr(expr)
    elif futureType == T_Minus:
        expr = ast.BinOp(left = rawValue(idx), op = ast.Sub(), right = parse_value(idx+2))
        return ast.Expr(expr)
    elif futureType == T_Times:
        expr = ast.BinOp(left = rawValue(idx), op = ast.Mult(), right = parse_value(idx+2))
        return ast.Expr(expr)
    elif futureType == T_Over:
        expr = ast.BinOp(left = rawValue(idx), op = ast.Div(), right = parse_value(idx+2))
        return ast.Expr(expr)


def rawValue(idx):
    if tokType(idx) == T_False:
        return ast.Num(n=0)
    elif tokType(idx) == T_True:
        return ast.Num(n=1)

def tokType(idx):
    return tokens[idx]['type']

def tokVal(idx):
    return tokens[idx]['value']