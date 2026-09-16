#                #T1        Text Analyzer

# Input:

# "Python is easy and Python is powerful"

# Output:

# Total words: 7
# Unique words: 5
# Python count: 2

# Make it work for any sentence.
------------------------------------------------------------



sentence = input("Enter a sentence: ")

words = sentence.split()

total = 0
unique = []

for word in words:
    total += 1

    if word.lower() not in unique:
        unique.append(word.lower())

print("Total words:", total)
print("Unique words:", len(unique))

print("\nRepeated words:")

for word in unique:
    count = 0

    for w in words:
        if w.lower() == word:
            count += 1

    if count > 1:
        print(word, ":", count)
