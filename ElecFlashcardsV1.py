import os, random
user = os.getlogin()
path = os.getcwd()
if os.path.isdir(path + '/Details') == False:
    os.mkdir(path + '/Details/')
while True:
    counter = 0
    CardLists = os.listdir(path + "/Details/")
    for CardList in CardLists:
        print("[" + str(counter) + "] " + CardList)
        counter += 1
    choice = input("Select which cardlist you want to use, enter [c] to create a new list or [e] to exit: ")
    if choice == "c":
        choice = input("What do you want to name it?: ")
        f = open(path + "/Details/" + choice, "a")
        f.write("\n")
        while True:
            choice = input("Enter what would you like to be the flashcard hint, or [r] to return to the start: ")
            if choice == "r":
                f.write("END\n")
                f.close()
                counter = 0
                CardLists = os.listdir(path + "/Details/")
                for CardList in CardLists:
                    print("[" + str(counter) + "] " + CardList)
                    counter += 1
                choice = input("Select which cardlist you want to use, enter [c] to create a new list or [e] to exit: ")
                break
            else:
                f.write(choice+"\n")
            choice = input("Enter the answer for the card: ")
            f.write(choice)
            f.write('\n\n')
    elif choice == "e":
        exit()
    print(CardLists[int(choice)] + " selected.")

    f  = open(path + "/Details/" + CardLists[int(choice)], "r")
    contents = f.readlines()

    position = 0
    WordPositions = []
    for line in contents:
        if line == "\n" and contents[position+1] != "END\n":
            #print(contents[position+1])
            WordPositions.append(position+1)
        position += 1

    #print(WordPositions)

    skipped=False
    ExhaustedCards = []
    while True:
        if skipped == False:
            choice = input("Enter [n] for next card, [e] to exit: ")
            skipped = True
        else:
            choice = "n"
        if choice == "n":
            randint = random.randint(0,len(WordPositions)-1)
            if randint not in ExhaustedCards:
                print(contents[WordPositions[randint]].replace('\n',''))
                choice = input("Reveal answer? (enter anything): ")
                counter = 1
                while True:
                    if contents[WordPositions[randint] + counter] != "\n":
                        print(contents[WordPositions[randint] + counter].replace('\n', ''))
                    elif contents[WordPositions[randint] + counter] == "\n":
                        break
                    else:
                        print("idk wtf happened bro, this was the line: " + contents[WordPositions[randint] + counter])
                    counter += 1
                choice = input("were you correct [y/n]: ")
                if choice == "y":
                    ExhaustedCards.append(randint)
            elif len(ExhaustedCards) == len(WordPositions):
                print("All cards completed.")
                break
            else:
                #print("Already showed " + contents[WordPositions[randint]].replace('\n',''))
                skipped=True
        elif choice == "e":
            f.close()
            exit()