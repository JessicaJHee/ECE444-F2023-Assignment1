def reversed(input: int):
    if not isinstance(input, int):
        raise Exception("Input is not an Integer")
    return int(str(input)[::-1])

def formatter(input: int):
    if not isinstance(input, int):
        raise Exception("Input is not an Integer")
    return bin(input), oct(input)