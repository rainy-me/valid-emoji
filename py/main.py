import os
import ast

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "../emoji.txt")

with open(filename) as f:
    [_, *emojis] = f.read().split('\n')

as_script = []
no_error = []

for emoji in emojis:
    try:
        code = ast.parse(emoji)
        as_script.append(emoji)
    except:
        continue

    try:
        eval(emoji)
        no_error.append(emoji)
    except:
        pass

print("valid as script:")
print(as_script)
print("\nruns without error:")
print(no_error)
