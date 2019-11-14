import random
import winsound
import tkinter as tk

statesAndCapitals = {
    "Alabama" : ("Montgomery"),     "Alaska" : ("Juneau"),          "Arizona" : ("Phoenix"),            "Arkansas" : ("Little Rock"),       "California" : ("Sacramento"),
    "Colorado" : ("Denver"),        "Connecticut" : ("Hartford"),   "Delaware" : ("Dover"),             "Florida" : ("Tallahassee"),        "Georgia" : ("Atlanta"),
    "Hawaii" : ("Honolulu"),        "Idaho" : ("Boise"),            "Illinois" : ("Springfield"),       "Indiana" : ("Indianapolis"),       "Iowa" : ("Des Moines"),
    "Kansas" : ("Topeka"),          "Kentucky" : ("Frankfort"),     "Louisiana" : ("Baton Rouge"),      "Maine" : ("Augusta"),              "Maryland" : ("Annapolis"),
    "Massachusetts" : ("Boston"),   "Michigan" : ("Lansing"),       "Minnesota" : ("St. Paul"),         "Mississippi" : ("Jackson"),        "Missouri" : ("Jefferson City"),
    "Montana" : ("Helena"),         "Nebraska" : ("Lincoln"),       "Nevada" : ("Carson City"),         "New Hampshire" : ("Concord"),      "New Jersey" : ("Trenton"),
    "New Mexico" : ("Santa Fe"),    "New York" : ("Albany"),        "North Carolina" : ("Raleigh"),     "North Dakota" : ("Bismarck"),      "Ohio" : ("Columbus"),
    "Oklahoma" : ("Oklahoma City"), "Oregon" : ("Salem"),           "Pennsylvania" : ("Harrisburg"),    "Rhode Island" : ("Providence"),    "South Carolina" : ("Columbia"),
    "South Dakota" : ("Pierre"),    "Tennessee" : ("Nashville"),    "Texas" : ("Austin"),               "Utah" : ("Salt Lake City"),        "Vermont" : ("Montpelier"),
    "Virginia" : ("Richmond"),      "Washington" : ("Olympia"),     "West Virginia" : ("Charleston"),   "Wisconsin" : ("Madison"),          "Wyoming" : ("Cheyenne")
}


usFlagsNSeals = {
    "Alabama" : ("AL_Flag.gif", "AL_Seal.png"),         "Alaska" : ("AK_Flag.gif", "AK_Seal.gif"),          "Arizona" : ("AZ_Flag.gif", "AZ_Seal.gif"),         "Arkansas" : ("AR_Flag.gif", "AR_Seal.gif"),
    "California" : ("CA_Flag.gif", "CA_Seal.gif"),      "Colorado" : ("CO_Flag.gif", "CO_Seal.gif"),        "Connecticut" : ("CT_Flag.gif", "CT_Seal.gif"),     "Delaware" : ("DE_Flag.gif", "DE_Seal.gif"),
    "Florida" : ("FL_Flag.gif", "FL_Seal.gif"),         "Georgia" : ("GA_Flag.gif", "GA_Seal.gif"),         "Hawaii" : ("HI_Flag.gif", "HI_Seal.gif"),          "Idaho" : ("ID_Flag.gif", "ID_Seal.gif"),
    "Illinois" : ("IL_Flag.gif", "IL_Seal.gif"),        "Indiana" : ("IN_Flag.gif", "IN_Seal.gif"),         "Iowa" : ("IA_Flag.gif", "IA_Seal.gif"),            "Kansas" : ("KS_Flag.gif", "KS_Seal.gif"),
    "Kentucky" : ("KY_Flag.gif", "KY_Seal.gif"),        "Louisiana" : ("LA_Flag.gif", "LA_Seal.gif"),       "Maine" : ("ME_Flag.gif", "ME_Seal.gif"),           "Maryland" : ("MD_Flag.gif", "MD_Seal.gif"),
    "Massachusetts" : ("MA_Flag.gif", "MA_Seal.gif"),   "Michigan" : ("MI_Flag.gif", "MI_Seal.gif"),        "Minnesota" : ("MN_Flag.gif", "MN_Seal.png"),       "Mississippi" : ("MS_Flag.gif", "MS_Seal.gif"),                                                                                                                                                                               
    "Missouri" : ("MO_Flag.gif", "MO_Seal.gif"),        "Montana" : ("MT_Flag.gif", "MT_Seal.gif"),         "Nebraska" : ("NE_Flag.gif", "NE_Seal.gif"),        "Nevada" : ("NV_Flag.gif", "NV_Seal.gif"),
    "New Hampshire" : ("NH_Flag.gif", "NH_Seal.gif"),   "New Jersey" : ("NJ_Flag.gif", "NJ_Seal.png"),      "New Mexico" : ("NM_Flag.gif", "NM_Seal.gif"),      "New York" : ("NY_Flag.gif", "NY_Seal.gif"),
    "North Carolina" : ("NC_Flag.gif", "NC_Seal.gif"),  "North Dakota" : ("ND_Flag.gif", "ND_Seal.gif"),    "Ohio" : ("OH_Flag.png", "OH_Seal.png"),            "Oklahoma" : ("OK_Flag.gif", "OK_Seal.gif"),
    "Oregon" : ("OR_Flag.gif", "OR_Seal.gif"),          "Pennsylvania" : ("PA_Flag.gif", "PA_Seal.gif"),    "Rhode Island" : ("RI_Flag.gif", "RI_Seal.gif"),    "South Carolina" : ("SC_Flag.gif", "SC_Seal.gif"),
    "South Dakota" : ("SD_Flag.gif", "SD_Seal.gif"),    "Tennessee" : ("TN_Flag.gif", "TN_Seal.gif"),       "Texas" : ("TX_Flag.gif", "TX_Seal.gif"),           "Utah" : ("UT_Flag.gif", "UT_Seal.gif"),
    "Vermont" : ("VT_Flag.gif", "VT_Seal.gif"),         "Virginia" : ("VA_Flag.gif", "VA_Seal.gif"),        "Washington" : ("WA_Flag.gif", "WA_Seal.gif"),      "West Virginia" : ("WV_Flag.gif", "WV_Seal.gif"),
    "Wisconsin" : ("WI_Flag.gif", "WI_Seal.gif"),       "Wyoming" : ("WY_Flag.gif", "WY_Seal.gif")
}


'''
self = Initialization class object
master = root = tkinter object

self.(itemName) is something I use only for the MainMenu object 'app' created 
- Makes it easy for me to access those widgets in different class functions
'''
class MainMenu:
    #############################################################################
    # This function sets up the (Main menu / welcoming page) of the application #
    #############################################################################
    def __init__(self, master):
        self.master = master
        
        self.mainMenuFr = tk.Frame(self.master, bg = "black")
        self.mainMenuFr.place(relwidth = 1.0, relheight = 1.0)

        startBtn = tk.Button(self.mainMenuFr, text = "Start", font = "Arial 18", bg = "black", fg = "white", bd = 0, activebackground = "black", cursor = "hand2", command = lambda: Gameplay.__init__(self, master))
        startBtn.place(relx = 0.12, relwidth = 0.1, relheight = 0.05)

        instructionsBtn = tk.Button(self.mainMenuFr, text = "Instructions", font = "Arial 18", bg = "black", fg = "white", bd = 0, activebackground = "black", cursor = "hand2", command = lambda: Instructions.__init__(self, master))
        instructionsBtn.place(relx = 0.34, relwidth = 0.1, relheight = 0.05)

        creditsBtn = tk.Button(self.mainMenuFr, text = "Credits", font = "Arial 18", bg = "black", fg = "white", bd = 0, activebackground = "black", cursor = "hand2", command = lambda: Credits.__init__(self, master))
        creditsBtn.place(relx = 0.56, relwidth = 0.1, relheight = 0.05)

        quitBtn = tk.Button(self.mainMenuFr, text = "Quit", font = "Arial 18", bg = "black", fg = "white", bd = 0, activebackground = "black", cursor = "hand2", command = master.destroy)
        quitBtn.place(relx = 0.78, relwidth = 0.1, relheight = 0.05)

        usaMapImg = tk.PhotoImage(file = "usaMap.png")
        mapLbl = tk.Label(self.mainMenuFr, image = usaMapImg, bg = "white")
        mapLbl.photo = usaMapImg
        mapLbl.place(rely = 0.05, relwidth = 1.0, relheight = 0.95)


class Instructions:
    ##################################################################
    # This function sets up the Instructions page of the application #
    ##################################################################
    def __init__(self, master):
        self.instructionsFr = tk.Frame(self.master, bg = "white")
        self.instructionsFr.place(relwidth = 1.0, relheight = 1.0)

        topBarLbl = tk.Label(self.instructionsFr, bg = "black")
        topBarLbl.place(relwidth = 1.0, relheight = 0.05)
        
        returnBtn = tk.Button(topBarLbl, text = "Return", font = "Arial 18", bg = "black", fg = "white", bd = 0, activebackground = "black", cursor = "hand2", command = self.instructionsFr.destroy)
        returnBtn.place(relx = 0.12, relwidth = 0.1, relheight = 1.0)


        bottomLeftFr = tk.Frame(self.instructionsFr, bg = "orange red")
        bottomLeftFr.place(relx = 0.02, rely = 0.1, relwidth = 0.13, relheight = 0.2)

        overviewBtn = tk.Button(bottomLeftFr, text = " > Overview", font = "Arial 18", bg = "ghost white", bd = 1, activebackground = "white", cursor = "hand2", anchor = "w", command = lambda: Instructions.overviewMode(self, bottomRightFr))
        overviewBtn.place(relx = 0.005, rely = 0.005, relwidth = 0.99, relheight = 0.495)

        hintsBtn = tk.Button(bottomLeftFr, text = " > Hints", font = "Arial 18", bg = "ghost white", bd = 1, activebackground = "white", cursor = "hand2", anchor = "w", command = lambda: Instructions.hints1Mode(self, bottomRightFr))
        hintsBtn.place(relx = 0.005, rely = 0.5, relwidth = 0.99, relheight = 0.495)


        bottomRightFr = tk.Frame(self.instructionsFr, bg = "black")
        bottomRightFr.place(relx = 0.17, rely = 0.1, relwidth = 0.81, relheight = 0.85)

        instructionsImg = tk.PhotoImage(file = "instructionSymbol.png")
        instructionsLbl = tk.Label(bottomRightFr, image = instructionsImg, bg = "white")
        instructionsLbl.photo = instructionsImg
        instructionsLbl.place(relx = 0.001, rely = 0.001, relwidth = 0.998, relheight = 0.998)


    ##################################################
    # This function explains the aim of the app/game #
    ##################################################
    def overviewMode(self, bottomRightFr):
        titleLbl = tk.Label(bottomRightFr, text = "Overview", font = ("Arial", 25), bg = "orange red")
        titleLbl.place(relx = 0.001, rely = 0.001, relwidth = 0.998, relheight = 0.099)

        overviewImg = tk.PhotoImage(file = "overview.png")
        overviewImg2 = overviewImg.subsample(2)
        imgLbl = tk.Label(bottomRightFr, image = overviewImg2, bg = "white")
        imgLbl.photo = overviewImg2
        imgLbl.place(relx = 0.001, rely = 0.1, relwidth = 0.549, relheight = 0.899)        

        overviewTxt = tk.Text(bottomRightFr, bg = "white", wrap = "word", font = "Arial 15", bd = 0)
        overviewTxt.insert("insert", "\n\nThis is a quiz that tests the player's knowledge of the capital cities of the 50 states of the United States of America. " +
                                "Since the U.S. is made up of 50 states, there will be 50 questions. (The image on the left shows an example of what the player will see every time they are asked a question.)")
        overviewTxt.tag_add("Description", "1.0", "9.end")
        overviewTxt.tag_config("Description", font = "Tahoma 20", justify = "center", offset = 20)
        overviewTxt.configure(state = "disabled")  # To make the text uneditable
        overviewTxt.place(relx = 0.55, rely = 0.1, relwidth = 0.449, relheight = 0.899)


    #######################################################
    # This function explains how the Coin Flip hint works #
    #######################################################                        
    def hints1Mode(self, bottomRightFr):
        titleLbl = tk.Label(bottomRightFr, text = "Hints", font = ("Arial", 25), bg = "orange red")
        titleLbl.place(relx = 0.001, rely = 0.001, relwidth = 0.998, relheight = 0.099)

        rightArrowImg1 = tk.PhotoImage(file = "rightArrow.png")
        rightArrowImg2 = rightArrowImg1.subsample(3)
        nextBtn = tk.Button(titleLbl, bg = "orange red", image = rightArrowImg2, bd=0, cursor = "hand2", activebackground = "orange red", command = lambda: Instructions.hints2Mode(self, bottomRightFr))
        nextBtn.photo = rightArrowImg2
        nextBtn.place(relx = 0.95, relwidth = 0.05, relheight = 1.0)


        coinFlipImg1 = tk.PhotoImage(file = "coinFlipImg.png")
        coinFlipImg2 = coinFlipImg1.subsample(2)
        coinFlipLbl = tk.Label(bottomRightFr, image = coinFlipImg2, bg = "white")
        coinFlipLbl.photo = coinFlipImg2
        coinFlipLbl.place(relx = 0.001, rely = 0.1, relwidth = 0.549, relheight = 0.899)
        
        coinFlipTxt = tk.Text(bottomRightFr, bg = "white", wrap = "word", font = "Arial 15", bd = 0)
        coinFlipTxt.insert("insert", "Coin Flip")
        coinFlipTxt.tag_add("title", "1.0", "1.end")
        coinFlipTxt.tag_config("title", font = "Tahoma 25", justify = "center")

        coinFlipTxt.insert("insert", "\n\nThe \"COIN FLIP\" button will return the user an answer to a question, but there is a catch: it only works half of the time. " +
                                     "When this button is clicked, it will give the correct answer to the question 50% of the time and an incorrect answer to the " +
                                     "question for the remaining 50% of the time, so it's up to the player to decide whether or not to trust it. (Can only be used once.)")
        coinFlipTxt.tag_add("Description", "2.0", "99.end")
        coinFlipTxt.tag_config("Description", font = "Tahoma 20", justify = "center", offset = 18)
        coinFlipTxt.configure(state = "disabled")  # To make the text uneditable
        coinFlipTxt.place(relx = 0.55, rely = 0.1, relwidth = 0.449, relheight = 0.899)


    #########################################################
    # This function explains how the Eliminate 1 hint works #
    ######################################################### 
    def hints2Mode(self, bottomRightFr):
        titleLbl = tk.Label(bottomRightFr, text = "Hints", font = ("Arial", 25), bg = "orange red")
        titleLbl.place(relx = 0.001, rely = 0.001, relwidth = 0.998, relheight = 0.099)

        leftArrowImg1 = tk.PhotoImage(file = "leftArrow.png")
        leftArrowImg2 = leftArrowImg1.subsample(3)
        prevBtn = tk.Button(titleLbl, bg = "orange red", image = leftArrowImg2, bd=0, cursor = "hand2", activebackground = "orange red", command = lambda: Instructions.hints1Mode(self, bottomRightFr))
        prevBtn.photo = leftArrowImg2
        prevBtn.place(relwidth = 0.05, relheight = 1.0)

        rightArrowImg1 = tk.PhotoImage(file = "rightArrow.png")
        rightArrowImg2 = rightArrowImg1.subsample(3)
        nextBtn = tk.Button(titleLbl, bg = "orange red", image = rightArrowImg2, bd=0, cursor = "hand2", activebackground = "orange red", command = lambda: Instructions.hints3Mode(self, bottomRightFr))
        nextBtn.photo = rightArrowImg2
        nextBtn.place(relx = 0.95, relwidth = 0.05, relheight = 1.0)


        eliminate1Img1 = tk.PhotoImage(file = "eliminate1Img.png")
        eliminate1Img2 = eliminate1Img1.subsample(2)
        eliminate1Lbl = tk.Label(bottomRightFr, image = eliminate1Img2, bg = "white")
        eliminate1Lbl.photo = eliminate1Img2
        eliminate1Lbl.place(relx = 0.001, rely = 0.1, relwidth = 0.549, relheight = 0.899)
        
        eliminate1Txt = tk.Text(bottomRightFr, bg = "white", wrap = "word", font = "Arial 15", bd = 0)
        eliminate1Txt.insert("insert", "Eliminate 1")
        eliminate1Txt.tag_add("title", "1.0", "1.end")
        eliminate1Txt.tag_config("title", font = "Tahoma 25", justify = "center")

        eliminate1Txt.insert("insert", "\n\n\n\n\nThe \"ELIMINATE 1\" button turns the color of one of the wrong answers to red, which helps the player eliminate one of the options." +
                            "(Can only be used once.)")
        eliminate1Txt.tag_add("Description", "3.0", "99.end")
        eliminate1Txt.tag_config("Description", font = "Tahoma 20", justify = "center", offset = 20)
        eliminate1Txt.configure(state = "disabled")  # To make the text uneditable
        eliminate1Txt.place(relx = 0.55, rely = 0.1, relwidth = 0.449, relheight = 0.899)


    ####################################################
    # This function explains how the Letter hint works #
    #################################################### 
    def hints3Mode(self, bottomRightFr):
        titleLbl = tk.Label(bottomRightFr, text = "Hints", font = ("Arial", 25), bg = "orange red")
        titleLbl.place(relx = 0.001, rely = 0.001, relwidth = 0.998, relheight = 0.099)

        leftArrowImg1 = tk.PhotoImage(file = "leftArrow.png")
        leftArrowImg2 = leftArrowImg1.subsample(3)
        prevBtn = tk.Button(titleLbl, bg = "orange red", image = leftArrowImg2, bd=0, cursor = "hand2", activebackground = "orange red", command = lambda: Instructions.hints2Mode(self, bottomRightFr))
        prevBtn.photo = leftArrowImg2
        prevBtn.place(relwidth = 0.05, relheight = 1.0)


        letterImg1 = tk.PhotoImage(file = "letterImg.png")
        letterImg2 = letterImg1.subsample(2)
        letterLbl = tk.Label(bottomRightFr, image = letterImg2, bg = "white")
        letterLbl.photo = letterImg2
        letterLbl.place(relx = 0.001, rely = 0.1, relwidth = 0.549, relheight = 0.899)
        
        letterTxt = tk.Text(bottomRightFr, bg = "white", wrap = "word", font = "Arial 15", bd = 0)
        letterTxt.insert("insert", "Letter")
        letterTxt.tag_add("title", "1.0", "1.end")
        letterTxt.tag_config("title", font = "Tahoma 25", justify = "center")

        letterTxt.insert("insert", "\n\n\n\n\nThe \"LETTER\" button gives the player 1 letter in the answer to the question. (Can only be used once.)")
        letterTxt.tag_add("Description", "3.0", "99.end")
        letterTxt.tag_config("Description", font = "Tahoma 20", justify = "center", offset = 20)
        letterTxt.configure(state = "disabled")  # To make the text uneditable
        letterTxt.place(relx = 0.55, rely = 0.1, relwidth = 0.449, relheight = 0.899)



class Credits:
    ##########################################
    # This function sets up the Credits page #
    ########################################## 
    def __init__(self, master):
        self.creditsFr = tk.Frame(self.master, bg = "white")
        self.creditsFr.place(relwidth = 1.0, relheight = 1.0)

        topBarLbl = tk.Label(self.creditsFr, bg = "black")
        topBarLbl.place(relwidth = 1.0, relheight = 0.05)
        
        returnBtn = tk.Button(topBarLbl, text = "Return", font = "Arial 18", bg = "black", fg = "white", bd = 0, activebackground = "black", cursor = "hand2", command = self.creditsFr.destroy)
        returnBtn.place(relx = 0.12, relwidth = 0.1, relheight = 1.0)
        

        bottomLeftFr = tk.Frame(self.creditsFr, bg = "orange red")
        bottomLeftFr.place(relx = 0.02, rely = 0.1, relwidth = 0.13, relheight = 0.2)

        imagesBtn = tk.Button(bottomLeftFr, text = " > Images", font = "Arial 18", bg = "ghost white", bd = 1, activebackground = "white", cursor = "hand2", anchor = "w", command = lambda: Credits.images(self, bottomRightFr))
        imagesBtn.place(relx = 0.005, rely = 0.005, relwidth = 0.99, relheight = 0.495)

        soundsBtn = tk.Button(bottomLeftFr, text = " > Sounds", font = "Arial 18", bg = "ghost white", bd = 1, activebackground = "white", cursor = "hand2", anchor = "w", command = lambda: Credits.sounds(self, bottomRightFr))
        soundsBtn.place(relx = 0.005, rely = 0.5, relwidth = 0.99, relheight = 0.495)


        bottomRightFr = tk.Frame(self.creditsFr, bg = "black")
        bottomRightFr.place(relx = 0.17, rely = 0.1, relwidth = 0.81, relheight = 0.85)

        instructionsImg = tk.PhotoImage(file = "creditsImg.png")
        instructionsLbl = tk.Label(bottomRightFr, image = instructionsImg, bg = "white")
        instructionsLbl.photo = instructionsImg
        instructionsLbl.place(relx = 0.001, rely = 0.001, relwidth = 0.998, relheight = 0.998)


    ###################################################################################################
    # This function credits the images used (that weren't copyright free or that need to be credited) #
    ###################################################################################################
    def images(self, bottomRightFr):
        titleLbl = tk.Label(bottomRightFr, text = "Image", font = ("Arial", 25), bg = "orange red")
        titleLbl.place(relx = 0.001, rely = 0.001, relwidth = 0.998, relheight = 0.099)


        img1 = tk.PhotoImage(file = "usaMap.png")
        img2 = img1.subsample(2)
        imgLbl = tk.Label(bottomRightFr, image = img2, bg = "white")
        imgLbl.photo = img2
        imgLbl.place(relx = 0.001, rely = 0.1, relwidth = 0.499, relheight = 0.899)


        imageTxt = tk.Text(bottomRightFr, bg = "white", bd = 0)
        imageTxt.insert("insert", "\nSpitfire19 from Wikipedia created this image")
        imageTxt.tag_add("description", "2.0", "2.end")
        imageTxt.tag_config("description", font = "Tahoma 20")

        imageTxt.insert("insert", "\n\n(https://upload.wikimedia.org/wikipedia/commons/5/58/BlankMap-USA.png)")
        imageTxt.tag_add("link", "4.0", "4.end")
        imageTxt.tag_config("link", font = "Tahoma 12")
        
        imageTxt.config(state = "disable")
        imageTxt.place(relx = 0.5, rely = 0.1, relwidth = 0.499, relheight = 0.899)


    ###################################################################################################
    # This function credits the sounds used (that weren't copyright free or that need to be credited) #
    ###################################################################################################
    def sounds(self, bottomRightFr):
        titleLbl = tk.Label(bottomRightFr, text = "Sounds", font = ("Arial", 25), bg = "orange red")
        titleLbl.place(relx = 0.001, rely = 0.001, relwidth = 0.998, relheight = 0.099)

        soundsTxt = tk.Text(bottomRightFr, bg = "white", bd = 0)

        soundsTxt.insert("insert", "\n1.) LittleRainySeasons from freesound.org created this sound: ")
        soundsTxt.tag_add("credit_1", "2.0", "2.end")
        soundsTxt.tag_config("credit_1", font = "Tahoma 20")

        sound1Btn = tk.Button(soundsTxt, text = "Click Me", bg = "yellow", cursor = "hand2", command = lambda: winsound.PlaySound("correctSound.wav", winsound.SND_ASYNC))
        sound1Btn.place(relx = 0.7, rely = 0.03, relwidth = 0.1, relheight = 0.07)

        soundsTxt.insert("insert", "\n\n2.) RICHERlandTV from freesound.org created this sound: ")
        soundsTxt.tag_add("credit_2", "4.0", "4.end")
        soundsTxt.tag_config("credit_2", font = "Tahoma 20")

        sound2Btn = tk.Button(soundsTxt, text = "Click Me", bg = "yellow", cursor = "hand2", command = lambda: winsound.PlaySound("incorrectSound.wav", winsound.SND_ASYNC))
        sound2Btn.place(relx = 0.7, rely = 0.12, relwidth = 0.1, relheight = 0.07)

        soundsTxt.config(state = "disable")
        soundsTxt.place(relx = 0.001, rely = 0.1, relwidth = 0.998, relheight = 0.899)


class Gameplay:
    ####################################################
    # This function sets up the "Play" mode of the app #
    ####################################################
    def __init__(self, master):        
        self.playFr = tk.Frame(master)
        self.playFr.place(relwidth = 1.0, relheight = 1.0)

        ############################## The very top of the "Play" mode" ##############################
        self.correct = 0
        self.correctLbl = tk.Label(self.playFr, text = "Correct: " + str(self.correct), bg = "light green", font = "Arial 15", bd = 0)
        self.correctLbl.place(relwidth = 0.2, relheight = 0.05)
        
        self.incorrect = 0
        self.incorrectLbl = tk.Label(self.playFr, text = "Incorrect: " + str(self.incorrect), bg = "red", font = "Arial 15", bd = 0)
        self.incorrectLbl.place(relx = 0.2, relwidth = 0.2, relheight = 0.05)
        
        self.accuracy = 0
        self.accuracyLbl = tk.Label(self.playFr, text = "Accuracy: " + str(self.accuracy) + "%", bg = "yellow", font = "Arial 15", bd = 0)
        self.accuracyLbl.place(relx = 0.4, relwidth = 0.2, relheight = 0.05)
        
        self.lastMissed = "N/A"
        self.lastMissedLbl = tk.Label(self.playFr, text = "Last Missed: " + self.lastMissed, bg = "pink", font = "Arial 15", bd = 0)
        self.lastMissedLbl.place(relx = 0.6, relwidth = 0.2, relheight = 0.05)

        quitBtn = tk.Button(self.playFr, text = "Quit", bg = "gray", activebackground = "gray", font = "Arial 15", cursor = "hand2", bd = 0, command = lambda: Gameplay.quitGame(self))
        quitBtn.place(relx = 0.8, relwidth = 0.2, relheight = 0.05)
        ############################## The very top of the "Play" mode" ##############################
        

        self.bottom = tk.Canvas(self.playFr, bg = "white")
        self.bottom.place(rely = 0.05, relwidth = 1.0, relheight = 0.95)

        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        self.bottom.create_polygon(screenWidth * 0.10, screenHeight * 0.05, #1  ####################################
                                   screenWidth * 0.90, screenHeight * 0.05, #2  # My terrible attempt at drawing   #
                                   screenWidth * 0.95, screenHeight * 0.15, #3  # a rounded rectangle as the back- #
                                   screenWidth * 0.95, screenHeight * 0.75, #4  # ground                           #
                                   screenWidth * 0.90, screenHeight * 0.83, #5  ####################################
                                   screenWidth * 0.10, screenHeight * 0.83, #6
                                   screenWidth * 0.05, screenHeight * 0.75, #7
                                   screenWidth * 0.05, screenHeight * 0.15, #8
                                    fill = "orange", smooth = True, splinesteps = 1000)

        
        usaFlag = tk.PhotoImage(file = "usaFlag.gif")
        usaLabel = tk.Label(self.bottom, image = usaFlag)
        usaLabel.photo = usaFlag
        usaLabel.place(relx =  ((screenWidth/2) - (usaFlag.width()/2)) / screenWidth, rely = ((screenHeight * 0.02) / screenHeight) - 0.01)


        ############################## State Flag, Question, and State seal ##############################
        self.stateFlagLbl = tk.Label(self.bottom, bg = "orange")
        self.stateFlagLbl.place(relx = 0.1, rely = 0.15, relheight = 0.3)

        self.questionFr = tk.Frame(self.bottom, bg = "black")
        self.questionFr.place(relx = 0.3375, rely = 0.15, relwidth = 0.325, relheight = 0.3)  # <---- Modify the "borders"?

        topLbl = tk.Label(self.questionFr, text = "What is the capital city", font = "Arial 30", bg = "white")
        topLbl.place(relx = 0.005, rely = 0.005, relwidth = 0.99, relheight = 0.33)
        
        midLbl = tk.Label(self.questionFr, text = "of the state of", font = "Arial 30", bg = "white")
        midLbl.place(relx = 0.005, rely = 0.335, relwidth = 0.99, relheight = 0.33)

        bottomLbl = tk.Label(self.questionFr, text = "...", font = "Arial 30", bg = "white")
        #bottomLbl.text is modified in QnA function below
        
        self.stateSealLbl = tk.Label(self.bottom, bg = "orange")
        self.stateSealLbl.place(relx = 0.675, rely = 0.15, relheight = 0.3)
        ############################## State Flag, Question, and State seal ##############################
        

        ############################## The Hints ############################## 
        self.hintSelected = tk.StringVar()

        hintsLbl = tk.Label(self.bottom, bg = "orange")
        hintsLbl.place(relx = 0.1, rely = 0.475, relwidth = 0.8, relheight = 0.08)#(relx = 0.1, rely = 0.43, relwidth = 0.8, relheight = 0.06)

        self.coinFlipBtn = tk.Button(hintsLbl, text = "COIN FLIP", bg = "orange", activebackground = "orange", bd = 1.0, cursor = "hand2", font = "Arial 20")
        self.coinFlipBtn.place(relx = 0.075, rely = 0.1, relwidth = .25, relheight = 0.8)

        self.eliminate1Btn = tk.Button(hintsLbl, text = "ELIMINATE 1", bg = "orange", activebackground = "orange", bd = 1.0, cursor = "hand2", font = "Arial 20")
        self.eliminate1Btn.place(relx = 0.375,  rely = 0.1, relwidth = .25, relheight = 0.8)

        self.letterBtn = tk.Button(hintsLbl, text = "LETTER", bg = "orange", bd = 1.0, activebackground = "orange", cursor = "hand2", font = "Arial 20")
        self.letterBtn.place(relx = 0.675, rely = 0.1, relwidth = .25, relheight = 0.8)
        ############################## The Hints ##############################


        ############################## The Buttons ##############################
        btn_A = tk.Button(self.bottom, bg = "light blue", activebackground = "light blue", bd = 1, cursor = "hand2", font = "Arial 22") ##
        btn_A.place(relx = 0.325, rely = 0.6, relwidth = 0.15, relheight = 0.09)
            
        btn_B = tk.Button(self.bottom, bg = "light blue", activebackground = "light blue", bd = 1, cursor = "hand2", font = "Arial 22")##
        btn_B.place(relx = 0.525, rely = 0.6, relwidth = 0.15, relheight = 0.09)
            
        btn_C = tk.Button(self.bottom, bg = "light blue", activebackground = "light blue", bd = 1, cursor = "hand2", font = "Arial 22")##
        btn_C.place(relx = 0.325, rely = 0.75, relwidth = 0.15, relheight = 0.09)
            
        btn_D = tk.Button(self.bottom, bg = "light blue", activebackground = "light blue", bd = 1, cursor = "hand2", font = "Arial 22")##
        btn_D.place(relx = 0.525, rely = 0.75, relwidth = 0.15, relheight = 0.09)
        ############################## The Buttons ##############################

        self.statesAnsweredCorrectly = list()
        self.statesAnsweredIncorrectly = list()

        Gameplay.QnA(self, master, btn_A, btn_B, btn_C, btn_D, bottomLbl)
        Gameplay.results(self, master, screenWidth, screenHeight)
        

    ####################################################
    # This function contains the logic of the gameplay #
    ####################################################
    def QnA(self, master, btn_A, btn_B, btn_C, btn_D, bottomLbl):
        statesToAsk = list(statesAndCapitals.keys())
        statesAsked = list()
        wrongAnswers = list()   # holds the 3 incorrect options
        wrongBtns = list()  # holds the 3 incorrect buttons
            
        for turn in range(1, 51):
            state = ""
            A = B = C = D = ""

            state, statesToAsk, statesAsked = Gameplay.getState(state, statesToAsk, statesAsked)
            correctLetter = random.choice("ABCD") # Decides which multiple choice option will hold the correct answer

            wrongAnswers.clear()
            wrongBtns.clear()
            A, B, C, D, wrongAnswers = Gameplay.assignAnswersToOptions(A, B, C, D, correctLetter, state, wrongAnswers)
            

            stateFlagImg = tk.PhotoImage(file = usFlagsNSeals[state][0])
            self.stateFlagLbl.configure(image = stateFlagImg)

            bottomLbl.configure(text = state + "?")#, font = "Arial 25")
            bottomLbl.place(relx = 0.005, rely = 0.665, relwidth = 0.99, relheight = 0.33)

            stateSealImg = tk.PhotoImage(file = usFlagsNSeals[state][1])
            self.stateSealLbl.configure(image = stateSealImg)

            answer = statesAndCapitals[state]


            btn_A.configure(text = A, bg = "light blue", state = "normal")
            btn_B.configure(text = B, bg = "light blue", state = "normal")
            btn_C.configure(text = C, bg = "light blue", state = "normal")
            btn_D.configure(text = D, bg = "light blue", state = "normal")


            if answer != A:
                wrongBtns.append(btn_A)
            if answer != B:
                wrongBtns.append(btn_B)
            if answer != C:
                wrongBtns.append(btn_C)
            if answer != D:
                wrongBtns.append(btn_D)


            if (turn == 1): # configures the hint buttons
                self.coinFlipBtn.configure(command = lambda: [self.hintSelected.set("coinFlipB"), self.coinFlipBtn.configure(state = "disable"), Gameplay.hintManagement(self, self.coinFlipBtn, self.hintSelected, answer, wrongAnswers, wrongBtns)])
                self.eliminate1Btn.configure(command = lambda: [self.hintSelected.set("eliminate1B"), self.eliminate1Btn.configure(state = "disable"), Gameplay.hintManagement(self, self.eliminate1Btn, self.hintSelected, answer, wrongAnswers, wrongBtns)])
                self.letterBtn.configure(command = lambda: [self.hintSelected.set("letterB"), self.letterBtn.configure(state = "disable"), Gameplay.hintManagement(self, self.letterBtn, self.hintSelected, answer, wrongAnswers, wrongBtns)])

                
            userGuess = tk.StringVar()
            
            btn_A.configure(command = lambda: userGuess.set(A), overrelief = "sunken")
            btn_B.configure(command = lambda: userGuess.set(B), overrelief = "sunken")
            btn_C.configure(command = lambda: userGuess.set(C), overrelief = "sunken")
            btn_D.configure(command = lambda: userGuess.set(D), overrelief = "sunken")

            btn_A.wait_variable(userGuess)
            # I only wait for button_A because that means that it'll only accept the users' first guesses. If I had waited for all 4 buttons,
            # then the user would have had to press the buttons 4 times before either being given another question, or the game ending. Also,
            # it doesn't matter that I waited for button_A; waiting for any other button would work

            if userGuess.get() == answer:
                winsound.PlaySound("correctSound.wav", winsound.SND_ASYNC)
                
                self.correct += 1
                self.correctLbl = tk.Label(self.playFr, text = "Correct: " + str(self.correct), bg = "light green", font = "Arial 15", bd = 0)
                self.correctLbl.place(relwidth = 0.2, relheight = 0.05)

                self.accuracy = round((self.correct/turn) * 100, 2)
                self.accuracyLbl = tk.Label(self.playFr, text = "Accuracy: " + str(self.accuracy) + "%", bg = "yellow", font = "Arial 15", bd = 0)
                self.accuracyLbl.place(relx = 0.4, relwidth = 0.2, relheight = 0.05)

                self.statesAnsweredCorrectly.append(state)                    

            else:
                winsound.PlaySound("incorrectSound.wav", winsound.SND_ASYNC)
                
                self.incorrect += 1
                self.incorrectLbl = tk.Label(self.playFr, text = "Incorrect: " + str(self.incorrect), bg = "red", font = "Arial 15", bd = 0)
                self.incorrectLbl.place(relx = 0.2, relwidth = 0.2, relheight = 0.05)

                self.accuracy = round((self.correct/turn) * 100, 2)
                self.accuracyLbl = tk.Label(self.playFr, text = "Accuracy: " + str(self.accuracy) + "%", bg = "yellow", font = "Arial 15", bd = 0)
                self.accuracyLbl.place(relx = 0.4, relwidth = 0.2, relheight = 0.05)

                self.lastMissed = state
                self.lastMissedLbl = tk.Label(self.playFr, text = "Last Missed: " + self.lastMissed, bg = "pink", font = "Arial 15", bd = 0)
                self.lastMissedLbl.place(relx = 0.6, relwidth = 0.2, relheight = 0.05)

                self.statesAnsweredIncorrectly.append(state)

                ############################## A window that lets the user know they answered a question incorrectly ##############################
                self.wrongAnsFr = tk.Frame(self.bottom, bg = "black", bd = 1)
                self.wrongAnsFr.place(relx = 0.3, rely = 0.6, relwidth = 0.4, relheight = 0.295)

                titleLbl = tk.Label(self.wrongAnsFr, bg = "red", text = "Incorrect Answer", font = "Arial 25")
                titleLbl.place(relwidth = 1.0, relheight = 0.25)

                wrongAnsLbl = tk.Label(self.wrongAnsFr, bg = "white", text = "Your Answer: " + userGuess.get(), fg = "red", font = "Arial 20")
                wrongAnsLbl.place(rely = 0.25, relwidth = 1.0, relheight = 0.25)

                rightAnsLbl = tk.Label(self.wrongAnsFr, bg = "white", text = "Correct Answer: " + answer, fg = "green", font = "Arial 20")
                rightAnsLbl.place(rely = 0.5, relwidth = 1.0, relheight = 0.25)


                tmpVar = tk.IntVar()

                continueLbl = tk.Label(self.wrongAnsFr, bg = "white")
                continueLbl.place(rely = 0.75, relwidth = 1.0, relheight = 0.25)

                continueBtn = tk.Button(continueLbl, bg = "white", activebackground = "white", text = "Continue", font = "Arial 22", cursor = "hand2", bd = 0, command = lambda: [self.wrongAnsFr.destroy(), tmpVar.set(1)])
                continueBtn.place(relx = 0.35, relwidth = 0.3, relheight = 1.0)
                
                continueBtn.wait_variable(tmpVar)
                ############################## A window that lets the user know they answered a question incorrectly ##############################
    


    ######################################
    # This function deals with the hints #
    ######################################
    def hintManagement(self, button, hintSelected, answer, wrongAnswers, wrongBtns):
        # "answer" & "wrongAnswers" are used when hintSelected.get() == "coinFlipB"
        # "wrongBtns" is used when hintSelected.get() == "eliminate1B"
        # "answer" is used when hintSelected.get() == "letterB"

        if hintSelected.get() == "coinFlipB":            
            x = random.randint(0, 1)    # 0 = Wrong Answer given; 1 = Correct Answer given

            hintFr = tk.Frame(self.bottom, bg = "black", bd = 1)
            hintFr.place(relx = 0.3, rely = 0.6, relwidth = 0.4, relheight = 0.295)

            titleLbl = tk.Label(hintFr, bg = "orange", text = "COIN FLIP", font = "Arial 25")
            titleLbl.place(relwidth = 1.0, relheight = 0.25)

            if x == 1:
                coinFlipLbl = tk.Label(hintFr, bg = "white", text = "The coin has chosen... " + answer + ".\nWill you trust it?", fg = "red", font = "Arial 20")
            else:
                wrongCity = random.sample(wrongAnswers, 1)[0]                
                coinFlipLbl = tk.Label(hintFr, bg = "white", text = "The coin has chosen... " + wrongCity + ".\nWill you trust it?", fg = "red", font = "Arial 20")
                
            coinFlipLbl.place(rely = 0.25, relwidth = 1.0, relheight = 0.5)

            btnLbl = tk.Label(hintFr, bg = "white")
            btnLbl.place(rely = 0.75, relwidth = 1.0, relheight = 0.25)

            closeBtn = tk.Button(btnLbl, text = "Close", font = "Arial 22", bg = "white", activebackground = "white", bd = 0, cursor = "hand2", command = hintFr.destroy)
            closeBtn.place(relx = 0.35, relwidth = 0.3, relheight = 1.0)

        elif hintSelected.get() == "eliminate1B":
            wrongButton = random.sample(wrongBtns, 1)[0]
            wrongButton.configure(bg = "red3", state = "disabled")
            
        elif hintSelected.get() == "letterB":
            letter = random.choice(answer[:]).lower()

            while letter == " " or letter == ".":
                letter = random.choice(answer[:]).lower()

            hintFr = tk.Frame(self.bottom, bg = "black", bd = 1)
            hintFr.place(relx = 0.3, rely = 0.6, relwidth = 0.4, relheight = 0.295)

            titleLbl = tk.Label(hintFr, bg = "orange", text = "LETTER", font = "Arial 25") 
            titleLbl.place(relwidth = 1.0, relheight = 0.25)

            textLbl = tk.Label(hintFr, bg = "white", text = letter, fg = "red", font = "Arial 20")
            textLbl.place(rely = 0.25, relwidth = 1.0, relheight = 0.5)

            btnLbl = tk.Label(hintFr, bg = "white")
            btnLbl.place(rely = 0.75, relwidth = 1.0, relheight = 0.25)

            closeBtn = tk.Button(btnLbl, text = "Close", font = "Arial 22", bg = "white", activebackground = "white", bd = 0, cursor = "hand2", command = hintFr.destroy)
            closeBtn.place(relx = 0.35, relwidth = 0.3, relheight = 1.0)            


    #########################################################################
    # This function finds the next state whose capital is going to be asked #
    #########################################################################
    def getState(state, statesToAsk, statesAsked):
        state = random.sample(statesToAsk, 1)  # Chooses a state
        state = state[0]    # I'm taking the 0th element of state because "random.sample(population, k)" returns a LIST of k items

        statesToAsk.remove(state)
        statesAsked.append(state)

        return state, statesToAsk, statesAsked



    ###############################################################
    # This function assigns answers to the options A, B, C, and D #
    ###############################################################
    def assignAnswersToOptions(A, B, C, D, correctLetter, state, wrongAnswers):        
        if correctLetter == "A":
            A = statesAndCapitals[state]
        elif correctLetter == "B":
            B = statesAndCapitals[state]
        elif correctLetter == "C":
            C = statesAndCapitals[state]
        elif correctLetter == "D":
            D = statesAndCapitals[state]

        cities = list(statesAndCapitals.values())
        cities.remove(statesAndCapitals[state])

        if A == "":
            A = random.sample(cities, 1)
            A = A[0]
            cities.remove(A)
            wrongAnswers.append(A)
        if B == "":
            B = random.sample(cities, 1)
            B = B[0]
            cities.remove(B)
            wrongAnswers.append(B)
        if C == "":
            C = random.sample(cities, 1)
            C = C[0]
            cities.remove(C)
            wrongAnswers.append(C)
        if D == "":
            D = random.sample(cities, 1)
            D = D[0]
            cities.remove(D)
            wrongAnswers.append(D)

        return A, B, C, D, wrongAnswers



    ################################################
    # This function prints the results of the game #
    ################################################
    def results(self, master, screenWidth, screenHeight):      
        resultsPg = tk.Frame(self.playFr, bg = "white")
        resultsPg.place(relwidth = 1.0, relheight = 1.0)

        topLbl = tk.Label(resultsPg, bg = "black")
        topLbl.place(relwidth = 1.0, relheight = 0.05)

        returnBtn = tk.Button(topLbl, text = "Return to Main Menu", bg = "black", activebackground = "black", fg = "white", font = "Arial 18", cursor = "hand2", bd = 0, command = lambda: self.playFr.destroy())
        returnBtn.place(relwidth = 0.2, relheight = 1.0)


        #########################################################################
        msgBox1 = tk.Text(resultsPg, bg = "light green")
        msgBox1.insert("insert", "States Answered Correctly" + "\n")
        msgBox1.tag_add("title", "1.0", "1.end")
        msgBox1.tag_config("title", font = "Tahoma 25")
        msgBox1.insert("insert", "(Scroll down if needed)" + "\n\n")
        msgBox1.tag_add("subscript", "2.0", "2.end")
        msgBox1.tag_config("subscript", font = "Arial 15")

        if len(self.statesAnsweredCorrectly) > 0:            
            for state in self.statesAnsweredCorrectly:
                msgBox1.insert("end", state + "\n")
                msgBox1.tag_add("state", "3.0", "99.end")
                msgBox1.tag_config("state", font = "Courier 15")
        else:
            msgBox1.insert("insert", "N/A")
            msgBox1.tag_add("state", "3.0", "99.end")
            msgBox1.tag_config("state", font = "Courier 15")
        
        msgBox1.configure(state = "disabled", bd = 0) 
        msgBox1.tag_add("Entire box", "1.0", "99.end") 
        msgBox1.tag_config("Entire box", justify = "center")
        msgBox1.place(relx = 0.05, rely = 0.05, relwidth = 0.3, relheight = 0.95)
        #########################################################################

        correctMsg = "\n\n\n\n\nStates answered correctly: " + str(self.correct) 
        incorrectMsg = "\nStates answered incorrectly: " + str(self.incorrect)
        accuracyMsg = "\nAccuracy: " + str(self.accuracy) + "%"

        msgBox2 = tk.Text(resultsPg, bg = "white", font = "Arial 22", bd = 0)
        msgBox2.insert("insert", correctMsg)
        msgBox2.insert("insert", incorrectMsg)
        msgBox2.insert("insert", accuracyMsg)
        msgBox2.configure(state = "disabled")
        msgBox2.tag_add("All the text in the box", 0.0, 10.0) 
        msgBox2.tag_config("All the text in the box", justify = "center", offset = 20)# Centers the text
        msgBox2.place(relx = 0.35, rely = 0.05, relwidth = 0.3, relheight = 0.95)
        
        #########################################################################
        msgBox3 = tk.Text(resultsPg, bg = "red")
        msgBox3.insert("insert", "States Answered Incorrectly" + "\n")
        msgBox3.tag_add("title", "1.0", "1.end")
        msgBox3.tag_config("title", font = "Tahoma 25")
        msgBox3.insert("insert", "(Scroll down if needed)" + "\n\n")
        msgBox3.tag_add("subscript", "2.0", "2.end")
        msgBox3.tag_config("subscript", font = "Arial 15")

        if len(self.statesAnsweredIncorrectly) > 0:            
            for state in self.statesAnsweredIncorrectly:
                msgBox3.insert("end", state + "\n")
                msgBox3.tag_add("state", "3.0", "99.end")
                msgBox3.tag_config("state", font = "Courier 15")
        else:
            msgBox3.insert("insert", "N/A")
            msgBox3.tag_add("state", "3.0", "99.end")
            msgBox3.tag_config("state", font = "Courier 15")

        msgBox3.configure(state = "disabled", bd = 0)
        msgBox3.tag_add("Entire box", "1.0", "99.end") 
        msgBox3.tag_config("Entire box", justify = "center")
        msgBox3.place(relx = 0.65, rely = 0.05, relwidth = 0.3, relheight = 0.95)
        #########################################################################

        usaCOA = tk.PhotoImage(file = "usaCoatOfArms.png")
        imageLabel = tk.Label(resultsPg, image = usaCOA, bg = "white")
        imageLabel.photo = usaCOA
        imageLabel.place(relx = ((screenWidth/2) - (usaCOA.width()/2)) / screenWidth, rely = 0.08)
        


    ######################################################################
    # This function closes the play frame in order to quit the play mode #
    ######################################################################
    def quitGame(self):
        quitFr = tk.Frame(self.bottom, bg = "black", bd = 1)
        quitFr.place(relx = 0.3, rely = 0.6, relwidth = 0.4, relheight = 0.295)

        titleLbl = tk.Label(quitFr, bg = "red", text = "QUIT", font = "Arial 25")
        titleLbl.place(relwidth = 1.0, relheight = 0.25)

        questionLbl = tk.Label(quitFr, bg = "white", text = "Are you sure you want to quit?", font = "Arial 20")
        questionLbl.place(rely = 0.25, relwidth = 1.0, relheight = 0.5)

        yesOrNoLbl = tk.Label(quitFr, bg = "white")
        yesOrNoLbl.place(rely = 0.75, relwidth = 1.0, relheight = 0.25)

        yesBtn = tk.Button(yesOrNoLbl, bg = "white", activebackground = "white", fg = "red", text = "Yes", font = "Arial 22", cursor = "hand2", bd = 0, command = lambda: self.playFr.destroy())
        yesBtn.place(relx = 0.1, relwidth = 0.3, relheight = 1.0)

        noBtn = tk.Button(yesOrNoLbl, bg = "white", activebackground = "white", fg = "green", text = "No", font = "Arial 22", cursor = "hand2", bd = 0, command = lambda: quitFr.destroy())
        noBtn.place(relx = 0.6, relwidth = 0.3, relheight = 1.0)
        

 
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Atlas (USA Edition)")
    app = MainMenu(root)
    
    root.mainloop()
