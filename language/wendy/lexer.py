import shlex

def tokenize(code):
    lines = code.split("\n")
    tokens = [shlex.split(line) for line in lines if line.strip()]
    return tokens
