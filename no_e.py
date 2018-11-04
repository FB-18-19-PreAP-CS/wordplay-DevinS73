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