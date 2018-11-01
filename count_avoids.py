def avoids(word,forbidden):
    for letter in forbidden:
        if letter in word:
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
