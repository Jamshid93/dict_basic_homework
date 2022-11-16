def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    answer={"LETTERS":0, "DIGITS":0}
    for i in txt:
        if i.isalpha():
            answer["LETTERS"]+=1
        elif i.isdigit():
            answer["DIGITS"]+=1
    return answer
print(count_all("python foundations 2022"))