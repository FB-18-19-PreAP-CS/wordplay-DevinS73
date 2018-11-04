def at_least():
    with open("words.txt") as file:
            for line in file:
                for word in line.strip().split():
                    if len(word)>=20:
                        print(word)