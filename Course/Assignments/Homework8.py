def makeStr(s1, s2):
    # Convert the first string into a set of unique characters
    s1_chars = set(s1)
    
    # Iterate over each character in the second string
    for char in s2:
        # If a character in s2 is not found in s1_chars, print "NO" and return
        if char not in s1_chars:
            print("NO")
            return
    
    # If the loop completes without finding an unmatched character, print "YES"
    print("YES")

# Sample calls
makeStr("hello", "") # Expected output: YES
makeStr("hello", "olleloheloeloheloel") # Expected output: YES
makeStr("hello", "olleloheloteloheloel") # Expected output: NO
makeStr("")
