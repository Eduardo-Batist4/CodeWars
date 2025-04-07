"""
# (1) - Descending Order
def descending_order(num):
    for i in str(num):
        print(i.sort(reversed=True))

descending_order(42145)
"""

# -------------------------------------------------------------------------- #
"""
def get_middle(s):
    tam = len(s)
    if tam % 2 == 0:
        return s[tam//2 - 1] + s[tam//2]
    else:
        return s[tam//2]
        
get_middle('test')
get_middle('testing')
get_middle('middle')
get_middle('a')
"""

# -------------------------------------------------------------------------- #
"""
def is_isogram(string):
    array = set()
    for i in string.lower():
        if i in array:
            return False
        array.add(i)
    return True

is_isogram("Dermatoglyphics")
is_isogram("aba")
is_isogram("moOse")
"""

# -------------------------------------------------------------------------- #
