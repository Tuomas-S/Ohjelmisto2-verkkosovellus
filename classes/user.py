import time
import random
import json
from pathlib import Path
from classes.items import *
from classes.locations import *
from misc.text_format import *
from collections import deque

class User:
    def __init__(self, name, age, location, status, inventory):
        self.name = name # pelaajan asettama nimi
        self.age = age # pelaajan asettama ikä
        self.location = location # nykyinen sijainti
        self.status = status # pelaajan tämänhetkinen tilanne
        self.inventory = inventory # inventaario

    def to_dictionary(self):
        return {
            "name": self.name,
            "age": self.age,
            "location": self.location.name,
            "status": self.status,
            "inventory": [item.name for item in self.inventory] if self.inventory else []
        }


    # Pelin tallennus
    def save_game(self):
        data = {
            "items": [item.to_dictionary() for item in allItems],
            "locations": [location.to_dictionary() for location in allLocations],
            "user": self.to_dictionary()
        }
        with open(Path(__file__).parents[1]/"progress"/"save_data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    # Pelin lataus
    def load_game(self, path):
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        itemLookup = {item.name: item for item in allItems}
        locationLookup = {location.name: location for location in allLocations}

        # Ladataan esineet
        for itemData in data["items"]:
            item = itemLookup[itemData["name"]]
            item.name = itemData["name"]
            item.foundText = itemData["foundText"]
            item.usedText = itemData["usedText"]
            item.itemNotUsed = itemData["itemNotUsed"]
            item.isSingleUse = itemData["isSingleUse"]
            item.usedIn = [locationLookup[locationName] for locationName in itemData["usedIn"]]

        # Ladataan sijainnit
        for locationData in data["locations"]:
            location = locationLookup[locationData["name"]]
            location.name = locationData["name"]
            location.searchText = locationData["searchText"]
            location.isLocked = locationData["isLocked"]
            location.lockedText = locationData["lockedText"]
            location.hasItem = [itemLookup[itemName] for itemName in locationData["hasItem"]]
            location.acceptsItem = [itemLookup[itemName] for itemName in locationData["acceptsItem"]]
            location.connections = [locationLookup[locationName] for locationName in locationData["connections"]]

        # Ladataan käyttäjä
        userData = data["user"]
        self.name = userData["name"]
        self.age = userData["age"]
        self.location = locationLookup[userData["location"]]
        self.status = userData["status"]
        self.inventory = [itemLookup[itemName] for itemName in userData["inventory"]]


    # Uuden pelin aloittaminen
    def new_game(self):
        if os.path.exists("peliprojekti/progress/save_data.json"):
            clear_shell()
            choice = input("╭──────────────────────────────────────────────╮ \n"
                           "│ Haluatko varmasti aloittaa uuden pelin?      │ \n"
                           "│ Sinulla on keskeneräinen tallennus.          │ \n"
                           "╰──────────────────────────────────────────────╯ \n\n"
                           '  Kirjoita "ok" vahvistaaksesi. \n'
                           "  [enter] = peruuta \n\n"
                           "  Valitse toiminto: ")
            if choice.lower() == "ok":
                os.remove(Path(__file__).parents[1]/"progress"/"save_data.json")
            else:
                self.main_menu()
                return
            
        clear_shell()
        print("╭────────────────────────────────╮ \n"
              "│ Luodaan uusi profiili.         │ \n"
              "╰────────────────────────────────╯ \n")
        player.name = input("  Nimi: ")
        player.age = input("  Ikä:  ")
        while True:
            try:
                int(player.age)
            except ValueError:
                player.age = input("  Anna ikä numerona: ")
            else:
                break
        player.age = int(player.age)

        if player.age < 12:
            input(f"{fancyLine}  Olet alaikäinen, suljetaan sovellus...")
            exit()
        else:
            input(f"{fancyLine}  Tervetuloa {player.name}! \n  [enter] = aloita peli")
            clear_shell()


    # Pelaajan liikkuminen
    def find_path(self, target):
        queue = deque([(self.location, [self.location])])
        visited = {self.location}

        while queue:
            current, path = queue.popleft()
            if current == target:
                return path[1:]

            for neighbor in current.connections:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    def move(self):
        clear_shell()
        choice = input("  ╭───────────────═══════════════════───────═════╗\n"
                       "  │                                         ^    ║\n"
                       "  │           皿  ⌂ ⌂                       N    ║\n"
                       "  ║    ╭╌╌ [ Keskusta ] ══╤═ [ Koti ][ Kellari ] ║\n"
                       "  ║    ┆        ║ ⌂⌂      │      ┆   ♣Ψ         ─╢\n"
                       "  │ [ Kuja ]  ⌂ ║         ╰─ [ Metsä ] ╌╌╌╮      │\n"
                       "  │    ┆        ║    [ Vaja ] ╌╯ │ ⌂      ┆      │\n"
                       "  ║    ┆    [ Kauppa ]         ♣ │    [ Raunio ] ║\n"
                       "  ╠═   ┆                         │ Ψ      ┆      ║\n"
                       "  ║    ╰╌ [ Varasto ] † †    [ Pelto ] ╌╌╌╯      ║\n"
                       "  ║                    †                 ~~~     │\n"
                       "  ║                        ▲▲                    │\n"
                       "  ╚═════════─────════════────────────────────────╯\n\n"
                       "  Liiku kirjoittamalla sijainnin nimi.\n"
                       "  [enter] = takaisin\n\n"
                       "  Valitse toiminto: ")
        if choice == "":
            return

        target = next((location for location in allLocations if location.name.lower() == choice.lower()), None)
        if not target:
            input(f"{fancyLine}  Sijaintia ei löytynyt.")
            self.move()

        path = self.find_path(target)
        for step in path:
            print(f"  Siirrytään: {step.name}...")
            time.sleep(random.randrange(1, 3))
            if step.isLocked:
                input(fancyLine + divide(step.lockedText))
                break
            self.location = step

    # Sijainnin tutkiminen
    def search(self):
        input(fancyLine + divide(self.location.searchText))
        if self.location.hasItem == []:
            input("\n  Et löytänyt alueelta mitään mukaan otettavaa.")
            clear_shell()

        else:
            for item in self.location.hasItem:
                input(f"\n{divide(item.foundText)}")
                self.inventory.append(item)
            self.location.hasItem = []


    # Esineen käyttäminen
    def item_use(self, choice):
        for item in self.inventory:
            if choice.lower() == item.name.lower():
                if item in self.location.acceptsItem:
                    if self.location in item.usedIn:
                        input(f"{fancyLine}  Olet jo käyttänyt esineen tässä paikassa.")
                        break
                    print("  Käytetään esine...")
                    time.sleep(random.randrange(1, 3))
                    input(fancyLine + divide(item.usedText))
                    item.usedIn.append(self.location)
                    if item.isSingleUse:
                        self.inventory.remove(item)
                    break
                else:
                    input(fancyLine + divide(item.itemNotUsed))
                    break
        else:
            input(f"{fancyLine}  Esinettä ei löytynyt inventaariostasi.")
            self.inv_show()
        
    # Inventaario ja esineen valinta
    def inv_show(self):
        clear_shell()
        if self.inventory == []:
            input("╭───────────────────────────────────────╮ \n"
                  "│ Inventaariosi on tyhjä.               │ \n"
                  "│ Täältä näet löytämäsi esineet.        │ \n"
                  "╰───────────────────────────────────────╯ \n\n"
                  "  [enter] = takaisin")
            
        else:
            print("╭─────────────────────────────────────────╮ \n"
                  "│ Inventaariossasi on:                    │")
            for item in self.inventory:
                print(f"│ » {item.name:<38}│")
            choice = input("╰─────────────────────────────────────────╯ \n\n"
                           "  Käytä esine kirjoittamalla sen nimi. \n"
                           "  [enter] = takaisin \n\n"
                           "  Valitse toiminto: ")
            if choice != "":
                self.item_use(choice)


    # Päävalikko
    def main_menu(self):
        clear_shell()
        hasSave = (Path(__file__).parents[1]/"progress"/"save_data.json").exists()
        if hasSave:
            choice = input("╭────────────────────────────────────────────────────╮ \n"
                           "│                OPERAATIO PERUSKOULU                │ \n"
                           "│                     ──◇ ◆ ◇──                      │ \n"
                           "│                TEKIJÄ: Tuomas Soini                │ \n"
                           "╰────────────────────────────────────────────────────╯ \n\n"
                           "  [1] = Uusi peli \n"
                           "  [2] = Jatka peliä \n"
                           "  [3] = Avaa ohjeet \n"
                           "  [4] = Sulje sovellus \n\n"
                           "  Valitse toiminto: ")
            
        else:
            choice = input("╭────────────────────────────────────────────────────╮ \n"
                           "│                OPERAATIO PERUSKOULU                │ \n"
                           "│                     ──◇ ◆ ◇──                      │ \n"
                           "│                TEKIJÄ: Tuomas Soini                │ \n"
                           "╰────────────────────────────────────────────────────╯ \n\n"
                           "  [1] = Uusi peli \n"
                           "  [2] = Avaa ohjeet \n"
                           "  [3] = Sulje sovellus \n\n"
                           "  Valitse toiminto: ")
            
        if choice == "1":
            self.new_game()
        elif hasSave and choice == "2":
            self.load_game(Path(__file__).parents[1]/"progress"/"save_data.json")
        elif (hasSave and choice == "3") or (not hasSave and choice == "2"):
            clear_shell()
            with open(Path(__file__).parents[1]/"misc"/"instructions.txt", "r", encoding = "utf-8") as file:
                data = file.readlines()
            for line in data:
                print(line.rstrip("\n"))
            input(f"{fancyLine} [enter] = takaisin")
            self.main_menu()
        elif (hasSave and choice == "4") or (not hasSave and choice == "3"):
            clear_shell()
            choice = input("╭────────────────────────────────────╮ \n"
                           "│ Haluatko sulkea sovelluksen?       │ \n"
                           "╰────────────────────────────────────╯ \n\n"
                           '  Kirjoita "ok" vahvistaaksesi. \n'
                           "  [enter] = peruuta \n\n"
                           "  Valitse toiminto: ")
            if choice.lower() == "ok":
                exit()
            self.main_menu()
        else:
            input(f"{fancyLine}  Kyseistä toimintoa ei löydy. Valitse toiminto \n  kirjoittamalla sitä vastaava numero.")
            self.main_menu()


    # Pelin sisäinen valikko
    def game_menu(self, mission):
        clear_shell()
        self.save_game()
        choice = input("╭─────────────────────────────────────────────────────╮ \n"
                      f"│ [⌂] SIJAINTI: {self.location.name:<38}│ \n"
                      f"│ [≡] TEHTÄVÄ:  {mission:<38}│ \n"
                       "╰─────────────────────────────────────────────────────╯ \n\n"
                       "  [1] = Vaihda sijaintia \n"
                       "  [2] = Tutki aluetta \n"
                       "  [3] = Avaa inventaario \n"
                       "  [4] = Sulje sovellus \n\n"
                       "  Valitse toiminto: ")
        if choice == "1":
            self.move()
        elif choice == "2":
            print("  Tutkitaan aluetta...")
            time.sleep(random.randrange(1,3))
            self.search()
        elif choice == "3":
            print("  Avataan inventaario...")
            time.sleep(1)
            self.inv_show()
        elif choice == "4":
            clear_shell()
            choice = input("╭────────────────────────────────────╮ \n"
                           "│ Haluatko sulkea sovelluksen?       │ \n"
                           "╰────────────────────────────────────╯ \n\n"
                           '  Kirjoita "ok" vahvistaaksesi. \n'
                           "  [enter] = peruuta \n\n"
                           "  Valitse toiminto: ")
            if choice.lower() == "ok":
                exit()
        else:
            input(f"{fancyLine}  Kyseistä toimintoa ei löydy. Valitse toiminto \n  kirjoittamalla sitä vastaava numero.")


# Luodaan pelaaja self, name, age, location, status, inventory
player = User(
    name = "",
    age = 0,
    location = koti,
    status = "Pakkaa tavarasi mukaan",
    inventory = []
)