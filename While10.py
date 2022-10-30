def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    c = 0
    while a < len(s):
        if s[a].isdigit():
            if int (s[a])%2==0:
                c += int (s[a])
        a +=1 
    return a

print(main("82436"))