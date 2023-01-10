"""
    This class is the model class of the "Stranded in Apocalypse" application.
    "Stranded in Apocalypse" is a basic, UI based adventure game.
    You wake up to a post apocalyptic world. Zombies have taken over.
    It's a miracle that you're still alive. You are humanity's last hope.
    The military scientists created a zombie virus while developing super soldiers.
    The key to an antidote to the virus is a human experiment in the Containment area.
    Safely deliver the child to the Area-51 lab to save the world.
    You best chance to reach there is a helicopter at the roof.
    HURRY...!! The world is running out of time. Tick Tock..!!
"""

from Room import Room
from Player import Player
import Inventory as inv


class Game:

    def __init__(self):
        """
        Initialises the game.
        """
        self.create_objects()
        self.create_rooms()
        self.current_room = self.experimentLab
        self.next_room_locked = self.securityRoom
        self.player = None
        self.zombie1alive = True
        self.zombie2alive = True
        self.zombieMainalive = True

    #  Creating objects
    def create_objects(self):
        """
        Creates objects used throughout the game
        :param:None
        :return: None
        """
        self.baby = inv.Baby(15, "The Baby: Last hope of humanity.")  #
        self.bag1 = inv.Bag(50, 10, "Bag to hold items.")  #
        self.burstgun = inv.AutomaticGun(30, 30, 30, "Burst Fire - AR15 rifle.")  #
        self.pistol = inv.Gun(6, 6, 20, "Glock Pistol.")  #
        self.knife1 = inv.Knife(10, "Sharp surgery knife")  #
        self.knife2 = inv.Knife(10, "Sharp kitchen knife")  #
        self.keysToHeli = inv.Keys(5, "Keys to Helicopter", "The helicopter")  #
        self.keysToSecRoom = inv.Keys(5, "Keys to Security Room", "Security Room")  #
        self.keysToAdminRoom = inv.Keys(5, "Keys to Admin Office", "The admin office")  #
        self.protectiveClothes = inv.Clothes(20, "Protective clothes")  #
        self.helicopter = inv.Helicopter("The helicopter")  #

    # Create rooms and set directions
    def create_rooms(self):
        """
            Sets up all room assets.
        :return: None
        """
        # ********************* Creating Rooms *********** ADD ITEMS IN ROOM HERE *****
        # Basement Level
        self.experimentLab = Room("experimentLab", "The Top Secret dark experiments lab", 'Basement',
                                  [self.knife1])
        self.containmentArea = Room("containmentArea", "The Containment lab Virus source", 'Basement',
                                    [self.baby, self.protectiveClothes])
        self.lobbyBasement = Room("lobbyBasement", "The lobby", 'Basement', [self.keysToSecRoom])
        self.staircaseBasement = Room("staircaseBasement", "The staircase to ground floor", 'Basement', [])

        # Ground floor
        self.corridorGround = Room("corridorGround", "The corridor.", 'Ground', [self.bag1])
        self.lobbyGround = Room("lobbyGround", "The lobby", 'Ground', [])
        self.securityRoom = Room("securityRoom", "Security Room", 'Ground', [self.burstgun, self.pistol], True)
        self.cateringHall = Room("cateringHall", "The kitchen and common area", 'Ground', [self.knife2])
        self.staircaseGround1 = Room("staircaseGround1", "The staircase from basement", 'Ground', [])
        self.staircaseGround2 = Room("staircaseGround2", "The staircase to the first floor", 'Ground', [self.keysToAdminRoom])

        # First floor
        self.corridorFirst = Room("corridorFirst", "The corridor", 'First', [])
        self.adminOffice = Room("adminOffice", "The admin office", 'First', [self.keysToHeli], True)
        self.changeRoom = Room("changeRoom", "The washrooms and changing rooms", 'First', [])
        self.medicalRoom = Room("medicalRoom", "The medical facilities and pharmacy", 'First', [])
        self.staircaseFirst1 = Room("staircaseFirst1", 'The staircase from the ground floor', 'First', [])
        self.staircaseFirst2 = Room("staircaseFirst2", 'The staircase to the roof', 'First', [])

        # Roof level
        self.staircaseRoof = Room("staircaseRoof", 'The staircase to/from first floor.', 'Roof', [])
        self.maintenanceRoom = Room("maintenanceRoom", 'The maintenance room.', 'Roof', [])
        self.openRoof = Room("openRoof", 'The open area.', 'Roof', [])
        self.helipad = Room("helipad", 'The helipad.', 'Roof', [self.helicopter])

        ######################## Setting directions ############################

        # Basement Level
        self.experimentLab.set_exit('north', self.containmentArea)
        self.containmentArea.set_exit('east', self.lobbyBasement)
        self.containmentArea.set_exit('south', self.experimentLab)
        self.lobbyBasement.set_exit('west', self.containmentArea)
        self.lobbyBasement.set_exit('east', self.staircaseBasement)
        self.staircaseBasement.set_exit('west', self.lobbyBasement)
        self.staircaseBasement.set_exit('upstairs', self.staircaseGround1)

        # Ground floor
        self.staircaseGround1.set_exit('downstairs', self.staircaseBasement)
        self.staircaseGround1.set_exit('west', self.corridorGround)
        self.corridorGround.set_exit('east', self.staircaseGround1)
        self.corridorGround.set_exit('north', self.securityRoom)
        self.corridorGround.set_exit('south', self.cateringHall)
        self.corridorGround.set_exit('west', self.lobbyGround)
        self.securityRoom.set_exit('west', self.lobbyGround)
        self.securityRoom.set_exit('south', self.corridorGround)
        self.cateringHall.set_exit('north', self.corridorGround)
        self.lobbyGround.set_exit('east', self.corridorGround)
        self.lobbyGround.set_exit('west', self.staircaseGround2)
        self.staircaseGround2.set_exit('east', self.lobbyGround)
        self.staircaseGround2.set_exit('upstairs', self.staircaseFirst1)

        # First floor
        self.staircaseFirst1.set_exit('downstairs', self.staircaseGround2)
        self.staircaseFirst1.set_exit('east', self.corridorFirst)
        self.corridorFirst.set_exit('east', self.changeRoom)
        self.corridorFirst.set_exit('west', self.staircaseFirst1)
        self.corridorFirst.set_exit('south', self.adminOffice)
        self.adminOffice.set_exit('north', self.corridorFirst)
        self.adminOffice.set_exit('east', self.medicalRoom)
        self.changeRoom.set_exit('west', self.corridorFirst)
        self.changeRoom.set_exit('south', self.medicalRoom)
        self.medicalRoom.set_exit('north', self.changeRoom)
        self.medicalRoom.set_exit('west', self.adminOffice)
        self.medicalRoom.set_exit('south', self.staircaseFirst2)
        self.staircaseFirst2.set_exit('north', self.medicalRoom)
        self.staircaseFirst2.set_exit('upstairs', self.staircaseRoof)

        # Roof level
        self.staircaseRoof.set_exit('downstairs', self.staircaseFirst2)
        self.staircaseRoof.set_exit('north', self.openRoof)
        self.openRoof.set_exit('north', self.maintenanceRoom)
        self.openRoof.set_exit('south', self.staircaseRoof)
        self.openRoof.set_exit('west', self.helipad)
        self.maintenanceRoom.set_exit('south', self.openRoof)
        self.helipad.set_exit('east', self.openRoof)

    #  Creating the player
    def create_player(self, tempVar):
        """
        Creates the player
        :return:
        """
        #  player decided based on male and female choice by user
        if tempVar == "male":
            self.player = Player("Darryl", 60)
        elif tempVar == "female":
            self.player = Player("Carol", 50)

    def print_welcome(self):
        """
        Return the welcome message as a string.
        :return: welcome message string
        """
        self.msg = \
            f"*******Welcome to the new world {self.player.username}**********\n\
        You wake up to a post apocalyptic world. Zombies have taken over.\n\
        It's a miracle that you're still alive. You are humanity's last hope.\n\
        The military scientists created a zombie virus while developing super soldiers.\n\
        The key to an antidote to the virus is a human experiment in the Containment area.\n\
        Safely deliver the child to the Area-51 lab to save the world.\n\
        You best chance to reach there is a helicopter at the roof.\n\n\
        HURRY {self.player.username}...!! The world is running out of time. Tick Tock..!!\n\n\
        {self.current_room.get_long_description()}."
        return self.msg

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['Help', 'Go', 'Pick Items', 'Drop Items', 'View Items', 'Quit Game']

    def print_help(self):
        """
            Display some useful help text.
        :return: message
        """
        msg = f"You are in a military lab where the virus was created.\n\
        The antidote of the virus is a child in the containment area.\n\
        Safely deliver the child to the Area-51 lab to save the world.\n\
        Go get the child..and be careful the place is crawling of the dead walkers..!\n\n\
        {self.current_room.get_long_description()}."
        return msg

    def do_go_command(self, second_word):
        """
            Performs the GO command.
        :param secondWord: the direction the player wishes to travel in
        :return: text output
        """
        if second_word is None:
            # Missing second word...
            return 'Go where?', self.story()[1]
        next_room = self.current_room.get_exit(second_word)
        if next_room is None:
            return 'There is no door!', self.story()[1]
        else:
            try:
                # Checking if next room is locked
                if next_room.isLocked:
                    self.next_room_locked = next_room
                    story = f"Door is locked..! Click on door to try keys..!", self.story()[1]
                else:
                    self.current_room = next_room
                    story = self.story()
            except:
                print("That should not have happened..!!")
            return story

    def story(self):
        """
        This function builds up the whole storyline for the user and suggests user the next tasks that they may need
        to perform to win the game. Also returns the location of the player depending on which room the player is in.
        :return: story lines and player position on screen in pixels
        """
        item_desc = [item.description for item in self.player.inventory]
        if self.current_room.roomName == "experimentLab":
            pos = (200, 250)
            lines = f"You're back from where you started. Are you lost. Remember the world is running out of time.\n" \
                    f"HURRY UP!! {self.player.username}...!! Tick Tock..!!\n"
        elif self.current_room.roomName == "containmentArea":
            pos = (200, 100)
            if "Protective clothes" not in item_desc:
                self.player.health -= 10
                lines = f"There is a lot of radiation in the Containment lab..!!\n\n" \
                        f"Find some protective clothing or you may die soon.\n\n" \
                        f"Hurry...!! You health is declining..!!\n\n" \
                        f"Current Health: {self.player.health}"
            else:
                if "The Baby: Last hope of humanity." not in item_desc:
                    lines = f"Great you've got the protective clothing..!!\n\n" \
                            f"It's time to look for the child.\n\n" \
                            f"Find the child and take it to safety..!! Hurry now...!\n\n" \
                            f"Don't make too much noise.. There might be zombies in the lobby area...!!\n\n" \
                            f"It may be a good idea to look for some weapons..!!"
                else:
                    lines = f"Take the child to safety..!! Hurry now...!\n\n" \
                            f"Don't make too much noise.. There might be zombies in the lobby area...!!\n\n" \
                            f"It may be a good idea to look for some weapons..!!"
        elif self.current_room.roomName == "lobbyBasement":
            pos = (600, 100)
            if "The Baby: Last hope of humanity." not in item_desc:
                lines = f"It looks like you left the baby.\n\n" \
                        f"Go back and get the baby."
            else:
                lines = f"The walls are splattered with blood.\n\n" \
                        f"The foul stench has taken over the whole {self.current_room.description}.\n\n" \
                        f"Get out of the {self.current_room.description} before the baby starts crying."
        elif self.current_room.roomName == "staircaseBasement":
            pos = (810, 185)
            lines = f"Go to the ground floor..!!\n\n" \
                    f"Be careful there is some noise..!!\n\n\n" \
                    f"Arrrrrgh....!!!....Arrrrrgh....!!!!"
        elif self.current_room.roomName == "staircaseGround1":
            pos = (820, 190)
            lines = f"Blood is flowing through the crevice between the door and the floor..\n\n" \
                    f"Noise is getting louder...Danger is nigh..!!"
        elif self.current_room.roomName == "corridorGround":
            pos = (720, 190)
            if "Sharp surgery knife" not in item_desc and self.zombie1alive:
                lines = f"OH NO....There is a zombie in the corridor..!!\n" \
                        f"You don't have appropriate weapons...You're doomed to die..!!\n" \
                        f"Next time be prepared\n\n" \
                        f"***GAME OVER***\n" \
                        f"This Window will now close in 5 seconds..5..4..3..2..1"
            else:
                if self.zombie1alive:
                    self.player.health -= 10
                    lines = f"OH NO....There is a zombie in the corridor..!!\n" \
                            f"Use knife in inventory to kill zombie..\n\n" \
                            f"Command: Use Knife" \
                            f"\n\nCurrent Health: {self.player.health}"
                else:
                    lines = "It's too quiet here..!! Something is amiss..!! Get Moving now..!!"
        elif self.current_room.roomName == "securityRoom":
            pos = (650, 110)
            lines = f"Someone tried to make a last stand in this room...!! Alas..!! No one has survived the monsters..!!\n"\
                    f"There are a lots of supplies here...You may have a chance now..!!\n" \
                    f"Gather some weapons for any potential threats..!!"
            self.next_room_locked = self.adminOffice
        elif self.current_room.roomName == "cateringHall":
            pos = (450, 300)
            lines = f"You find yourself in a big dark room with blood splattered all over the ground and the ceilings.\n" \
                    f"Who knows what in the hell happened here? No one survived the disaster.\n" \
                    f"Only one way to find the answers... you need to go to the area 51 lab... you need to find a way...\n" \
                    f"Hurry up now...!!"
        elif self.current_room.roomName == "lobbyGround":
            pos = (180, 120)
            lines = f"Danger is lurking in the shadows try to keep in the light...!!\n" \
                    f"Find the fastest way to the roof and be careful..!!"
        elif self.current_room.roomName == "staircaseGround2":
            pos = (40, 30)
            lines = f"Suddenly it's too quite...Only sound you can hear is your heart pounding...tired, heavy breaths...\n" \
                    f"This is eerie... seems like the quite before a storm. Be careful...!!"
        elif self.current_room.roomName == "staircaseFirst1":
            pos = (30, 40)
            lines = f"Check your equipments..Make sure you have everything you need..!!\n" \
                    f"Just one more level to cross  now...!! Don't lose hope.!!"
        elif self.current_room.roomName == "corridorFirst":
            pos = (270, 30)
            lines = f"Do you hear someone screaming from the Changing room...!!\n" \
                    f"Are there any survivors..!!\n" \
                    f"You have to check...but wait...!! What if that a trap..!!\n" \
                    f"A huge dilemma..What would you do?"
        elif self.current_room.roomName == "changeRoom":
            pos = (600, 40)
            lines = f"After walking for 2 minutes you encounter the source of the noise..!!\n" \
                    f"As you try to go closer you realise you made a HUGE MISTAKE..!!\n" \
                    f"You just unlocked a room full of zombies..Someone must have lured them in and locked them up.!!\n" \
                    f"how dumb can you be...this is gonna cost you your life..!! As you try to run away\n" \
                    f"you slip in a pool of blood and the zombies had a nice breakfast..Few hours later you rise as a zombie.!!\n\n" \
                    f"***GAME OVER***\n" \
                    f"This Window will now close in 5 seconds..5..4..3..2..1"
        elif self.current_room.roomName == "adminOffice":
            pos = (150, 220)
            if "Glock Pistol." not in item_desc and self.zombie2alive:
                lines = f"OH NO....There is a zombie in the office..!!\n" \
                        f"You don't have appropriate weapons...You're doomed to die..!!\n" \
                        f"Next time be prepared\n\n" \
                        f"***GAME OVER***\n" \
                        f"This Window will now close in 5 seconds..5..4..3..2..1"
            else:
                if self.zombie2alive:
                    self.player.health -= 10
                    lines = f"This floor is filled with the dead-walkers.. take each step carefully..!!\n" \
                            f"The long dark hallways make things even worse..Stay focused...You have to...\n" \
                            f"The admin office is an important room.. you may find the helicopter keys here..!!\n"\
                            f"OH NO....There is a zombie in the office..!!\n" \
                            f"Use the handgun to kill zombie..\n\n" \
                            f"Command: Use Gun" \
                            f"\n\nCurrent Health: {self.player.health}"
                else:
                    lines = f"This floor is filled with the dead-walkers.. take each step carefully..!!\n" \
                            f"The long dark hallways make things even worse..Stay focused...You have to...\n" \
                            f"The admin office is an important room.. you may find the helicopter keys here..!!"
        elif self.current_room.roomName == "medicalRoom":
            pos = (590, 210)
            lines = f"Looks like someone was trying to cut-off their arm to get rid of the infection...\n" \
                    f"Can't say that is was successful by the looks of it..!!\n" \
                    f"You need to keep moving....!!! Don't forget your aim...SAVE THE HUMANITY...!!"
                    # f"Grab those med-kits, it can help you recover your health..!!"
        elif self.current_room.roomName == "staircaseFirst2":
            pos = (790, 310)
            lines = f"THUD***THUD***THUD***THUD-----\n" \
                    f"What is that banging noise??...\n" \
                    f"There is someone on the Roof...Is it a human trying to get away....OR is it a Zombie waiting for it's next target !!"
        elif self.current_room.roomName == "staircaseRoof":
            pos = (790, 300)
            lines = f"Whatever happens....!! No Matter what...!!\n" \
                    f"Don't let the baby get hurt...It is the last beacon of hope for humanity...\n" \
                    f"Protect it at any cost..!!\n" \
                    f"Be careful...This may be your final stand-off...!!"
        elif self.current_room.roomName == "openRoof":
            pos = (550, 220)
            if "The Baby: Last hope of humanity." not in item_desc:
                lines = f"You can not leave the Baby behind.. It is the cure..!!\n" \
                        f"How can you be so careless..!!\n" \
                        f"Go back and get the baby from the containment area..!!"
            else:
                lines = f"Be careful..!! There is a huge Zombie on the helipad..!\n" \
                        f"Make sure you have an automatic gun to kill it..!!"
        elif self.current_room.roomName == "maintenanceRoom":
            pos = (740, 50)
            lines = f"Quit wasting time..!! Go to the helipad and get out of this hell hole..!!\n" \
                    f"HURRY UP!!"
        elif self.current_room.roomName == "helipad":
            pos = (330, 200)
            if "Burst Fire - AR15 rifle." not in item_desc and self.zombieMainalive:
                lines = f"OH NO....I tried to warn you about the big zombie..!!\n" \
                        f"Are you going to fight the zombie by hand..!!\n" \
                        f"Next time take a gun...an automatic one..This zombie seems to be on steroids..!!\n" \
                        f"You're doomed to die..!!\n" \
                        f"****GAME OVER****"
            else:
                if self.zombieMainalive:
                    self.player.health -= 10
                    lines = f"OH NO....There is a zombie on the helipad..!!\n" \
                            f"This zombie seems to be on steroids..!!\n" \
                            f"Use the automatic gun to kill the dead-walker now...!!!\n\n" \
                            f"\n\nCurrent Health: {self.player.health}"
                else:
                    lines = f"Well done Mate..!!\n" \
                            f"Go now, take away the baby to safety..!!\n\n"
        return lines + f"\n\n{self.current_room.get_long_description()}", pos



