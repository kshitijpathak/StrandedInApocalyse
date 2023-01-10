import tkinter as tk
from Game import Game
from image_objects import image_objects
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class App:

    # Creates a Frame for the application and populates the GUI...
    def __init__(self, root):
        # Creating game class
        self.game = Game()
        self.player_check = 0
        self.root = root

        # creating some menu items
        menubar = tk.Menu()
        menubar.add_command(label="Quit", command=self.root.destroy)
        menubar.add_command(label="About", command=self.show_about)
        self.root.config(menu=menubar)

        # Create two frames owned by the window root.
        # In order to use multiple layout managers, the frames
        # cannot share a parent frame. Here both frames are owned
        # by a top level instance root.
        self.frame1 = tk.Frame(self.root, width=900, height=380, bg='#ADD8E6', borderwidth=2)
        self.frame1.grid_propagate(False)  # Prevents resizing
        self.frame2 = tk.Frame(self.root, width=900, height=220, bg='WHITE', borderwidth=2)
        self.frame2.grid_propagate(False)  # Prevents resizing
        self.frame3 = tk.Frame(self.root, width=900, height=150, bg='LIGHT GREY', borderwidth=2)
        self.frame3.grid_propagate(False)  # Prevents resizing
        # This packs both frames into the root window...
        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=1, column=0)
        self.frame3.grid(row=3, column=0)

        # Now add some useful widgets...
        self.text_area1 = tk.Label(self.frame2, text='')
        self.text_area1.place(x=450, y=100, anchor="center")
        # self.cmd_area = tk.Entry(self.frame3, text='')
        # self.cmd_area.place(x=450, y=10, anchor="center")

        # Initialising images objects
        self.ioj = image_objects()
        self.button_list = {}
        self.drop_list = {}


        # Initialising GUI elements like buttons, gates etc.
        self.build_GUI()

        # Opening the user activity log file
        timestamp = datetime.now().strftime("%d_%m_%y %H%M%S")
        self.log = open('./logs/log_'+str(timestamp)+'.txt', 'w')
        lines = f"Timestamp,Command,Current_Room,Player_Inventory"
        self.log.write(lines)


    def build_GUI(self):
        """
        This function initialises various UI elements which are to be embedded into the game sreen
        :return:
        """
        self.text_area1.configure(text="Select Player: 'Male' or 'Female'")

        # Creating buttons for different functions
        # Movement buttons
        self.move_north = tk.Button(self.frame3, text='Go North', fg='white', bg='#00008B',
                                    command=lambda: self.do_command("Go North"))
        self.move_south = tk.Button(self.frame3, text='Go South', fg='white', bg='#00008B',
                                    command=lambda: self.do_command("Go South"))
        self.move_east = tk.Button(self.frame3, text=' Go East ', fg='white', bg='#00008B',
                                   command=lambda: self.do_command("Go East"))
        self.move_west = tk.Button(self.frame3, text=' Go West ', fg='white', bg='#00008B',
                                   command=lambda: self.do_command("Go West"))
        self.move_up = tk.Button(self.frame3, text='   Go Upstairs  ', fg='white', bg='#00008B',
                                 command=lambda: self.do_command("Go Upstairs"))
        self.move_down = tk.Button(self.frame3, text='Go Downstairs', fg='white', bg='#00008B',
                                   command=lambda: self.do_command("Go Downstairs"))

        # Help button
        self.help = tk.Button(self.frame3, text='Help!', fg='white', bg='#00008B',
                              command=lambda: self.do_command("help"))
        # Quit Button
        self.quit = tk.Button(self.frame3, text='  Quit', fg='white', bg='#00008B',
                              command=self.root.destroy)

        # Player selection buttons
        self.male_player = tk.Button(self.frame3, text='Male   ♂', fg='white', bg='#00008B',
                                     command=lambda: self.do_command("Male"))
        self.male_player.place(x=380, y=10)
        self.female_player = tk.Button(self.frame3, text='Female ♀', fg='white', bg='#AA336A',
                                       command=lambda: self.do_command("Female"))
        self.female_player.place(x=440, y=10)

        # Inventory buttons
        self.inventory_options = tk.Button(self.frame3, text='Inventory', fg='white', bg='#00008B',
                                           command=lambda: self.show_inventory_options())
        self.pick_items = tk.Button(self.frame3, text='Pick Items', fg='white', bg='#00008B',
                                           command=lambda: self.do_command("Pick items"))
        self.drop_items = tk.Button(self.frame3, text='Drop/View Items', fg='white', bg='#00008B',
                                    command=lambda: self.do_command("Drop items"))
        self.view_items = tk.Button(self.frame3, text='View Items', fg='white', bg='#00008B',
                                    command=lambda: self.do_command("View items"))
        self.hide = tk.Button(self.frame3, text='     Hide     ', fg='white', bg='#00008B',
                                    command=lambda: self.hide_inventory_options())

        # Activity buttons
        self.use_knife = tk.Button(self.frame3, text='Use Knife', fg='white', bg='#00008B',
                                    command=lambda: self.do_command("Use Knife"))
        self.use_gun = tk.Button(self.frame3, text='Use Gun', fg='white', bg='#00008B',
                                   command=lambda: self.do_command("Use gun"))
        self.use_automaticgun = tk.Button(self.frame3, text='Use Rifle', fg='white', bg='#00008B',
                                   command=lambda: self.do_command("Use automaticgun"))
        self.unlock_heli = tk.Button(self.frame3, text='Unlock Helicopter', fg='white', bg='#00008B',
                                          command=lambda: self.do_command("Unlock Helicopter"))

        # Health Bar
        # Progress bar widget
        self.health_status = ttk.Progressbar(self.frame3, orient="horizontal", length=100, mode='determinate', value=100)
        self.health_label = tk.Label(self.frame3, text="Player Health", pady=0)


    def room_ui(self, frame, room_loc, width, height, room=None, door_details=None):
        """
        method to create UI for different rooms
        :return:
        """
        # create styling
        style1 = ttk.Style()
        # style1.configure('TSeparator', background='black' )
        style1.configure('TSeparator', background='black')

        # Unpacking room location
        x, y = room_loc

        # Creating walls for room
        # North wall
        ttk.Separator(frame, orient="horizontal", style='TSeparator', class_=ttk.Separator, takefocus=1,
                      cursor='cross').place(x=x, y=y, width=width)
        # South wall
        ttk.Separator(frame, orient="horizontal", style='TSeparator', class_=ttk.Separator, takefocus=1,
                      cursor='plus').place(x=x, y=y+height, width=width)
        # East wall
        ttk.Separator(frame, orient="vertical", style='TSeparator', class_=ttk.Separator, takefocus=1,
                      cursor='plus').place(x=x+width, y=y, height=height)
        # West wall
        ttk.Separator(frame, orient="vertical", style='TSeparator', class_=ttk.Separator, takefocus=1,
                      cursor='plus').place(x=x, y=y, height=height)

        # Placing items in room
        if len(room.itemsInRoom) > 0:
            locs = self.ioj.item_locs((x, y), width, height)[:(len(room.itemsInRoom)+1)]
            items_to_place = [item.__class__.__name__ for item in room.itemsInRoom ]
            i=0
            for item_image in items_to_place:
                command = "Pick " + item_image
                if item_image == "Keys":
                    item_image = item_image+"_"+room.itemsInRoom[0].keyOpens
                # Saving item objects as dictionary
                self.button_list[item_image] = tk.Button(frame, image=self.ioj.item_dict[item_image], borderwidth=0,
                                                         state="disabled", command=lambda command=command: self.do_command(command))
                self.button_list[item_image].photo = self.ioj.item_dict[item_image]
                self.button_list[item_image].place(x=locs[i][0], y=locs[i][1])
                i += 1

        # Placing doors if any
        if door_details is not None:
            for door in door_details:
                if room.isLocked:
                    self.doorButton = tk.Button(self.frame1, text="|        🔒        |" if door["dir"] == "north" or door["dir"] == "south" else "__\n\n🔒\n\n__",
                                                bg="black", fg="white", command=lambda: self.do_command("Unlock Door"))
                    self.doorButton.place(x=door["loc"][0], y=door["loc"][1])
                else:
                    # Create a Label Widget to display the text or Image
                    img=self.ioj.item_dict["door_north"] if door["dir"] == "north" else (self.ioj.item_dict["door_south"] if door["dir"] == "south" else
                                                                        (self.ioj.item_dict["door_east"] if door["dir"] == "east" else self.ioj.item_dict["door_west"]))
                    label = tk.Label(frame, image=img, borderwidth=0)
                    label.photo = img
                    label.place(x=door["loc"][0], y=door["loc"][1])


    def destroy_rooms(self):
        """
        This function is used to destroy the UI in order to update the visuals.
        :return:
        """
        for widget in self.frame1.winfo_children():
            widget.destroy()

    def create_room_UI(self, room):
        """
        This method creates the whole floor layout based on the floor attribute of the current room received as the arguments.
        :param room: current room location based on which floor layout is decided
        :return: None
        """
        self.destroy_rooms()  # destroy rooms to update

        # Creating rooms layout based on floor
        if room.level == "Basement":
            self.room_ui(self.frame1, room_loc=(0, 200), width=450, height=170, room=self.game.experimentLab)  # Experiment Lab room
            self.room_ui(self.frame1, room_loc=(450, 0), width=440, height=370, room=self.game.lobbyBasement)  # Lobby Basement room
            self.room_ui(self.frame1, room_loc=(800, 150), width=90, height=120, room=self.game.staircaseBasement,
                         door_details=[{"dir": "west", "loc": (780, 175)}])  # Staircase room
            self.room_ui(self.frame1, room_loc=(0, 0), width=450, height=200, room=self.game.containmentArea,
                         door_details=[{"dir": "south", "loc": (200, 195)},
                                       {"dir": "east", "loc": (445, 70)}])  # Containment Lab room
        elif room.level == "Ground":
            self.room_ui(self.frame1, room_loc=(450, 170), width=440, height=90, room=self.game.corridorGround)  # corridor room
            self.room_ui(self.frame1, room_loc=(0, 0), width=450, height=260, room=self.game.lobbyGround,
                         door_details=[{"dir": "east", "loc": (445, 182)}])  # Lobby Ground floor
            self.room_ui(self.frame1, room_loc=(0, 0), width=100, height=100, room=self.game.staircaseGround2,
                         door_details=[{"dir": "east", "loc": (95, 15)}])  # Staircase 2 room
            self.room_ui(self.frame1, room_loc=(0, 260), width=890, height=110, room=self.game.cateringHall,
                         door_details=[{"dir": "north", "loc": (560, 240)}])  # Kitchen/Common room
            self.room_ui(self.frame1, room_loc=(450, 0), width=440, height=170, room=self.game.securityRoom,
                         door_details=[{"dir": "west", "loc": (430, 60)},
                                       {"dir": "south", "loc": (660, 160)}])  # Security room
            self.room_ui(self.frame1, room_loc=(800, 170), width=90, height=90, room=self.game.staircaseGround1,
                         door_details=[{"dir": "west", "loc": (780, 180)}])  # staircase 1 room
        elif room.level == "First":
            self.room_ui(self.frame1, room_loc=(100, 0), width=400, height=150, room=self.game.corridorFirst)  # corridor room
            self.room_ui(self.frame1, room_loc=(0, 0), width=100, height=150, room=self.game.staircaseFirst1,
                         door_details=[{"dir": "east", "loc": (95, 40)}])  # Staircase 1 room
            self.room_ui(self.frame1, room_loc=(500, 0), width=390, height=150, room=self.game.changeRoom,
                         door_details=[{"dir": "west", "loc": (480, 40)},
                                       {"dir": "south", "loc": (670, 147)}])  # Change room
            self.room_ui(self.frame1, room_loc=(0, 150), width=390, height=220, room=self.game.adminOffice,
                         door_details=[{"dir": "north", "loc": (160, 140)},
                                       {"dir": "east", "loc": (385, 230)}])  # Admin room
            self.room_ui(self.frame1, room_loc=(390, 150), width=500, height=220, room=self.game.medicalRoom)  # Medical room
            self.room_ui(self.frame1, room_loc=(730, 290), width=160, height=80, room=self.game.staircaseFirst2,
                         door_details=[{"dir": "north", "loc": (780, 268)}])  # Staircase 2 room
        elif room.level == "Roof":
            self.room_ui(self.frame1, room_loc=(450, 0), width=440, height=370, room=self.game.openRoof,)  # Open Area
            self.room_ui(self.frame1, room_loc=(0, 0), width=450, height=370, room=self.game.helipad,
                         door_details=[{"dir": "east", "loc": (445, 180)}])  # Helipad
            self.room_ui(self.frame1, room_loc=(740, 270), width=150, height=100, room=self.game.staircaseRoof,
                         door_details=[{"dir": "north", "loc": (780, 248)}])  # Staircase roof
            self.room_ui(self.frame1, room_loc=(640, 0), width=250, height=130, room=self.game.maintenanceRoom,
                         door_details=[{"dir": "south", "loc": (740, 127)}])  # Maintenance room

    def move_character(self, pos):
        """
        Helps to place the player at correct locations depending on the room they are in
        :param pos: the position in pixels
        :return:
        """
        # creating the image and placing at appropriate location
        character_img = self.ioj.item_dict[self.game.player.username]
        label = tk.Label(self.frame1, image=character_img, borderwidth=0)
        label.photo = character_img
        label.place(x=pos[0], y=pos[1])

    def hide_inventory_options(self):
        """
        method used to hide inventory options (pick, drop etc)
        :return:
        """
        self.inventory_options.place(x=77, y=76)
        self.pick_items.place_forget()
        self.drop_items.place_forget()
        self.view_items.place_forget()
        self.hide.place_forget()

    def show_inventory_options(self):
        """
        method to show inventory options
        :return:
        """
        self.inventory_options.place_forget()
        self.pick_items.place(x=10, y=77)
        self.drop_items.place(x=81, y=77)
        # self.view_items.place(x=156, y=77)
        self.hide.place(x=186, y=77)

    def game_over(self, force=False):
        """
        Method checks the health and terminates the game is health is less than or equal to 0.
        :param force: if the game should terminate due to some other reasons aside from low health
        :return:
        """
        if self.game.player.health <= 0 or force:
            self.destroy_rooms()
            img = self.ioj.item_dict["gameover"]
            label = tk.Label(self.frame1, image=img, borderwidth=0)
            label.photo = img
            label.place(x=300, y=50)
            self.text_area1.configure(text="YOU DIED.....GAME OVER!!!")
            self.root.after(3000, self.root.destroy)

    def do_command(self, command=None):
        """
        method to execute the commands given by the button press
        :param command:
        :return:
        """
        if command is None:
            command = self.cmd_area.get()  # Returns a 2-tuple
        try:
            self.record_commands(command)
            self.process_command(command)
        except Exception as e:
            print(e)
        print("command: ", command)

    def record_commands(self, command):
        """
        Method to record the user activity log every time a user plays the game
        :param command:
        :return:
        """
        try:
            timestamp = datetime.now().strftime("%d_%m_%y %H%M%S")
            # writing some important information into the log file
            lines = f"\n{timestamp},{command},{self.game.current_room},{self.game.player.inventory if self.game.player is not None else 'No Item'}"
            self.log.write(lines)
        except ValueError as msg:
            print(msg)
        except AttributeError as msg:
            print(msg)
        except:
            print("That should not have happened..!!")

    def get_command_string(self, input_line):
        """
            Fetches a command (borrowed from old TextUI).
        :return: a 2-tuple of the form (command_word, second_word)
        """
        word1 = None
        word2 = None
        if input_line != "":
            all_words = input_line.split()
            word1 = all_words[0]
            if len(all_words) > 1:
                word2 = all_words[1]
            else:
                word2 = None
            # Just ignore any other words
        return word1, word2

    def process_command(self, command):
        """
        This method is used to process a command from the user to reflect in the ui.
        :param: command: a 2-tuple of the form (command_word, second_word)
        """

        # Checking for player health and decide survival
        if self.player_check != 0:
            self.game_over()

        command_word, second_word = self.get_command_string(command)
        if command_word is not None:
            command_word = command_word.lower()
            if second_word is not None:
                second_word = second_word.lower()
            # Whole If-else ladde takes care of different types of commands that the user can give
            if command_word == "pick" and self.player_check == 1:
                if second_word == "items":
                    if len(self.game.current_room.itemsInRoom) > 0:
                        # displaying available items
                        textLines = f"Choose item to pick:\n" \
                                    f"{['Pick ' + type(item).__name__ for item in self.game.current_room.itemsInRoom]}"
                        self.text_area1.configure(text=textLines)

                        # Changing button state from disabled to active
                        for thing in [type(item).__name__ for item in self.game.current_room.itemsInRoom]:
                            if thing == "Keys":
                                thing = thing + "_" + self.game.current_room.itemsInRoom[0].keyOpens
                            self.button_list[thing].configure(state="normal")
                    else:
                        self.text_area1.configure(text="!!..No Items to pick..!!\n\n" + self.game.story()[0])
                else:
                    # picking items here
                    item = [item for item in self.game.current_room.itemsInRoom if
                            type(item).__name__.lower() == second_word]
                    if len(item) == 0:
                        self.text_area1.configure(text="Don't know what you mean..!!\n\n" + self.game.story()[0])
                    else:
                        check = self.game.player.pickItems(item[0])
                        if check:
                            thing = type(item[0]).__name__

                            # Removing items from Room in UI
                            if thing == "Keys":
                                thing = thing + "_" + self.game.current_room.itemsInRoom[0].keyOpens
                            self.button_list[thing].place_forget()
                            self.game.current_room.remove_item(item[0])
                            self.text_area1.configure(text="Item Picked..!!\n\n" + self.game.story()[0])
                        elif check is False:
                            self.text_area1.configure(text="Max load exceeded. Item can't be picked..!!\nDrop some"
                                                           "items.\n\n" + self.game.story()[0])
            elif command_word == "drop" and self.player_check == 1:
                if second_word == "items":
                    if len(self.game.player.inventory) > 0:
                        # displaying items
                        textLines = f"Choose item to drop:\n" \
                                    f"{['Drop ' + type(item).__name__ for item in self.game.player.inventory]}"
                        self.text_area1.configure(text=textLines)

                        items_to_drop = [item.__class__.__name__ for item in self.game.player.inventory]
                        i = 0
                        # Showing items in inventory which can be dropped
                        for item_image in items_to_drop:
                            command = "Drop " + item_image
                            if item_image == "Keys":
                                item_image = item_image + "_" + self.game.player.inventory[i].keyOpens
                            self.drop_list[item_image] = tk.Button(self.frame3, image=self.ioj.item_dict[item_image],
                                                                     borderwidth=0,
                                                                     command=lambda command=command: self.do_command(command))
                            self.drop_list[item_image].photo = self.ioj.item_dict[item_image]
                            self.drop_list[item_image].place(x=290+i*60, y=90)
                            i += 1
                    else:
                        self.text_area1.configure(text="!!..No Items to drop..!!\n\n" + self.game.story()[0])
                else:
                    # dropping items here
                    item = [item for item in self.game.player.inventory if
                            type(item).__name__.lower() == second_word]
                    if len(item) == 0:
                        self.text_area1.configure(text="Don't know what you mean..!!\n\n" + self.game.story()[0])
                    else:
                        check = self.game.player.dropItems(item[0])
                        if check:
                            self.game.current_room.add_item(item[0])

                            # Adding the items back to room
                            thing = type(item[0]).__name__
                            if thing == "Keys":
                                thing = thing + "_" + item[0].keyOpens
                            self.drop_list[thing].place_forget()

                            # placing rooms
                            self.create_room_UI(self.game.current_room)

                            # moving character
                            self.move_character(self.game.story()[1])

                            self.text_area1.configure(text="Item Dropped..!!\n\n" + self.game.story()[0])
                        elif check is False:
                            self.text_area1.configure(text="!!..No Items to drop..!!\n\n" + self.game.story()[0])
            elif command_word == "view" and self.player_check == 1:
                if len(self.game.player.inventory) == 0:
                    textLines = f"!!..Inventory Empty..!!\n\n"
                else:
                    textLines = self.game.player.viewItems()
                    i = 0
                self.text_area1.configure(text=textLines + "\n\n" + self.game.story()[0])
            elif command_word == "help" and self.player_check == 1:
                self.text_area1.configure(text=self.game.print_help())
            elif command_word == "go" and self.player_check == 1:
                textLines = self.game.do_go_command(second_word)
                self.text_area1.configure(text=textLines[0])

                self.health_status['value'] = self.game.player.health

                # placing rooms
                self.create_room_UI(self.game.current_room)

                # moving character
                self.move_character(textLines[1])

                # Placing zombies and the 'use' buttons as per games progress
                if self.game.current_room.roomName == "corridorGround" and self.game.zombie1alive:
                    self.use_knife.place(x=500, y=27)
                    self.zombie1 = tk.Label(self.frame1, image=self.ioj.item_dict["zombie1"], borderwidth=0)
                    self.zombie1.photo = self.ioj.item_dict["zombie1"]
                    self.zombie1.place(x=630, y=190)
                elif self.game.current_room.roomName == "helipad" and self.game.zombieMainalive:
                    self.use_automaticgun.place(x=500, y=27)
                    self.zombieMain = tk.Label(self.frame1, image=self.ioj.item_dict["zombieMain"], borderwidth=0)
                    self.zombieMain.photo = self.ioj.item_dict["zombieMain"]
                    self.zombieMain.place(x=300, y=275)
                elif "Unlock Helicopter" in textLines[0]:
                    self.unlock_heli.place(x=500, y=27)

                if "GAME OVER" in textLines[0]:
                    self.root.after(4000, self.root.destroy)
            elif (command_word == "male" or command_word == "female") and self.player_check == 0:
                # creating some ui elements after user selects the player
                self.game.create_player(command_word)
                self.text_area1.configure(text=self.game.print_welcome())
                self.player_check = 1
                self.male_player.place_forget()
                self.female_player.place_forget()
                self.move_north.place(x=77, y=10)
                self.move_south.place(x=77, y=43)
                self.move_east.place(x=142, y=27)
                self.move_west.place(x=10, y=27)
                self.move_up.place(x=210, y=10)
                self.move_down.place(x=210, y=43)
                self.help.place(x=850, y=10)
                self.quit.place(x=850, y=42)
                self.health_status.place(x=790,y=90)
                self.health_label.place(x=792,y=115)
                self.inventory_options.place(x=77, y=76)
                # placing Basement rooms
                self.create_room_UI(self.game.current_room)
                # placing character
                self.move_character((200, 250))
            elif command_word == "use" and self.player_check == 1:
                if second_word == "knife":
                    textLines = self.game.knife1.cut()
                    if self.game.zombie1alive:
                        self.game.zombie1alive = False
                        self.text_area1.configure(
                            text=textLines + "\n" + "OH Damn, that zombie is dead...again !!" + "\n\n" + self.game.story()[0])
                        self.zombie1.destroy()
                    else:
                        self.text_area1.configure(
                            text=textLines + "\n" + "No Zombies here, you're safe!!" + "\n\n" + self.game.story()[0])
                    self.use_knife.place_forget()
                elif second_word == "gun":
                    status, textLines = self.game.pistol.shoot()
                    if status:
                        if self.game.zombie2alive:
                            self.game.zombie2alive = False
                            self.text_area1.configure(
                                text=textLines + "\n" + "OH Damn, that zombie is dead...again !!" + "\n\n" + self.game.story()[0])
                            self.zombie2.destroy()
                        else:
                            self.text_area1.configure(
                                text=textLines + "\n" + "No Zombies here, you're safe!!" + "\n\n" + self.game.story()[0])
                        self.use_gun.place_forget()
                elif second_word == "automaticgun":
                    status, textLines = self.game.burstgun.shoot()
                    if status:
                        if self.game.zombieMainalive:
                            self.game.zombieMainalive = False
                            self.text_area1.configure(
                                text=textLines + "\n" + "OH Damn, that zombie is dead...again !!" + "\n\n" + self.game.story()[0])
                            self.zombieMain.destroy()
                        else:
                            self.text_area1.configure(
                                text=textLines + "\n" + "No Zombies here, you're safe!!" + "\n\n" + self.game.story()[0])
                        self.final_win = tk.Button(self.frame3, text="Unlock Helicopter", fg='white', bg='#00008B',
                                                   command=lambda: self.do_command("Unlock Helicopter"))
                        self.final_win.place(x=500, y=27)
                        self.use_automaticgun.place_forget()
            elif command_word == "unlock" and self.player_check == 1:
                keys = [item for item in self.game.player.inventory if item.__class__.__name__ == "Keys"]
                self.text_area1.configure(text=f"Trying keys...!")
                if second_word == "door":
                    if len(keys) > 0:
                        for i in keys:
                            opened = i.unlock_door(self.game.next_room_locked)
                            if opened:
                                self.game.next_room_locked.isLocked = False
                                self.game.current_room = self.game.next_room_locked
                                self.text_area1.configure(
                                    text=f"Door is open. You may proceed further.\n\n" + self.game.story()[0])
                                # placing Basement rooms
                                self.create_room_UI(self.game.current_room)
                                # placing character
                                self.move_character(self.game.story()[1])
                                if self.game.current_room.roomName == "adminOffice" and self.game.zombie2alive:
                                    self.use_gun.place(x=500, y=27)
                                    self.zombie2 = tk.Label(self.frame1, image=self.ioj.item_dict["zombie2"], borderwidth=0)
                                    self.zombie2.photo = self.ioj.item_dict["zombie2"]
                                    self.zombie2.place(x=150, y=290)
                                break
                        if not opened:
                            self.text_area1.configure(text="Sorry no keys work. Please get the correct key..!!")
                    else:
                        self.text_area1.configure(text="No Keys in inventory..!!")
                elif second_word == "helicopter":
                    if len(keys) > 0:
                        for i in keys:
                            opened = i.unlock_door(self.game.helicopter)
                            if opened:
                                self.game.helicopter.isLocked = False
                                self.text_area1.configure(
                                    text=f"Door is open. You may proceed further.\n\n" + self.game.helicopter.fly())
                                self.destroy_rooms()
                                img = self.ioj.item_dict["winner"]
                                label = tk.Label(self.frame1, image=img, borderwidth=0)
                                label.photo = img
                                label.place(x=300, y=50)
                                self.log.close()
                                self.root.after(3000, self.root.destroy)
                                break
                        if not opened:
                            self.text_area1.configure(text="Sorry no keys work. Please get the correct key..!!")
                    else:
                        self.text_area1.configure(text="No Keys in inventory..!!")
            else:
                if self.player_check == 1:
                    # Handling Unknown commands...
                    self.text_area1.configure(
                        text=f"Don't know what you mean. Please choose correct option.\n\n{self.game.print_help()}")
                else:
                    self.text_area1.configure(
                        text=f"Don't know what you mean. Please choose correct option.\n\nSelect Player: 'Male' or 'Female'")

    def show_about(self):
        """
        method show about information as a messagebox
        :return:
        """
        msg = f"'Stranded in Apocalypse' a call from distant future.\n\nThere has been a global zombie break-out due to" \
              f" some malfunctioned military experiments. Whole world is in chaos. You are the last beacon of hope. You have to save the humanity by" \
              f" delivering an experimental child to a secret lab at other end of the city. Whole infrastructure has collapsed and you are" \
              f" humanity's last hope. Scientists at the lab are waiting for you to bring the child so that they can manufacture a vaccine.\n\n\
                Developed By: Kshitij Pathak"
        messagebox.showinfo("**Stranded in Apocalypse**", msg)


def main():
    win = tk.Tk()  # Create a window
    win.title("**Stranded in Apocalypse**")  # Set window title
    win.geometry("900x750")  # Set window size
    win.resizable(False, False)  # Both x and y dimensions...

    # Create the GUI as a Frame and attach it to the window...
    myApp = App(win)

    # Call the GUI mainloop...
    win.mainloop()


if __name__ == "__main__":
    main()
