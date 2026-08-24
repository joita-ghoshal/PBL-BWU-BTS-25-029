# word frequency analyzer

text = input("Enter a sentence: ")

words = text.split()

count = {}

for word in words:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

print("Word frequency:")

for word in count:
    print(word, ":", count[word])