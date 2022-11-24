def is_palindrome_iterative(word):
    if not isinstance(word, str) or not word:
        return False

    last_index = len(word) - 1
    reverted_word = ""

    for index in range(len(word)):
        reverted_word += word[last_index - index]

    return reverted_word == word
