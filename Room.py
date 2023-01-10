"""
    The Room class is used to create places where the character can roam around.
    It's attributes are:
    1. roomName: name of the room
    2. Description: more info about the room
    3. level : on which level is the room
    4. itemsInRoom: which items can be found within the room
    5. isLocked: is the room locked or not
"""

class Room:

    def __init__(self, roomName, description, level, itemsInRoom, isLocked=False):
        """
            Constructor method.
        :param description: Text description for this room
        """
        self.roomName = roomName
        self.isLocked = isLocked
        self.description = description
        self.level = level
        self.exits = {}  # Dictionary
        self.itemsInRoom = itemsInRoom

    def set_exit(self, direction, neighbour):
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room).
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour

    def get_short_description(self):
        """
            Fetch a short text description about the room details.
        :return: text description
        """
        return self.description

    def get_long_description(self):
        """
            Fetch a longer description including available exits and items present in room.
        :return: text description
        """
        return f'Location: {self.description}, Level: {self.level}, Exits: {self.get_exits()}, Items in Room: {[item.description for item in self.itemsInRoom]}.'

    def get_exits(self):
        """
            Fetch all available exits as a list.
        :return: list of all available exits
        """
        all_exits = list(self.exits.keys())
        return all_exits

    def get_exit(self, direction):
        """
            Fetch an exit in a specified direction.
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None

    def add_item(self, item):
        """
        Method to Add objects to the room
        :param item: object to be added to the room
        :return: None
        """
        try:
            self.itemsInRoom.append(item)
        except NameError as msg:
            print(msg)

    def remove_item(self, item):
        """
        Method to remove objects from the room
        :param item: object to be removed from the room
        :return:None
        """
        try:
            self.itemsInRoom.remove(item)
        except NameError as msg:
            print(msg)

