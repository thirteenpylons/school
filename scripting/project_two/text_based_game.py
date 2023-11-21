"""

TODO:
    Print surrounding rooms
    Print instructions
    Print inventory
    Boss shouldn't be moving after every input, only after moving.

Author: Christian M. Fulton
Date: 20.Nov.23
"""
import random
from colorama import init, Fore


init(autoreset=True)

class Game:
    def __init__(self):
        self.rooms: dict = {
            'Lobby': {'North': 'Steves office', 'East': 'Lunch room', 'South': 'Restrooms', 'West': 'Players office', 'item': None},
            'Players office': {'North': 'Conference room', 'East': 'Lobby', 'item': 'laptop'},
            'Conference room': {'East': 'Steves office', 'South': 'Players office', 'item': 'printer'},
            'Steves office': {'West': 'Conference room', 'South': 'Lobby', 'item': 'paper'},
            'Lunch room': {'North': 'Bosses room', 'West': 'Lobby', 'South': 'MDF', 'item': 'sandwich'},
            'Bosses room': {'South': 'Lunch room', 'item': None},
            'MDF': {'North': 'Lunch room', 'item': 'router'},
            'Restrooms': {'North': 'Lobby', 'South': 'Storage', 'item': None},
            'Storage': {'North': 'Restrooms', 'item': 'ink'},
        }
        self.current_room: str = 'Lobby'
        self.inventory: dict = {'ink': False, 'paper': False, 'sandwich': False, 'router_rebooted': False, 'printer_loaded': False}
        self.villain: str = 'Boss'
        self.villain_encountered: bool = False
        self.game_running: bool = True

    def show_surrounding_rooms(self) -> None:
        print(f"\nYou are currently in the {self.current_room}.")
        print("Surrounding rooms:")
        for direction, room in self.rooms[self.current_room].items():
            if direction in ['North', 'South', 'East', 'West']:  # Filter out non-direction keys
                print(f"\t{direction}: {room}")

    def show_instructions(self) -> None:
        print("\nCubicle Quest: The Great Paper Chase")
        print("\tCollect ink and paper and load the printer, reboot the router and print your reports.")
        print("\tGrab the sandwich from the Lunch room to dodge the boss the first time.")
        print("\nTo see surrounding rooms: look around")
        print("\nMove commands: go north, go east, go south, go west")
        print("\nAdd to Inventory: get 'item name'")
        print("\nSpecial commands: reboot router, load printer, print reports\n")

    def show_inventory(self) -> None:
        current_inventory = [item for item, has in self.inventory.items() if has]
        if not current_inventory:
            print(COLORS["inventory"] + "Your inventory is empty.")
        else:
            print(f"Inventory: {', '.join(current_inventory)}")
    
    def move(self, direction: str) -> None:
        """
        Move direction if possible and MOVE THE BOSS
        If item is in room, tell player about the item.
        If move is not possible, tell player it's not possible.
        """
        if direction in self.rooms[self.current_room]:
            self.current_room = self.rooms[self.current_room][direction]
            print(Fore.LIGHTGREEN_EX + f"You moved to the {self.current_room}.")
            self.move_villain()
            if self.rooms[self.current_room]['item']:
                print(Fore.LIGHTYELLOW_EX + f"You see a {self.rooms[self.current_room]['item']} here.")
        else:
            print("You can't go that way.")

    def move_villain(self) -> None:
        # Get the list of possible rooms to which the villain can move
        possible_rooms = list(self.rooms.keys())
        # Remove the current room of the villain to avoid staying in place
        possible_rooms.remove(self.villain)
        # Move the villain to a random room, excluding the 'item' and 'Start' room
        new_room = random.choice([room for room in possible_rooms if room not in ['item', 'Start']])
        self.villain = new_room
        print(Fore.RED + f"The boss is now in the {self.villain}.")

    def get_item(self, item: str) -> None:
        if item in ['sandwich', 'ink', 'paper'] and self.rooms[self.current_room].get('item') == item:
            self.inventory[item] = True
            self.rooms[self.current_room]['item'] = None
            print(Fore.GREEN + f"You picked up {item}.")
        else:
            print(Fore.MAGENTA + "There is nothing to pick up here.")

    def reboot_router(self) -> None:
        if self.current_room == 'MDF':
            self.inventory['router_rebooted'] = True
            print(Fore.GREEN + "You rebooted the router.")
        else:
            print(Fore.MAGENTA + "There's no router here to reboot.")

    def load_printer(self) -> None:
        if self.current_room == 'Conference room' and self.inventory['ink'] and self.inventory['paper']:
            self.inventory['printer_loaded'] = True
            print(Fore.GREEN + "You loaded the printer with ink and paper.")
        else:
            print("You need ink and paper to load the printer.")

    def eat_sandwich(self) -> None:
        if self.inventory['sandwich']:
            self.inventory['sandwich'] = False
            print("You ate the sandwich. Yum!")
        else:
            print("You have no sandwich to eat.")

    def print_reports(self) -> None:
        if self.current_room == 'Players office' and self.inventory['printer_loaded'] and self.inventory['router_rebooted']:
            print(Fore.GREEN + "You have printed the reports.")
            print(Fore.CYAN + "Congratulations, You win the game!")
            self.game_running = False
        else:
            if not self.inventory['router_rebooted']:
                print(Fore.MAGENTA + "You need to reboot the router!")
            if not self.inventory['printer_loaded']:
                print(Fore.MAGENTA + "You need to load the printer with ink and paper!")

    def start_game(self) -> None:
        self.show_instructions()
        print("You need to print your reports that are due to your boss before he catches you.")
        print(Fore.YELLOW + f"You are currently in the {self.current_room}")
        self.villain = random.choice([room for room in self.rooms if room != self.current_room and room != 'item'])

        while self.game_running:
            command = input("What do you want to do? ").split()
            
            # Handle single word commands first
            if command[0] == 'quit':
                print("Quitting the game...")
                self.game_running = False
                continue

            # Validate the command has two parts
            if len(command) < 2:
                print("Invalid command.")
                continue

            action, item = command[0], command[1]

            if action == 'go':
                self.move(item.capitalize())
            elif action == 'show' and item == 'inventory':
                self.show_inventory()
            elif action == 'show' and item == 'instructions':
                self.show_instructions()
            elif action == 'look' and item == 'around':
                self.show_surrounding_rooms()
            elif action == 'get':
                self.get_item(item)
            elif action == 'reboot' and item == 'router':
                self.reboot_router()
            elif action == 'load' and item == 'printer':
                self.load_printer()
            elif action == 'eat' and item == 'sandwich':
                self.eat_sandwich()
            elif action == 'print' and item == 'reports':
                self.print_reports()
            else:
                print("I don't understand that command.")
                        
            # Check if the player is in the same room as the villain
            if self.current_room == self.villain:
                if self.inventory['sandwich']:
                    print(Fore.GREEN + "You hand your boss a sandwich!")
                    self.inventory['sandwich'] = False
                else:
                    print(Fore.LIGHTRED_EX + "You bumped into your boss and he fired you... Game over!")
                    self.game_running = False

        print(Fore.GREEN + "Thanks for playing!")

# Create a game instance and start the game
if __name__ == "__main__":
    office_game = Game()
    office_game.start_game()
