def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    b = 0
    c = 0
    while a < len(s):
        if s[a].isdigit():
            if int(s[a])% 2 == 0:
                b +=1
        if s[a].isdigit():
            if int (s[a])%2 == 0:
                c +=1
        a+=1
    return a

print(main("85858"))