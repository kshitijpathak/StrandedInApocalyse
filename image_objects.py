from PIL import ImageTk, Image

class image_objects:
    """
    This class is used to instantiate all the images being used in th user interface. For example, the doors, the items in the inventory, player, zombies etc.
    Also contains the method to return the position of items which are dropped in a room.
    1. item_dict: conatins the images in proper format as compatible with tkinter
    2. item_locs: return the location where the items must be put in a room
    """
    def __init__(self):        

        # Reading and Creating Item images
        self.item_dict = {
            "door_west": ImageTk.PhotoImage(Image.open("./door_west.png")),
            "door_north": ImageTk.PhotoImage(Image.open("./door_north.png")),
            "door_south": ImageTk.PhotoImage(Image.open("./door_south.png")),
            "door_east": ImageTk.PhotoImage(Image.open("./door_east.png")),
            "Baby": ImageTk.PhotoImage(Image.open("./baby.png").resize((50, 50))),
            "Bag": ImageTk.PhotoImage(Image.open("./bag.png").resize((50, 50))),
            "AutomaticGun": ImageTk.PhotoImage(Image.open("./burstgun.png").resize((50, 50))),
            "Gun": ImageTk.PhotoImage(Image.open("./pistol.png").resize((50, 50))),
            "Knife": ImageTk.PhotoImage(Image.open("./knife1.png").resize((50, 50))),
            "Keys_The helicopter": ImageTk.PhotoImage(Image.open("./keys.png").resize((50, 50))),
            "Keys_Security Room": ImageTk.PhotoImage(Image.open("./keys.png").resize((50, 50))),
            "Keys_The admin office": ImageTk.PhotoImage(Image.open("./keys.png").resize((50, 50))),
            "Clothes": ImageTk.PhotoImage(Image.open("./clothes.png").resize((50, 50))),
            "Helicopter": ImageTk.PhotoImage(Image.open("./helicopter.png").resize((250, 250))),
            "Food": ImageTk.PhotoImage(Image.open("./food.png").resize((50, 50))),
            "Darryl": ImageTk.PhotoImage(Image.open("./player_male.png").resize((50, 50))),
            "Carol": ImageTk.PhotoImage(Image.open("./player_female.png").resize((50, 50))),
            "zombie1": ImageTk.PhotoImage(Image.open("./zombie1.png").resize((50, 50))),
            "zombie2": ImageTk.PhotoImage(Image.open("./zombie2.png").resize((50, 50))),
            "zombieMain": ImageTk.PhotoImage(Image.open("./zombieMain.png").resize((80, 80))),
            "gameover": ImageTk.PhotoImage(Image.open("./gameover.png").resize((300, 300))),
            "winner": ImageTk.PhotoImage(Image.open("./winner.png").resize((300, 300)))
        }

    # Function to return item locations ina room
    def item_locs(self, room_loc, width, height):
        """

        :param room_loc:
        :param width:
        :param height:
        :return:
        """
        x, y = room_loc
        x += 15
        y += 15
        self.item_location = []
        while x < room_loc[0]+width or y < room_loc[0]+height:
            self.item_location.append((x, y))
            x += 55
            y += 15
        return self.item_location


