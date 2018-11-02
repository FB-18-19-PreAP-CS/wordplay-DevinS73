def uses_only(word,letters):
    for letter in word:
        if letter.lower() not in letters.lower():
            return False
    return True
def words_with_only(letters):
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_only(word,letters):
                    print(word)