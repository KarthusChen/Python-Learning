def avg(*args):
    """
    Calculate the average of a variable number of numeric arguments.

    Returns:
        float: The average of the arguments, or None if no arguments are provided.
    """
    if not args:  
        return None
    return sum(args) / len(args)

print(avg(1, 2, 3))
print(avg())
