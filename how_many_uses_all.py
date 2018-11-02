def uses_all(word,letters):
    for letter in letters:
        if letter.lower() not in word.lower():
            return False
    return True
def how_many_uses_all(letters):
    pass