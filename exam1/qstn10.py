import re

def check_intlit(inp):
    pattern = r"^(0[xX][0-9a-fA-F]+)|([0-7]+)|(\d+)$"
    return re.match(pattern, inp) is not None


