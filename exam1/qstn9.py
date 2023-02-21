import re

def check_fp(inp):
    pattern = r"^[+-]?\d*.?\d+(?:[eE][+-]?\d+)?$"
    return re.match(pattern, inp) is not None

