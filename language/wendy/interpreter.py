from lexer import tokenize

variables = {}

def run(tokens):
    for line in tokens:
        if line[0] == "let":
            var = line[1]
            value = int(line[3])
            variables[var] = value

        elif line[0] == "print":
            var = line[1]
            print(variables.get(var, 0))

if __name__ == "__main__":
    code = open("examples/hello.wy").read()
    tokens = tokenize(code)
    run(tokens)
