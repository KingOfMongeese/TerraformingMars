#KingOfMongeese
#Corporation selector for terraforming mars.

import random
import argparse
import art
import os


parser = argparse.ArgumentParser()

parser.add_argument("-t", "--Turmoil", action="store_true", help="Add Turmoil Corps")
parser.add_argument("-v", "--Venus", action="store_true", help="Add Venus Corps")
parser.add_argument("-cp", "--Corporate", action="store_true", help="Add Corporate Corps")
parser.add_argument("-e", "--Exclude", help="Exclude a corporation.")
parser.add_argument("-c", "--Colonies", action="store_true", help="Add Colonies Corps")
parser.add_argument("-p", "--Prelude", action="store_true", help="Add Prelude Corps")
parser.add_argument("-pm", "--Premotional", action="store_true", help="Add Premotional Corps")
parser.add_argument("-cu", "--Custom",action="store_true", help="Add Custom Corps.")
parser.add_argument("-a", "--All", action="store_true", help="Add all Corps")

parser.add_argument("-cc", "--CreateCustom",action="store_true", help="Create custom corps.")

parser.add_argument("-cps", "--CreatePreset", action="store_true", help="Create a preset.")
parser.add_argument("-ps", "--Preset", help="Run a preset.")


args = parser.parse_args()

if args.Preset:
    cmd = "python3 corpsel.py "
    fname = "Presets/" + args.Preset + ".txt"
    with open(fname) as file:
        for line in file:
            cmd += line
    os.system(cmd)
    exit()

art.tprint('Corp Selector')

#List of corporations. Some are custom ones. 
corplist = ["United Nations Mars Initiative", "Thorgate", "Tharsis Republic", "Phoblog", "Inventrix", "Interplanetary Cinematics", "Mining Guild", "Helion", "Ecoline", "Credicor"]

Prelude = ["Cheung Shing Mars", "Point Luna", "Robinson Industries", "Valley Trust", "Vitor"]

Colonies = ["Aridor", "Arklight", "Polyphemos", "Poseidon", "Storm Craft Incorporated"]

Turmoil = ["LakeFront Resorts", "Pristar", "Utopia Invest", "Terralabs Research", "Septum Tribus"]

Premotional = ["Factorum", "Mons Insurance", "Philares", "Arcadian Communities", "Recyclon", "Splice Tactical Genomics"]

Corporate = ["Saturn Systems", "Terractor"]

Venus = ["Viron", "Morning Star Inc.", "Manutech", "Celestic", "Aphrodite"]

Custom = []

if os.path.isfile("custom_corps.txt"):
    with open("custom_corps.txt") as file:
        for line in file:
            if line.startswith('#') or line.strip() == "":
                continue
            Custom.append(line.strip())


if args.CreatePreset:
    fname = "Presets/"
    name = input("Enter name for preset:\n>")
    if not os.path.isdir("Presets"):
        os.system("mkdir Presets")
    fname += name + ".txt"
    
    with open(fname, 'w') as file:
        print("Args that follow command. For example, you ran this with 'python3 corpsel.py -cps'. just enter '-cps'. Or if you ran this with 'python3 corpsel.py -t -v' just enter '-t -v'")
        config = input("Enter args for preset:\n>")
        file.write(config)
        print("Preset created. To remove a preset simply delete the file")
        exit()

if args.CreateCustom:
    print("Press 'enter' when done adding custom corps.")
    while(True):
        corpCustom = input("Enter corp:")
        if corpCustom == "":
            exit()
        with open("custom_corps.txt", "a") as file:
            file.write(corpCustom + "\n")

if args.All:
    print("Adding all corps . . .")
    corplist = corplist + Prelude + Colonies + Turmoil + Premotional + Corporate + Venus + Custom

if args.Custom:
    print("Adding custom corps . . .")
    corplist = corplist + Custom

if args.Turmoil:
    print("Adding Turmoil corps . . .")
    corplist = corplist + Turmoil
    
if args.Venus:
    print("Adding Venus corps . . .")
    corplist = corplist + Venus

if args.Corporate:
    print("Adding Corporate corps . . .")
    corplist = corplist + Corporate
    
if args.Colonies:
    print("Adding Colonies corps . . .")
    corplist = corplist + Colonies

if args.Prelude:
   print("Adding Prelude corps . . .")
   corplist = corplist + Prelude
   
if args.Premotional:
   print("Adding Premotional corps . . .")
   corplist = corplist + Premotional

if args.Exclude:
    if args.Exclude in corplist:
        corplist.remove(args.Exclude)
    else:
        print("**Could not find %s in corplist. Unable to remove**" % (args.Exclude))
    
print(corplist)
    

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
    
    

