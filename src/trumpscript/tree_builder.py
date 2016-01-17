from src.trumpscript.constants import *
import ast

def error():
    print("YOURE FIRED")
    exit()

def tree_builder(tokens):
    variableNames = set()

    def tokenValue(idx):
        ty = tokens[idx+1]['type']
        if(ty == )

    def tokenRawValue(idx):
        tokType = tokens[idx]['type']
        tokVal = tokens[idx]['value']
        if tokType == T_Word:
            return ast.expr(ast.Name(id=tokVal, ctx=ast.Load()))
        elif tokType == T_Num:
            ast.Num(n = tokVal)

    def stmt(idx):
        tree = ast.parse("")
        exec(compile(tree, filename="<ast>", mode="exec"))

        if tokens[idx]['type'] == T_Make:
            if tokens[idx+1]['type'] != T_Word:
                error()
            variable = tokens[idx+1]['value']
            findNotGarbage(idx+2)
            value = tokenValue(idx+2)
            node = ast.assign(targets = [ast.Name(id = variable, ctx= ast.Store())], value = ast.Num(n=1))
