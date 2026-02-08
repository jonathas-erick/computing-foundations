def eval_ast(node, variables):

    if node.__class__.__name__ == "Number":
        return node.value
    
    if node.__class__.__name__ == "String":
        return node.value

    if node.__class__.__name__ == "Variable":
        return variables.get(node.name, 0)

    if node.__class__.__name__ == "BinOp":
        left = eval_ast(node.left, variables)
        right = eval_ast(node.right, variables)

        if node.op == "+":
            return left + right
        if node.op == "-":
            return left - right
        if node.op == "*":
            return left * right
        if node.op == "/":
            return left // right
