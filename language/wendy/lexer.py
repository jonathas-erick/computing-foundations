def tokenize(code):
    lines = code.split("\n")
    tokens = [line.strip().split() for line in lines if line.strip()]
    return tokens
