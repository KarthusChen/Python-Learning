def split_it_up(a_string, sep):
    # Initialize index to -1
    index = -1
    
    # Search for the first occurrence of sep in a_string
    for i in range(len(a_string) - len(sep) + 1):
        if a_string[i:i+len(sep)] == sep:
            index = i
            break
    
    # If separator is found, split the string
    if index != -1:
        return (a_string[:index], sep, a_string[index+len(sep):])
    else:
        # If not found, return the string and two empty strings
        return (a_string, '', '')

# Testing the function
print(split_it_up("hello world", " "))  # ('hello', ' ', 'world')
print(split_it_up("hello world", "wo"))  # ('hello ', 'wo', 'rld')
print(split_it_up("hello world", "r"))  # ('hello wo', 'r', 'ld')
print(split_it_up("hello world, I am ready to program", " "))  # ('hello', ' ', 'world, I am ready to program')
print(split_it_up("hello world", "|"))  # ('hello world', '', '')
