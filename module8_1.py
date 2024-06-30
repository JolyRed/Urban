def add_everything_up(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return str(a) + str(b)
    return a + b
