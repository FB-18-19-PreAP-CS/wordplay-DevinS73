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