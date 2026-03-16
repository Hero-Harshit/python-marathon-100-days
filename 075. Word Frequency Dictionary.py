# Word Frequency Dictionary
# Take a sentence and create a dictionary showing how many times each word appears.

sentence = input("Enter a sentence: ").lower()
words = sentence.split()

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequencies:")
for word, count in frequency.items():
    print(f"{word}: {count}")
