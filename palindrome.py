def palindrome(param):
    word = param
    reversedWord = ""
    for letter in param[::-1]:
        reversedWord += letter
    if word == reversedWord:
        return True
    else:
        return False