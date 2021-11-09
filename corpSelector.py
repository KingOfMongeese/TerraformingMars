#KingOfMongeese
#Corporation selector for terraforming mars.

import random

#List of corporations. Some are custom ones. 
corplist = ["Thorgate","dev wright","Phoblog","Collins, Rubin & Haytham","UnderSec","AeroSpace Alloys", "Viron","Manutech","Credicor","Helion","AMA","Celestic","Terractor","Interplanetary Cinematics","Ecoline","Mining Guild","Aphrodite","Tharsis Republic","Inventrix","Saturn Systems","Morning Star Inc."]

#picks 2 corps per player removing them from the avaible options
def pickCorp(playerName, corps):
    corp1 = random.choice(corps)
    corps.remove(corp1)
    corp2 = random.choice(corps)
    corps.remove(corp2)
    print(playerName + " : " + corp1 + " or " + corp2)

#creates the player list
def getPlayers():
    players = []
    print()
    print("Press 'enter' when done entering names.")
    print()
    while True:
        player = input("Enter Player Name:")
        if player == "":
            break
        players.append(player)
    return players
    
Players = getPlayers()
print()
print("----------------------------------------------------------------------------")
print()

#loop that picks the corps for all the players.
for player in Players:
    pickCorp(player, corplist)
       
