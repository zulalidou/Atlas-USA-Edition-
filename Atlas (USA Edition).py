import random


statesAndCapitals = {
                    "Alabama" : "Montgomery",       "Alaska" : "Juneau",            "Arizona" : "Phoenix",          "Arkansas": "Little Rock",
                    "California" : "Sacramento",    "Colorado" : "Denver",          "Connecticut" : "Hartford",     "Delaware" : "Dover",
                    "Florida" : "Tallahassee",      "Georgia" : "Atlanta",          "Hawaii" : "Honolulu",          "Idaho" : "Boise",
                    "Illinois" : "Springfield",     "Indiana" : "Indianapolis",     "Iowa" : "Des Moines",          "Kansas" : "Topeka",
                    "Kentucky" : "Frankfort",       "Louisiana": "Baton Rouge",     "Maine" : "Augusta",            "Maryland" : "Annapolis",
                    "Massachusetts" : "Boston",     "Michigan" : "Lansing",         "Minnesota" : "St. Paul",       "Mississippi" : "Jackson",
                    "Missouri": "Jefferson City",   "Montana": "Helena",            "Nebraska" : "Lincoln",         "Nevada" : "Carson City",
                    "New Hampshire" : "Concord",    "New Jersey" : "Trenton",       "New Mexico" : "Santa Fe",      "New York" : "Albany",
                    "North Carolina" : "Raleigh",   "North Dakota" : "Bismarck",    "Ohio" : "Columbus",            "Oklahoma" : "Oklahoma City",
                    "Oregon" : "Salem",             "Pennsylvania" : "Harrisburg",  "Rhode Island" : "Providence",  "South Carolina" : "Columbia",
                    "South Dakota" : "Pierre",      "Tennessee" : "Nashville",      "Texas" : "Austin",             "Utah" : "Salt Lake City",
                    "Vermont" : "Montpelier",       "Virginia" : "Richmond",        "Washington" : "Olympia",       "West Virginia" : "Charleston",
                    "Wisconsin" : "Madison",        "Wyoming" : "Cheyenne"
                    }



'''
This function welcomes the user, and asks them to pick a mode. If the user types in the play
mode, then the function will exit
'''
def mainMenu():
    print("Welcome to Atlas (USA Edition)!", end = "\n\n")
    displayModes()

    while True:
        mode = input("\n> Please pick 1 of the modes displayed above: ")
        mode = (mode.strip()).lower()
        
        if mode != "play" and mode != "p" and mode != "instructions" and mode != "i":
            print("The mode you entered is invalid")
        else:
            if mode == "play" or mode == "p":
                break
            else:
                with open("instructions.txt", "r") as file:
                    print(file.read())

                leave = input("Enter \"exit\" to leave this mode: ")
                leave = (leave.strip()).lower()

                while leave != "exit" and leave != "x":
                    leave = input("That is incorrect. Please enter \"exit\" or \"x\" to leave this mode: ")
                    leave = (leave.strip()).lower()

                print("\n\n\n")
                displayModes()



'''
This function displays the modes that are available to the user
'''
def displayModes():
    print("-" * 12, "\n", "{:12}".format("| Play (P) |"), "\n", "-" * 12, sep = "")
    print("-" * 20, "\n", "{:20}".format("| Instructions (I) |"), "\n", "-" * 20, sep = "")



'''
This is the "main" function of the program; it asks the user to guess the capital of a state.
It does this by randomly generating a state from the keys list in the statesAndCapitals dict.

It creates 4 variables named A, B, C, & D, and assigns the answer (the capital of the state
asked) to 1 of these variables at random. The other 3 variables get assigned incorrect cities.
'''
def gamePlay():
    points = 0
    statesAlreadyAsked = []
    state = ""
    
    for turn in range(1, 51):
        A = B = C = D = "" #Multiple choice options

        state, statesAlreadyAsked = getState(state, statesAlreadyAsked)
        correctLetter = random.choice("ABCD") #Decides which multiple choice option will hold the correct answer
        
        A, B, C, D = assignAnswersToOptions(A, B, C, D, correctLetter, state)

        print("\nRound:", turn)
        print("What is the capital of ", state, "?", sep = "")
        print("A.", "{:<20}".format(A), "B.", "{:<20}".format(B))
        print("C.", "{:<20}".format(C), "D.", "{:<20}".format(D))

        guesses = 0

        while True:
            userGuess = input("\n> Type in your answer here: ")
            userGuess = (userGuess.strip()).lower()
            guesses += 1
            
            if userGuess == correctLetter.lower() or userGuess == statesAndCapitals[state].lower():
                points += 1
                print("\nCorrect!\n\n")
                break
            else:                
                if guesses is 3:
                    print("\nWrong once again. The answer was: ", statesAndCapitals[state], ".\n\n", sep = "")
                    break
                else:
                    print("Incorrect. Try again.")
                

    playerScore(points)



'''
This function generates a random state, which the program will eventually use to ask the user
to guess its capital.

The list "statesAlreadyAsked" is designed to make sure that the program doesn't keep asking
the user the capital of states that had been asked previously.
'''
def getState(state, statesAlreadyAsked):
    state = random.sample(statesAndCapitals.keys(), 1)  #The state's capital being asked
    state = state[0]    #I'm taking the 0th element of state because "random.sample(population, k)" returns a [LIST] of k items

    while state in statesAlreadyAsked:
        state = random.sample(statesAndCapitals.keys(), 1)
        state = state[0]

    statesAlreadyAsked.append(state)

    return state, statesAlreadyAsked



'''
This function assigns the capital city of the state being asked to 1 of the options. The remaining
3 options get assigned "wrongCities".
'''
def assignAnswersToOptions(A, B, C, D, correctLetter, state):
    wrongAnswers = list() #Keeps 3 of the incorrect options
    
    if correctLetter == "A":
        A = statesAndCapitals[state]
    elif correctLetter == "B":
        B = statesAndCapitals[state]
    elif correctLetter == "C":
        C = statesAndCapitals[state]
    elif correctLetter == "D":
        D = statesAndCapitals[state]


    while len(wrongAnswers) < 3:
        wrongCity = random.sample(list(statesAndCapitals.values()), 1)
        wrongCity = wrongCity[0]

        while wrongCity in wrongAnswers or wrongCity == statesAndCapitals[state]:
            wrongCity = random.sample(list(statesAndCapitals.values()), 1)
            wrongCity = wrongCity[0]

        wrongAnswers.append(wrongCity)


    if A == "":
        A = wrongAnswers[0]
        wrongAnswers.remove(A)
    if B == "":
        B = wrongAnswers[0]
        wrongAnswers.remove(B)
    if C == "":
        C = wrongAnswers[0]
        wrongAnswers.remove(C)
    if D == "":
        D = wrongAnswers[0]
        wrongAnswers.remove(D)

    return A, B, C, D



'''
It prints the user's points
'''
def playerScore(points):
    print("\n\nThanks for playing!\nHere's your score:", points, "/ 50")
    


if __name__ == "__main__":
    mainMenu()
    gamePlay()
