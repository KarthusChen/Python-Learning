def letter_frequency(s):
    freq_dict = {}
    for letter in s:
        if letter in freq_dict:
            freq_dict[letter] += 1
        else:
            freq_dict[letter] = 1
    print(freq_dict)

# Example call to the function with the string "happy"
letter_frequency("happy")

# Example call to the function with the longer string
letter_frequency("pneumonoultramicroscopicsilicovolcanoconiosis")
