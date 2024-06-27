def is_palindrome(chars):
  if len(chars) <= 1:
    return True
  return chars[0] == chars[-1] and is_palindrome(chars[1:-1])

print(is_palindrome('abba'))
print(is_palindrome('abcdba'))
print(is_palindrome('racecar'))

# A Man, A Plan, A Canal, Panama
print(is_palindrome('amanaplanacanalpanama'))