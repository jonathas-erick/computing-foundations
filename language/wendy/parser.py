from ast_nodes import Number, Variable, BinOp, String

def parse_expression(tokens):

    if len(tokens) == 1:
        token = tokens[0]

        if token.isdigit():
            return Number(int(token))

        
        if token.startswith('"') or " " in token:
            return String(token)

        return Variable(token)

    left = parse_expression([tokens[0]])
    op = tokens[1]
    right = parse_expression(tokens[2:])

    return BinOp(left, op, right)
