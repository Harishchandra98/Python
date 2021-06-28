import re

def testexp(input_string, regular_expression):
    pattern = re.compile(regular_expression)
    return bool(pattern.match(input_string))

# to check a string is matched with regular expression
