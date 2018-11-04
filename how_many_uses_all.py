def uses_all(word,letters):
    for letter in letters:
        if letter.lower() not in word.lower():
            return False
    return True
def how_many_uses_all(letters):
    count=0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_all(word,letters):
                    count+=1
    print(count)