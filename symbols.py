TS = {}

def add_if_not_exists(name):
    if name not in TS:
        TS[name] = 0

def lookup(name):
    return TS.get(name, 0)
