name = "grace hopper"

chars = set(name)
count = 0

for word in open("words.txt"):
    word = word.rstrip()
    word_chars = set(word)
    if word_chars <= chars:
        count = count + 1
        print(word)

print(count)
