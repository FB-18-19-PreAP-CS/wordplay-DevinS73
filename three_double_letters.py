def three_double_letters():
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if len(word)>=6:
                    for i in range(len(word)):
                        if i+5<=len(word)-1:
                            if (word[i].lower()==word[i+1].lower()) and (word[i+2].lower()==word[i+3].lower()) and (word[i+4].lower()==word[i+5].lower()):
                                print(word)
if __name__=='__main__':
    three_double_letters()