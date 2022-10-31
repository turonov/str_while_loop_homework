def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    a = 0
    b = 0
    s=s.lower()
    while a < len(s):
        if s[a] == "a" or s[a]== "e" or s[a] == "i" or s[a]=="o" or s[a]=="u":
            b += 1
        else:
            a += 0
        a += 1   
    return b

print(main("salom"))