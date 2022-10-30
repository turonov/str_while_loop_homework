def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    a = 0
    punctuation = '''!@#$%^&*(){}[]|._-`/?:;"'\,~'''
    while i<len(s):
        if s[i] in punctuation:
            a +=1
            
        i+=1

    return a

print(main("sa~!@####lom"))