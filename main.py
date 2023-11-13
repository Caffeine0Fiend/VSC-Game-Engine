#
# ██╗░░░██╗░██████╗░█████╗░  ░██████╗░░█████╗░███╗░░░███╗███████╗  ███████╗███╗░░██╗░██████╗░██╗███╗░░██╗███████╗
# ██║░░░██║██╔════╝██╔══██╗  ██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔════╝████╗░██║██╔════╝░██║████╗░██║██╔════╝
# ╚██╗░██╔╝╚█████╗░██║░░╚═╝  ██║░░██╗░███████║██╔████╔██║█████╗░░  █████╗░░██╔██╗██║██║░░██╗░██║██╔██╗██║█████╗░░
# ░╚████╔╝░░╚═══██╗██║░░██╗  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░╚██╗██║██║╚████║██╔══╝░░
# ░░╚██╔╝░░██████╔╝╚█████╔╝  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ███████╗██║░╚███║╚██████╔╝██║██║░╚███║███████╗
# ░░░╚═╝░░░╚═════╝░░╚════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝░╚═════╝░╚═╝╚═╝░░╚══╝╚══════╝
#

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
# converttaa pelistä, peli plätformiksi : Valmis
# lisätä lisää vaihtoehtoja : Valmis
# lisää pelejä : Valmis
# -------------------------------------------------------------

# Trello > https://trello.com/b/IzZj8Om5/peli-trello
# Github > https://github.com/Caffeine0Fiend/VSC-Game-Engine

# ----------------------------------------------------------------

# imports
import random
import time

# player data
Points = {}
Usernames = {}
Adventure_Grid = {} # grid positions
GridTypeData = {} # storing data for grid positions
selections = {
        1: "Rock",
        2: "Paper",
        3: "Scissors",
    }
Grid_Types = {
    1: "Forest",
    2: "Brick Buidling",
    3: "Cave",
    4: "Open Field",
    5: "Town",
    5: "Trail",
    6: "River",
}
Grid_Items = {
    1: "Water Bottle",
    2: "Food",
    3: "Orc",
    4: "Wolf",
    5: "Weapon",
    5: "Poison",
    6: "Shelter",
}
GridValues = {
    "Water Bottle" : ["Take", "Drink", "Ignore"],
    "Food" : ["Take", "Eat", "Ignore"],
    "Orc" : ["Attack", "Retreat", "Run", "Ignore"],
    "Wolf" : ["Attack", "Retreat", "Run", "Ignore"],
    "Weapon" : ["Take","Ignore"],
    "Poison" : ["Take", "Consume", "Ignore"],
    "Shelter" : ["Await Daytime", "Ignore"],
}
Reoccuring = {
    "Forest":True,
    "Open Field":True,
    "River":True,
}

class player:
    health: 100
    maxhealth: 100
    hunger: 0
    thirst: 0
    temperature: random.randint(35,37)
    position: 0
    itemsstored: 0
    inventory: {}

    def __init__(self, position = 0, thirst = 0, hunger = 0, temperature = random.randint(35,37), inventory = {}, health = 100, maxhealth = 100, itemsstored = 0) -> None:
        self.position = position
        self.thirst = thirst
        self.hunger = hunger
        self.temperature = temperature
        self.inventory = inventory
        self.health = health
        self.maxhealth = maxhealth
        self.itemsstored = itemsstored
        pass

    def __str__(self) -> str:
        print("█▀█ █░░ ▄▀█ █▄█ █▀▀ █▀█   █▀ ▀█▀ ▄▀█ ▀█▀ █▀")
        print("█▀▀ █▄▄ █▀█ ░█░ ██▄ █▀▄   ▄█ ░█░ █▀█ ░█░ ▄█")
        print("")
        print(f"Health : {self.health}/{self.maxhealth}")
        print(f"Hunger : {self.hunger}/{100}")
        print(f"Thirst : {self.thirst}/{100}")
        print(f"Temperature : {self.temperature}°C")
        print("")
        print("Your Inventory Contains:")
        print("-")
        for I in self.inventory:
            print(self.inventory.get(I), I)
        return "-"

# functions
def RollDice(): # nopan heitto
    throw = random.randint(1,100) # 10% mahdollisuus hävitä
    if throw <= 10:
        return 1
    else:
        return random.randint(2,6)
    
def PrintSpace(num: int):
    for i in range(1,num):
        print("")

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
        PrintSpace(5)
        print(f" Game ended with the Stats being")
        print(f"Winner : " + gamedata["Winner"])
        print("Points :")
        for Player in gamedata["Players"]:
            print(f"{Usernames.get(Player)} scored a total of {Points.get(Player)} points")

        print(f"Returning to main menu in 3 seconds")
        time.sleep(3)
        return "Completed Game"
    pass

def R_P_S_AI(gamedata :dict):

    def SelectRandom():
        return selections[random.randint(1,3)]

    print("---")

    Bestof = int(input("This game will be played as Best of (3-5) : "))
    Bestof = int(Bestof)
    if Bestof > 5:
        Bestof = 5
    elif Bestof < 3:
        Bestof = 3
    RequiredForWin = (Bestof/2)
    RequiredForWin = int(RequiredForWin)
    if Bestof >= 4:
        RequiredForWin += 1
    elif Bestof == 3:
        RequiredForWin = 2

    print(f"This game will be ran in the Best of {Bestof} format")
    print(f"To win youll have to score {RequiredForWin} points")
    print("---")

    Ai_Points = 0
    Player_Points = 0

    while Ai_Points < RequiredForWin and Player_Points < RequiredForWin:
        
        for itm in selections:
            print(itm,":",selections.get(itm))
        
        inp = int(input(f"Pick a choice (1-3) : "))

        if selections.get(inp) != None:
            Selected = selections.get(inp)
            AI_Selected = SelectRandom()

            if Selected == "Rock" and AI_Selected == "Scissors":
                Player_Points = Player_Points + 1
                print("---")
                print(f"Player Wins with {Selected}")
                print("")
                print(f"Player Points : {Player_Points}")
                print(f"AI Points : {Ai_Points}")
                print("---")
            elif Selected == "Paper" and AI_Selected == "Rock":
                Player_Points = Player_Points + 1
                print("---")
                print(f"Player Wins with {Selected}")
                print("")
                print(f"Player Points : {Player_Points}")
                print(f"AI Points : {Ai_Points}")
                print("---")
            elif Selected == "Scissors" and AI_Selected == "Paper":
                Player_Points = Player_Points + 1
                print("---")
                print(f"Player Wins with {Selected}")
                print("")
                print(f"Player Points : {Player_Points}")
                print(f"AI Points : {Ai_Points}")
                print("---")
            elif Selected == AI_Selected:
                print("---")
                print("Tie")
                print("")
                print(f"Player Points : {Player_Points}")
                print(f"AI Points : {Ai_Points}")
                print("---") 
            else:
                Ai_Points = Ai_Points + 1
                print("---")
                print(f"AI Wins with {AI_Selected}")
                print("")
                print(f"Player Points : {Player_Points}")
                print(f"AI Points : {Ai_Points}")
                print("---")


        else:
            print("---")
            print("Invalid Input")
            print("---")

    PrintSpace(5)        
    if Ai_Points >= RequiredForWin:
        print("")
        print("---")
        print("░█████╗░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗░██████╗")
        print("██╔══██╗██║  ░██║░░██╗░░██║██║████╗░██║██╔════╝")
        print("███████║██║  ░╚██╗████╗██╔╝██║██╔██╗██║╚█████╗░")
        print("██╔══██║██║  ░░████╔═████║░██║██║╚████║░╚═══██╗")
        print("██║░░██║██║  ░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝")
        print("╚═╝░░╚═╝╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░")
        print("---")
    else:
        print("")
        print("---")
        print("██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░  ░██╗░░░░░░░██╗██╗███╗░░██╗░██████╗")
        print("██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗  ░██║░░██╗░░██║██║████╗░██║██╔════╝")
        print("██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝  ░╚██╗████╗██╔╝██║██╔██╗██║╚█████╗░")
        print("██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗  ░░████╔═████║░██║██║╚████║░╚═══██╗")
        print("██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║  ░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝")
        print("╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░")
        print("---")
    
    print(f"Returning to main menu in 3 seconds")
    time.sleep(3)
    return "Completed Game"

worlddata = {
    "day": 0
}
game_finished = False
def Multi_user_dungeon(gamedata :dict):

    GamePlayer = player()

    def printcustom(typetext):

        if typetext == "died":
            PrintSpace(255)
            print("██╗░░░██╗░█████╗░██╗░░░██╗  ██████╗░██╗███████╗██████╗░")
            print("╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔══██╗██║██╔════╝██╔══██╗")
            print("░╚████╔╝░██║░░██║██║░░░██║  ██║░░██║██║█████╗░░██║░░██║")
            print("░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░██║██║██╔══╝░░██║░░██║")
            print("░░░██║░░░╚█████╔╝╚██████╔╝  ██████╔╝██║███████╗██████╔╝")
            print("░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═════╝░╚═╝╚══════╝╚═════╝░")

    GridTypes = {
        1: [100, "50x50"],
        2: [200, "100x100"],
        3: [500, "250x250"],
        4: [1000, "500x500"],
    }

    finish_type = None

    def HealthCheck():
        if GamePlayer.health <= 0:
            game_finished = True
            finish_type = "Death"
            printcustom("died")
            PrintSpace(2)
            print(GamePlayer)
            PrintSpace(8)
            return "ded"
        return "alive"
        
    checkup = HealthCheck()

    if checkup == "ded":
        return "Completed Game"
    
    for Item in GridTypes:
        print(Item, GridTypes.get(Item)[1])
    type = int(input("Select a World Size (1-4) : "))
    GridValue = GridTypes.get(type)
    print(GridValue[1],"Selected")
    
    #printtype = input("Input Print Type (Raw/Clean) : ")
    GridCount = 0
    PieceBefore = "Forest"
    for I in range(0,GridTypes.get(type)[0]):
        GridCount += 1
        GridPiece = Grid_Types.get(random.randint(1,6))
        if Reoccuring.get(PieceBefore) != None and Reoccuring[PieceBefore] == True:
            if random.randint(0,100) <= 30:
                GridPiece = PieceBefore
        Items = {}
        TypeCount = 0
        for I in range(0,random.randint(2,6)):

            if random.randint(0,100) <= 25:
                TypeCount += 1
                item = Grid_Items.get(random.randint(1,6))
                Items.__setitem__(TypeCount,item)
        Adventure_Grid.__setitem__(GridCount, GridPiece)
        GridTypeData.__setitem__(GridCount,Items)
        PieceBefore = GridPiece
       # if printtype == "Test_Clean":
           # print(GridCount,Items)
    #print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    #if printtype == "Test":
     #   print(GridTypeData)
   # print(Adventure_Grid)
    #print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    GamePlayer.position = (GridCount/2) + random.randint(-GridCount/4,GridCount/4)
    print("Welcome to the vast lands! Would you like any instructions?")
    PrintSpace(2)
    answer = input("")

    def printposition():
        if Adventure_Grid.get((GamePlayer.position-1)) == Adventure_Grid.get((GamePlayer.position+1)):
            print(f"You are inmiddle of two {Adventure_Grid.get((GamePlayer.position-1))}s, with {GamePlayer.itemsstored} items in your possession.")
        else:  
            print(f"You are near a {Adventure_Grid.get((GamePlayer.position-1))}, with {GamePlayer.itemsstored} items in your possession, theres still a {Adventure_Grid.get((GamePlayer.position+1))} nearby")
        PrintSpace(2)
    
    def GameLoop(start):

        print(f"Your currently in {Adventure_Grid.get(GamePlayer.position)}")

        state = HealthCheck()

        if state == "ded":
            return "death"
        
        GamePlayer.itemsstored = 0
        for I in GamePlayer.inventory:
            GamePlayer.itemsstored + GamePlayer.inventory.get(I)

        if start != True:
            printposition()

        def Act(action):
            if action == 1:
                print(GamePlayer)
                return GameLoop(False)
            elif action == 2:
                GamePlayer.position += 1
                return GameLoop(False)
            elif action == 3:
                GamePlayer.position -= 1
                return GameLoop(False)
        
        PrintSpace(3)

        num = 1
        interacting = True
        lastprint = ""
        while interacting and game_finished != True:
            
            recount = 1
            grid_data :dict = GridTypeData.get(GamePlayer.position)
            if grid_data == None:
                break
            item = grid_data.get(recount)
            itemdata = GridValues.get(item)

            ConcurrentData = {}
            ConcurrentData.__setitem__("item",item)
            ValidActions = {}

            if itemdata != None:
                
                print(f"You find {grid_data.get(recount)}")

                listcount = 0
                listmax = len(itemdata)
                for i in range(0,listmax):
                    print(f": {itemdata[listcount]}") #{listcount}
                    ValidActions.__setitem__(itemdata[listcount], True)
                    listcount += 1

                num += 1
                recount += 1
                PrintSpace(3)
                if grid_data != {} and ConcurrentData.get("item") != None:
                   
                    def Ask():
                        def Action(acti):

                            if acti == "Take":
                                if GamePlayer.inventory.get(ConcurrentData.get("item")) != None:
                                    GamePlayer.inventory.__setitem__(ConcurrentData.get("item"), GamePlayer.inventory.get(ConcurrentData.get("item")) + 1)
                                else:
                                    GamePlayer.inventory.__setitem__(ConcurrentData.get("item"), 1)

                                GridTypeData.pop(GamePlayer.position)
                                #GridTypeData.get(GamePlayer.position).__setitem__(recount, None)

                                print("You pick it up and store it.")
                                time.sleep(1)
                                return "Breakloop"
                            elif acti == "Attack":
                                inventory = GamePlayer.inventory

                                if inventory.get("Weapon") != None:
                                    inventory.__setitem__("Weapon",inventory.get("Weapon") - 1)
                                    print("1 Weapon Used")
                                    GridTypeData.pop(GamePlayer.position)
                                else:
                                    print("You fight barehanded")
                                    time.sleep(3)
                                    
                                    victory = random.randint(0,100) <= 2

                                    if victory:
                                        GridTypeData.pop(GamePlayer.position)
                                        return "Breakloop"
                                    else:
                                        GamePlayer.health = 0
                                        return "Died"
                            elif acti == "Ignore":
                                
                                return "Breakloop"
                            elif acti == "Drink":
                                print("You drink water..")
                                print("- 12 thirst")
                                if GamePlayer.thirst >= 12:
                                    GamePlayer.thirst -= 12
                                else:
                                    GamePlayer.thirst = 0
                                GridTypeData.pop(GamePlayer.position)
                                return "Breakloop"
                            elif acti == "Eat":
                                print("You eat food..")
                                print("- 6 hunger")
                                if GamePlayer.hunger >= 6:
                                    GamePlayer.hunger -= 6
                                else:
                                    GamePlayer.hunger = 0
                                GridTypeData.pop(GamePlayer.position)
                                return "Breakloop"
                            elif acti == "Consume":
                                GridTypeData.pop(GamePlayer.position)
                                print("You consume poison..")
                                print("- 6 health")
                                if GamePlayer.health >= 6:
                                    GamePlayer.health -= 6
                                else:
                                    GamePlayer.health = 0
                                    return "Died"
                                #HealthCheck()
                                return "Breakloop"
                            elif acti == "Retreat":
                                GridTypeData.pop(GamePlayer.position)
                                print("You retreated slowly..")
                                print("nothing noticed you move..")
                                GamePlayer.position -= 2
                                printposition()
                                time.sleep(1)
                                return "Breakloop"
                            elif acti == "Run":
                                GridTypeData.pop(GamePlayer.position)
                                print("You Ran Fast..")

                                if item == "Orc" or item == "Wolf":
                                    if random.randint(0,100) <= 25:
                                        print("A hostile saw you ran and caught you")
                                        time.sleep(1)
                                        print("You fight back..")
                                        time.sleep(2)
                                        if random.randint(0,100) <= 30:
                                            GamePlayer.health = 0
                                            return "Died"
                                    else:
                                        print("nothing noticed you move..")
                                        GamePlayer.position -= 2
                                        printposition()
                                else:
                                        print("nothing noticed you move..")
                                        GamePlayer.position -= 2
                                        printposition()
                                
                                time.sleep(1)
                                GridTypeData.get(GamePlayer.position).__setitem__(recount, None)
                                return "Breakloop"
                            elif acti == "Await Daytime":
                                print("You await daytime..")
                                time.sleep(3)
                                print("You feel refreshed..")
                                print("+ 3 health")
                                worlddata["day"] += 1
                                if GamePlayer.health - GamePlayer.maxhealth >= 3:
                                    GamePlayer.health += 3
                                else:
                                    GamePlayer.health = GamePlayer.maxhealth
                                time.sleep(1)
                                return "Breakloop"


                        act = input("")
                        if ValidActions.get(act) != None and ValidActions.get(act) == True:
                            returned = Action(act)
                            if returned == "Breakloop":
                                #GridTypeData.get(GamePlayer.position).__setitem__(recount, None)
                                return "Breakloop"
                            elif returned == "Died":
                                #GridTypeData.get(GamePlayer.position).__setitem__(recount, None)
                                return "Died"
                        else:
                            print("InvalidAction")
                            returned = Ask()
                            if returned == "Breakloop":
                                return "Breakloop"
                            elif returned == "Died":
                                return "Died"

                    returned = Ask()
                    if returned == "Breakloop":
                        break
                    elif returned == "Died":
                        HealthCheck()
                        break
                else:
                    break
            else:
                interacting = False
                break

        if game_finished != True or GamePlayer.health == 0:

            if HealthCheck() == "alive":

                print(f"{1} : View Player")
                print(f"{2} : Head Forwards")
                print(f"{3} : Head Backwards")

                PrintSpace(3)
                action = input("")

                if action == "RawPrint":
                    print(GridTypeData)
                    print(Adventure_Grid)
                    print(GamePlayer.position)
                    return GameLoop(False)
                action = int(action)
                Act(action)

        if game_finished != True or GamePlayer.health == 0:
            returned = GameLoop(False)
            if returned == "Completed Game":
                return "Completed Game"
        else:
            return "Completed Game"

    if answer != None :
        if answer == "Yes":
            print("For this multi user dungeon you will have to choose options by typing their number, i have also added Thirst, Hunger, Poison and Health. DEATH WILL BE APPARENT WHILE PLAYING")
        beginning = random.randint(1,3)
        if beginning == 1:
            if Adventure_Grid.get((GamePlayer.position-1)) == Adventure_Grid.get((GamePlayer.position+1)):
                print(f"You wake up inmiddle of two {Adventure_Grid.get((GamePlayer.position-1))}s, with nothing in your possession.")
            else:  
                print(f"You wake up near a {Adventure_Grid.get((GamePlayer.position-1))}, with nothing in your possession, you also notice a {Adventure_Grid.get((GamePlayer.position+1))} nearby")
            returned = GameLoop(True)
            if returned == "Completed Game":
                print("Closing game in 3 seconds")
                time.sleep(3)
                return "Completed Game"
        elif beginning == 2:
            GamePlayer.inventory.__setitem__("Food", 1)
            if Adventure_Grid.get((GamePlayer.position-1)) == Adventure_Grid.get((GamePlayer.position+1)):
                print(f"You wake up inmiddle of two {Adventure_Grid.get((GamePlayer.position-1))}s, with nothing in your possession.")
            else: 
                print(f"You find yourself near a {Adventure_Grid.get((GamePlayer.position-1))}, with small rations in your possession, you also notice a {Adventure_Grid.get((GamePlayer.position+1))} nearby")
            returned = GameLoop(True)
            if returned == "Completed Game":
                print("Closing game in 3 seconds")
                time.sleep(3)
                return "Completed Game"
        else:
            GamePlayer.inventory.__setitem__("Food", 4)
            if Adventure_Grid.get((GamePlayer.position-1)) == Adventure_Grid.get((GamePlayer.position+1)):
                print(f"You wake up inmiddle of two {Adventure_Grid.get((GamePlayer.position-1))}s, with nothing in your possession.")
            else:
                print(f"You appear to be near a {Adventure_Grid.get((GamePlayer.position-1))}, with rations for 4 days in your possession, you also notice a {Adventure_Grid.get((GamePlayer.position+1))} nearby")
            returned = GameLoop(True)
            if returned == "Completed Game":
                print("Closing game in 3 seconds")
                time.sleep(3)
                return "Completed Game"


ValidGames = {
    "PDC": "Multi",
    "RPS": "Single",
    "MUD": "Single",

    "Rock Paper Scissors": "Single",
    "Multi User Dungeon": "Single",
    "Pig Dice Game": "Multi",
}

def RunGame(): # pelin aloitus

    PrintSpace(255)
    print("██╗░░░██╗░██████╗░█████╗░  ░██████╗░░█████╗░███╗░░░███╗███████╗  ███████╗███╗░░██╗░██████╗░██╗███╗░░██╗███████╗")
    print("██║░░░██║██╔════╝██╔══██╗  ██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔════╝████╗░██║██╔════╝░██║████╗░██║██╔════╝")
    print("╚██╗░██╔╝╚█████╗░██║░░╚═╝  ██║░░██╗░███████║██╔████╔██║█████╗░░  █████╗░░██╔██╗██║██║░░██╗░██║██╔██╗██║█████╗░░")
    print("░╚████╔╝░░╚═══██╗██║░░██╗  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░╚██╗██║██║╚████║██╔══╝░░")
    print("░░╚██╔╝░░██████╔╝╚█████╔╝  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ███████╗██║░╚███║╚██████╔╝██║██║░╚███║███████╗")
    print("░░░╚═╝░░░╚═════╝░░╚════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝░╚═════╝░╚═╝╚═╝░░╚══╝╚══════╝")
    PrintSpace(2)


    print("▄▀█ █░█ ▄▀█ █ █▄▄ █░░ █▀▀   █▀▀ ▄▀█ █▀▄▀█ █▀▀ █▀")
    print("█▀█ ▀▄▀ █▀█ █ █▄█ █▄▄ ██▄   █▄█ █▀█ █░▀░█ ██▄ ▄█")

    print("")
    
    print("> Pig Dice Game (PDC) < Multiplayer")
    print("> Rock, Paper, Scissors (RPS) < Singleplayer")
    print("> Multi User Dungeon (MUD) < Singleplayer")
    print("")

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

        PrintSpace(3)
        print("████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        print("█░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░███░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█")
        print("█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█")
        print("█░░▄▀░░░░░░▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░░░░░░░████░░▄▀░░░░▄▀▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░█")
        print("█░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░████████████░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░█████████░░▄▀░░████████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████")
        print("█░░▄▀░░░░░░▄▀░░███░░▄▀░░███░░▄▀░░████████████░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░█████████░░▄▀░░░░░░░░░░████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█")
        print("█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░███░░▄▀░░██░░░░░░████░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░██░░░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█")
        print("█░░▄▀░░░░░░░░░░███░░▄▀░░███░░▄▀░░██░░▄▀░░████░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░█████████░░▄▀░░░░░░░░░░████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░░░░░█")
        print("█░░▄▀░░███████████░░▄▀░░███░░▄▀░░██░░▄▀░░████░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░█████████░░▄▀░░████████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████")
        print("█░░▄▀░░█████████░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░████░░▄▀░░░░▄▀▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░░░░░░░░░█")
        print("█░░▄▀░░█████████░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█")
        print("█░░░░░░█████████░░░░░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░███░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█")
        print("████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
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



        Edit = input("Re-Edit Settings? (y/n) : ")
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

    if SelectGame == "Pig Dice Game" or SelectGame == "PDC":
        config() # call config
        ValidGame = True
    elif SelectGame == "Rock Paper Scissors" or SelectGame == "RPS":
        ValidGame = True
    elif ValidGames.get(SelectGame) == "Single" or ValidGames.get(SelectGame) == "Multi":
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

    if GameData["PlayersIngame"] <= 0 and SelectGame != "None" and ValidGame and ValidGames.get(SelectGame) != "Single": # incase you didnt add players
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

        if SelectGame == "Pig Dice Game" or SelectGame == "PDC":
            game = Pig_Game(GameData)
            if game == "Completed Game":
                RunGame()
        elif SelectGame == "Rock Paper Scissors" or SelectGame == "RPS":
            PrintSpace(2)
            print("██████╗░░█████╗░░█████╗░██╗░░██╗░░░  ██████╗░░█████╗░██████╗░███████╗██████╗░░░░")
            print("██╔══██╗██╔══██╗██╔══██╗██║░██╔╝░░░  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗░░░")
            print("██████╔╝██║░░██║██║░░╚═╝█████═╝░░░░  ██████╔╝███████║██████╔╝█████╗░░██████╔╝░░░")
            print("██╔══██╗██║░░██║██║░░██╗██╔═██╗░██╗  ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗██╗")
            print("██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗╚█║  ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║╚█║")
            print("╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝░╚╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝░╚╝")
            print("")
            print("░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗")
            print("██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝")
            print("╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░")
            print("░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗")
            print("██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝")
            print("╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░")
            print("------")
            game = R_P_S_AI(GameData)
            if game == "Completed Game":
                RunGame()
        elif SelectGame == "Multi User Dungeon" or SelectGame == "MUD":
            print("███╗░░░███╗██╗░░░██╗██╗░░░░░████████╗██╗  ██╗░░░██╗░██████╗███████╗██████╗░")
            print("████╗░████║██║░░░██║██║░░░░░╚══██╔══╝██║  ██║░░░██║██╔════╝██╔════╝██╔══██╗")
            print("██╔████╔██║██║░░░██║██║░░░░░░░░██║░░░██║  ██║░░░██║╚█████╗░█████╗░░██████╔╝")
            print("██║╚██╔╝██║██║░░░██║██║░░░░░░░░██║░░░██║  ██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗")
            print("██║░╚═╝░██║╚██████╔╝███████╗░░░██║░░░██║  ╚██████╔╝██████╔╝███████╗██║░░██║")
            print("╚═╝░░░░░╚═╝░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝  ░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝")
            print("")
            print("██████╗░██╗░░░██╗███╗░░██╗░██████╗░███████╗░█████╗░███╗░░██╗")
            print("██╔══██╗██║░░░██║████╗░██║██╔════╝░██╔════╝██╔══██╗████╗░██║")
            print("██║░░██║██║░░░██║██╔██╗██║██║░░██╗░█████╗░░██║░░██║██╔██╗██║")
            print("██║░░██║██║░░░██║██║╚████║██║░░╚██╗██╔══╝░░██║░░██║██║╚████║")
            print("██████╔╝╚██████╔╝██║░╚███║╚██████╔╝███████╗╚█████╔╝██║░╚███║")
            print("------")
            game = Multi_user_dungeon(GameData)
            if game == "Completed Game":
                RunGame()

# begin game
RunGame()