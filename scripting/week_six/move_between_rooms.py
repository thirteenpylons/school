# Starter Code
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}
DIRECTIONS = ['North', 'South', 'East', 'West']
EXIT_COMMAND = "Exit"
VALID_INPUTS = DIRECTIONS + [EXIT_COMMAND]
INVALID_DIRECTION = "That is not a valid direction. You need to enter one of: " +\
    str(VALID_INPUTS) + "."
CANNOT_GO_THAT_WAY = "You bumped into a wall."
GAME_OVER = "Thanks for playing."
EXIT_ROOM_SENTINEL = "exit"

# IMPORTANT: When submitting to Sense, do not modify any code above this line or the function signature below.

def navigate(current_room: str, direction: str):
    """
    Given a current_room in rooms and a user_input, return a tuple (next_room, err_msg) with
    next_room -- where you are after or EXIT_ROOM_SENTINEL
    err_msg -- message to print, if any, empty, GAME_OVER, INVALID_DIRECTION, or CANNOT_GO_THAT_WAY
    """
    if direction == EXIT_COMMAND:
        return (EXIT_ROOM_SENTINEL, GAME_OVER)
    
    if direction not in VALID_INPUTS:
        return (current_room, INVALID_DIRECTION)
    
    if direction in rooms[current_room]:
        next_room = rooms[current_room][direction]
        return (next_room, '')
    else:
        return (current_room, CANNOT_GO_THAT_WAY)

    # Do not modify anything below this line. 
    
    return next_room, err_msg
