
# Projecti 1 >
# ---------------------------------------------------------------

# Ideana oli tehdä Pig noppapeli
# annettu aika on perjantaihin mennessä

# haluan minimissään saada seuraavat functiot >
# -------------------------------------------------------------
# Vuoro Function ja toistorakenteen : Valmis
# nopan heitto : Valmis
# pelin aloitus : Valmis
# -------------------------------------------------------------

# jos jää aikaa >
# -------------------------------------------------------------
# voisin hienostella inputit : Valmis
# voisin heinostella printit : Valmis
# lisätä peli teitojen vaihto : Valmis
# converttaa pelistä, peli plätformiksi : Työn Alla
# lisätä lisää vaihtoehtoja : Työn Alla
# lisää pelejä : Työn alla
# -------------------------------------------------------------

# ----------------------------------------------------------------

# imports
import random

# player data
Points = {}
Usernames = {}

# functions
def RollDice(): # nopan heitto
    throw = random.randint(1,100) # 10% mahdollisuus hävitä
    if throw <= 10:
        return 1
    else:
        return random.randint(2,6)

def Pig_Game(gamedata :dict): # peli looppi pelin loppuun asti
    if gamedata["Round"] > 1:
        print("------")
        print("Round Results")
        print("------")
        for Player in gamedata["Players"]:
         print(Usernames.get(Player), "Scored", Points.get(Player), "Points")
        print("------")
        print("Next Round")


    gamedata.__setitem__("Round", gamedata["Round"] + 1)
    for Player in gamedata["Players"]:
        turn_over = False
        print("------")
        print(f"{Usernames.get(Player)}'s turn")
        while not turn_over and gamedata["Game Ended"] != True: # jatkuva tilan katse
            if gamedata["Game Ended"] == True:
                break
            rolldice = input(f"Roll Dice {Usernames.get(Player)}? (y/n) : ")

            PlayerPoints = Points.get(Player)
            if PlayerPoints == None:
                Points.__setitem__(Player, 0)
                PlayerPoints = Points.get(Player)
            
            if rolldice == "y":

                num = RollDice()

                if num >= 2:
                    print(f"{Usernames.get(Player)} Rolled {num}")
                    Points.__setitem__(Player,int(PlayerPoints + num))
                    print(f"{Usernames.get(Player)} Has total points of {Points.get(Player)}")
                    print("------")
                    if Points.get(Player) >= gamedata["WinningPoints"]:
                        print(f"{Usernames.get(Player)} Ended the game with {Points.get(Player)} points")
                        gamedata["Game Ended"] = True
                        gamedata["Winner"] = Player
                        turn_over = True
                elif num == 1:
                    print(f"{Usernames.get(Player)} Rolled {num} ending their turn and resetting their points")
                    Points.__setitem__(Player,0)
                    turn_over = True
            elif rolldice == "n":
                turn_over = True
                print("------")
                print("Next Turn")
            else:
                print("------")
                print(f"invalid input")
    
    if gamedata["Game Ended"] != True:
        Pig_Game(gamedata)
    else:
        print(f" Game ended with the Stats being")
        print(f"Winner : " + gamedata["Winner"])
        print("Points :")
        for Player in gamedata["Players"]:
            print(f"{Usernames.get(Player)} scored a total of {Points.get(Player)} points")
        return "Completed Game"
    pass


def RunGame(): # pelin aloitus

    print("------")
    print("VSC Gradia Game Engine Project")
    print("--")


    print("Avaible Games")

    print("")
    
    print("> Pig Dice Game (PDC)")

    print("------")

    SelectGame = input("Select Game From the list above or input None to quit : ")
    ValidGame = False
    
    print("------")

    GameData = {

            "PlayersIngame": 0,
            "Players": {},
            "Round": 1,

            "WinningPoints": 50,
            "Game Ended": False,
            "Winner": None,
        }
    
    def config(): # Configure game settings

        print("> Pig Dice Game (PDC)")
        print("------")
        print("Game Config")
        print("")
        def editsettings():

            WinningPoints = int(input("Points Required to win? (1-100) : "))

            if WinningPoints > 100:
                WinningPoints = 100
                GameData["WinningPoints"] = WinningPoints
            elif WinningPoints < 1:
                WinningPoints = 1
                GameData["WinningPoints"] = WinningPoints
            else:
                GameData["WinningPoints"] = WinningPoints

            Edit = input("Edit Settings? (y/n) : ")
            if Edit == "y":
                editsettings()
            else:
                return
        

    
        Edit = input("Edit Settings? (y/n) : ")
        if Edit == "y":
            editsettings()

        AllPlayersIn = False
        print("------")
        print("Player Inputting")
        print("")
        while not AllPlayersIn:
            if GameData["PlayersIngame"] != 0:
                print("------")
            
            addnew = input("Add new player? (y/n) : ")

            if addnew == "y":

                def SelectName():

                    newplayer = input("Ingame name: ")

                    for Player in GameData["Players"]:
                        if newplayer == Usernames.get(Player):
                            print("------")
                            print("This name is already in use.")
                            print("------")
                            return SelectName()
                    Playernum = GameData["PlayersIngame"] + 1
                    playeridentifier = "Player" + str(Playernum)

                    GameData.__setitem__("PlayersIngame", (GameData["PlayersIngame"] + 1))

                    GameData["Players"].__setitem__(playeridentifier, True)

                    Points.__setitem__(playeridentifier,0)
                    Usernames.__setitem__(playeridentifier,newplayer)

                SelectName()

            elif addnew == "n":
                AllPlayersIn = True
            else:
                print(f"Invalid Input.")
            
            if AllPlayersIn:
                break
            pass

    if SelectGame == "Pig Dice Game" or SelectGame == "PDC":
        config() # call config
        ValidGame = True
    elif SelectGame == "None":
        return
    else:
        print("------")
        print(f" Invalid Game Name")
        CONF = input("Return to mainmenu? (y/n) : ")
        if CONF == "y":
            RunGame()
        else:
            return

    if GameData["PlayersIngame"] <= 0 and SelectGame != "None" and ValidGame: # incase you didnt add players
        Edit = input("are you sure you want to begin with no players? (y/n) : ")

        if Edit == "y":
            print("------")
            print(f" No players inputted")
            print(f" Game ended with no winner ")
        elif Edit == "n":
            config()
        return
    
    if SelectGame != "None":
        print("------")
    
        print("Starting Game")

        game = Pig_Game(GameData)
        if game == "Completed Game":
            RunGame()


# begin game
RunGame()