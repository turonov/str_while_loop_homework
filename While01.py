def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    d = 0
    while a<len(s):
        if s[a].isdigit():
            d += 1
        a += 1   
    return a

print(main("kdk551"))