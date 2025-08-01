def upper(s):
    return str(s).upper()

def lower(s):
    return str(s).lower()

def split(s, sep=None):
    return str(s).split(sep)

def join(lst, sep=""):
    return sep.join(map(str, lst))

def replace(s, old, new):
    return str(s).replace(old, new)

def find(s, sub):
    return str(s).find(sub)

def startswith(s, prefix):
    return str(s).startswith(prefix)

def endswith(s, suffix):
    return str(s).endswith(suffix)

def strip(s):
    return str(s).strip()

def len(s):
    return len(str(s))
