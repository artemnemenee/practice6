def is_anagram(word, word2):
    word1.replace(' ', '')
    word2.replace(' ', '')
    print(set(word), set(word2))
    if set(word) == set(word2):
        condition = True
    else:
        condition = False
    return condition
