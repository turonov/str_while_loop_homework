def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    j = 0
    n = 0

    while j < len(s):
        if s[j].isdigit():
            if int (s[j]) % 2 != 0:
                n += 1
            else:
                j += 0
        j += 1
    return n

print(main("95728"))
    