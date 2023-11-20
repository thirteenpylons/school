"""
Author: Christian M. Fulton
Date: 20.Nov.23
"""
import random


class Game:
    def __init__(self):
        self.rooms = {
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
        self.current_room = 'Lobby'
        self.inventory = {'ink': False, 'paper': False, 'sandwich': False, 'router_rebooted': False, 'printer_loaded': False}
        self.villain = 'Boss'
        self.villain_encountered = False
        self.game_running = True

    def move(self, direction):
        if direction in self.rooms[self.current_room]:
            self.current_room = self.rooms[self.current_room][direction]
            print(f"You moved to the {self.current_room}.")
            if self.rooms[self.current_room]['item']:
                print(f"You see a {self.rooms[self.current_room]['item']} here.")
        else:
            print("You can't go that way.")

    def move_villain(self):
        # Get the list of possible rooms to which the villain can move
        possible_rooms = list(self.rooms.keys())
        # Remove the current room of the villain to avoid staying in place
        possible_rooms.remove(self.villain)
        # Move the villain to a random room, excluding the 'item' and 'Start' room
        new_room = random.choice([room for room in possible_rooms if room not in ['item', 'Start']])
        self.villain = new_room
        print(f"The boss is now in the {self.villain}.")

    def get_item(self, item):
        if item in ['sandwich', 'ink', 'paper'] and self.rooms[self.current_room].get('item') == item:
            self.inventory[item] = True
            self.rooms[self.current_room]['item'] = None
            print(f"You picked up {item}.")
        else:
            print("There is nothing to pick up here.")

    def reboot_router(self):
        if self.current_room == 'MDF':
            self.inventory['router_rebooted'] = True
            print("You rebooted the router.")
        else:
            print("There's no router here to reboot.")

    def load_printer(self):
        if self.current_room == 'Conference room' and self.inventory['ink'] and self.inventory['paper']:
            self.inventory['printer_loaded'] = True
            print("You loaded the printer with ink and paper.")
        else:
            print("You need ink and paper to load the printer.")

    def eat_sandwich(self):
        if self.inventory['sandwich']:
            self.inventory['sandwich'] = False
            print("You ate the sandwich. Yum!")
        else:
            print("You have no sandwich to eat.")

    def print_reports(self):
        if self.current_room == 'Players office' and self.inventory['printer_loaded'] and self.inventory['router_rebooted']:
            print("You have printed the reports.")
            print("Congratulations, You win the game!")
            self.game_running = False
        else:
            if not self.inventory['router_rebooted']:
                print("You need to reboot the router!")
            if not self.inventory['printer_loaded']:
                print("You need to load the printer with ink and paper!")

    def start_game(self):
        print("You need to print your reports that are due to your boss before he catches you.")
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

            if action == 'move':
                self.move(item.capitalize())
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
            
            self.move_villain()
            
            # Check if the player is in the same room as the villain
            if self.current_room == self.villain:
                if self.inventory['sandwich']:
                    print("You hand your boss a sandwich!")
                    self.inventory['sandwich'] = False
                else:
                    print("You bumped into your boss and he fired you... Game over!")
                    self.game_running = False

        print("Thanks for playing!")

# Create a game instance and start the game
office_game = Game()
office_game.start_game()
