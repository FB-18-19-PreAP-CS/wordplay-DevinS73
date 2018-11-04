def at_least():
    with open("words.txt") as file:
            for line in file:
                for word in line.strip().split():
                    if len(word)>=20:
                        print(word)
def has_no_e(word):
    if 'e' not in word.lower():
        return True
def no_e():
    noe=0
    total=0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if has_no_e(word):
                    noe+=1
                total+=1
    print('{}'.format(noe/total*100))
def avoids(word,forbidden):
    for letter in forbidden:
        if letter.lower() in word.lower():
            return False
    return True
def count_avoids():
    count=0
    forbidden=input('Input the forbidden letters: ')
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if avoids(word,forbidden):
                    count+=1
    return count
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
def is_abecedarian(word):
    for i in range(len(word)):
        for j in word[i:]:
            if word[i].lower()>j.lower():
                return False
    return True
def count_abecedarian():
    count=0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if is_abecedarian(word):
                    count+=1
    print(count)