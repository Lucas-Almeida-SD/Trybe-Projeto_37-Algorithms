def is_palindrome_recursive_aux(word):
    if len(word) == 1:
        return word
    else:
        return word[-1] + is_palindrome_recursive_aux(word[:-1])


def is_palindrome_recursive(word, low_index, high_index):
    if not isinstance(word, str) or not word:
        return False

    reversed_word = is_palindrome_recursive_aux(word)

    return reversed_word == word
