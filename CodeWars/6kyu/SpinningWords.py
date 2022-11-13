def spin_words(sentence):
    words = sentence.split()
    wordList = []
    for word in words:
        if len(word) >= 5:
            wordList.append(word[::-1])
        else:
            wordList.append(word)
    return " ".join(wordList)

print(spin_words("Hello my name is joe"))