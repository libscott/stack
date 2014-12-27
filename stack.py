
stack = []

while True:
    for s in stack:
        print s
    try:
        line = raw_input("> ")
    except EOFError:
        break
    if not line and stack:
        stack.pop()
    elif line:
        stack.append(line)

print
