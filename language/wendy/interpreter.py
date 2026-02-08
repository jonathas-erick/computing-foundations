from parser import parse_expression
from evaluator import eval_ast

variables = {}

def evaluate_condition(line):
    a = variables.get(line[1], 0)
    op = line[2]
    b = int(line[3])

    if op == "<":
        return a < b
    if op == ">":
        return a > b
    if op == "==":
        return a == b
    return False

def run(tokens):
    i = 0

    while i < len(tokens):
        line = tokens[i]

        if line[0] == "let":
            var = line[1]
            expr_tokens = line[3:]
            ast = parse_expression(expr_tokens)
            value = eval_ast(ast, variables)
            variables[var] = value

        elif line[0] == "print":
            ast = parse_expression(line[1:])
            value = eval_ast(ast, variables)
            print(value)

        elif line[0] == "while":
            if evaluate_condition(line):
                i += 1
                continue
            else:
                i += 2
                continue

        i += 1
