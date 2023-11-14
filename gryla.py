import os.path
import random
grylaAlive = True
playerAlive = True
chestOpen = False
taxesFromkingGeorgeitem = False
grylaKey = False



while True: 
    print('The Scenario')     
    path = 'grylascenario.txt' 

    infile = open(path, 'r')

    readFile = infile.read()
    print(readFile)

    #setting off (part 2)
    
    path = 'grylasettingoff.txt'
    infile = open(path, 'r')

    readFile = infile.read()
    print(readFile)

    settingInput = input('Please respond with a corresponding number:')
    if settingInput == "2":
                         print('Instead of facing your fears, you run, forever to be tormented by both Grÿla and your poor decision making.')
                         print()
                         print('--> If you would like to try again after running away, please press "r"<--')
                         print('--> If you would like to quit, press "x" <--') 
                         userInput = input() 
                         if userInput == "x":
                            quit()
                         if userInput == "r":
                             continue
                    
                         else:
                             while True:
                                 print()
                                 print()
                                 print('--> That input is not understood, would you like to restart from the beginning <--')
                                 print('--> Press "r" to restart from checkpoint or "x" to quit <--')
                                 print()
                                 userInput = input()
                                 if userInput == "x":
                                         quit()
                                 if userInput == "r":
                                     while False:
                                         continue



                                        
    if settingInput == "1":
        print('You continue your travels by opening the door')
    
    else:
         print()
         print()
         print('--> That input is not understood, would you like to restart from the beginning <--')
         print('--> Press "r" to restart from checkpoint or "x" to quit <--')
         print()
         userInput = input()
         if userInput == "x":
             quit()
         if userInput == "r":
             continue
         else:
             print()
             print()
             print('--> That input is not understood, would you like to restart from the beginning <--')
             print('--> Press "r" to restart from checkpoint or "x" to quit <--')
             print()
             userInput = input()
             if userInput == "x":
                 quit()
             if userInput == "r":
                 continue
             else:
                 print()
                 print('Ok, hopefully, third time is the charm for you. Now please:')
                 print()
                 print('--> Press "r" to restart from checkpoint or "x" to quit <--')
                 print()
                 userInput = input()
                 if userInput == "x":
                     quit()
                 if userInput == "r":
                     continue
                 else:
                     print()
                     print('No, there is no secret code built into this. Stop searching.')
                     print()
                     print('--> Press "r" to restart from checkpoint or "x" to quit <--')
                     print()
                     userInput = input()
                     if userInput == "x":
                         quit()
                     if userInput == "r":
                         continue
                     else:
                         print()
                         print('Oh, you want a secret, do you? Do it again, see what happens.')
                         print('--> Press "r" to restart from checkpoint or "x" to quit <--')
                         print()
                         userInput = input()
                         if userInput == "x":
                             quit()
                         if userInput == "r":
                             continue
                         else:
                            print()
                            print()
                            print('--> Please press any key to find your secret gift <--')

                            userInput = input()
                            if userInput == "x":
                                quit()
                            else:
                                quit()


#entryway begins
    if settingInput == "1":                        
        path = 'gencounter.txt'
        infile = open(path, 'r')

        readFile = infile.read()
        print(readFile)

        entrywayInput = input('Please respond with a corresponding number:')
        if entrywayInput == "1":
                             print('You opened the left door to a kitchen(3)')
        if entrywayInput == "2":
                             print('You opened the right door to a bedroom(4)')
        if entrywayInput == "3":
                          print('After adventuring into the hut, you decided to end your trip. You leave to be forever tormented by both Grÿla and your poor decision making.')
                          quit()
        if entrywayInput == "4":
                             for rolls in range(1):
                                 randomDice = random.randrange(3)+1
                             if randomDice != 3:
                                 path = 'gencountertablefail.txt'
                                 infile = open(path, 'r')

                                 readFile = infile.read()
                                 print(readFile)
                                 
                             if randomDice == 3:
                                 taxesFromkingGeorge = True
                                 path = 'gencountertablesuccess.txt'
                                 infile = open(path, 'r')

                                 readFile = infile.read()
                                 print(readFile)

                                 entrywayInput = input('Please respond with a corresponding number:')
                                 if entrywayInput == "1":
                                     print('You opened the left door')
                                 if entrywayInput == "2":
                                     print('You opened the right door')
                                 if entrywayInput == "3":
                                     print('After adventuring into the hut, you decided to end your trip. You leave to be forever tormented by both Grÿla and your poor decision making.')
                                     print()
                                     print('--> If you would like to try again after running away, please press "r"<--')
                                     print('--> If you would like to quit, press "x" <--') 
                                     userInput = input() 
                                     if userInput == "x":
                                        quit()
                                     if userInput == "r":
                                         continue
                                
                                     else:
                                         while True:
                                             print()
                                             print()
                                             print('--> That input is not understood, would you like to restart from the beginning <--')
                                             print('--> Press "r" to restart from checkpoint or "x" to quit <--')
                                             print()
                                             userInput = input()
                                             if userInput == "x":
                                                 while False:
                                                     quit()
                                             if userInput == "r":
                                                 while False:
                                                     continue

                             
                                            
                     
                    #come back to check error code
                                                #add output for after table search


        if entrywayInput == "1":
            path = 'gkitchen.txt'
            infile = open(path, 'r')

            readFile = infile.read()
            print(readFile)

            kitchenInput = input('Please respond with a corresponding number:')
            if kitchenInput == "1":
                print()
                print('--> Your search reveals nothing')
                while kitchenInput =="1":
                        path = 'gkitchen.txt'
                        infile = open(path, 'r')

                        readFile = infile.read()
                        print(readFile)

                        kitchenInput = input('Please respond with a corresponding number:')
                
            if kitchenInput == "2":
                
                print()
                print('--> You decide to travel down the stairs')
                
            if kitchenInput == "3":
                path = 'entrykreturn.txt'
                infile = open(path, 'r')

                readFile = infile.read()
                print(readFile)
                    

            if kitchenInput == "4":
                print('--> After entering the kitchen, you decide the heat was too much and ran from the building. Forever to be torimented by Grÿla and your thoughts.')
                print()
                quit()
        



#bedroom
#if the player enters the bedroom first, have it state there is a door to another room
#if the player already entered the other room, state there is a door that leads to the kitchen(3) and vice versa  

   # entrywayInput2 = entrywayInput

if entrywayInput == "2":
    path = 'gbedroom.txt'
    infile = open(path, 'r')

    readFile = infile.read()
    print(readFile)

    bedroomInput = input('Please respond with a corresponding number:')

    if bedroomInput == "1":
        print('Your search turned up nothing you did not already know')
    if bedroomInput == "2":
        print('Exit back to the EntryWay (2)')
    if bedroomInput == "3":
        print ('You attempted to open the chest, but surprise surprise, a key is required.')
        print()
        while bedroomInput =="3":
            path = 'gbedroom.txt'
            infile = open(path, 'r')

            readFile = infile.read()
            print(readFile)
            kitchenInput = ('Please respond with the corresponding number') 
# if kitchenInput == "3":




            
        #cellar
    if kitchenInput == "2":
        path = 'gcellar.txt'
        infile = open(path, 'r')

        readFile = infile.read()
        print(readFile)

        cellarInput = input('Please respond with a corresponding number:')
        if cellarInput == "1":
                  print()
        if cellarInput == "2":
                  print()
        if cellarInput == "3":
                  print()
    
    #break



