# Stranded In Apocalyse
## 1.	Problem Statement
The python program is a basic UI-based game that allows the user to interact with the game environment to play an adventure space game. An adventure space game is a game where the character can roam around freely and complete designated tasks to win the game. The following paragraphs describe the game scenario and capabilities.
### 1.1 Game scenario
This game is set in a post-apocalyptic world. The player who was in hibernation wakes up in a world that has been taken over by zombies. The player is situated in a lab where the virus was born. This is a military experiment facility that was being used to experiment on humans to produce super soldiers. The player was also part of the experiments. As he/she was kept in an experimental isolation pod, they survived the outbreak. However, as he is awake, he is responsible for saving the world. Some pre-recorded messages by scientists mention the antidote. The antidote is within an experiment child which is in the same laboratory complex. As the lab building is destroyed the player must take the child, the antidote, to another lab on the outskirts of the city so that the scientists can cure the disease.

### 1.2 Capabilities
The player can move around 20 rooms set in the lab complex though they must be careful of any zombie encounters. Different rooms have different objects that can help the player to proceed further in the game. For example, guns/knives can help to kill zombies, and keys to different rooms containing important objects for progressing in the game.
The final objective of the game is to reach on top of the roof and kill the mega-zombie to finally escape using the helicopter placed on the rooftop. But to reach the rooftop the player must go through the rooms filled with zombies. The player should also be careful not to leave the baby behind.


## 2.	Class Diagram
Please refer to the below image to view the class diagram relationships for the application. The same is also placed in the zip directory. Some major relationships are mentioned below:

1.	Main model script is Game.py, which interacts with the following modules:
   a.	App.py: this module controls the user interface of the game application
   b.	Room.py: this module is responsible for creating the rooms for the game model. Other functionalities include setting exits of the rooms etc.
   c.	Player.py: used to instantiate the player object
   d.	Inventory.py: contains various objects needed throughout the game
2.	App.py, interacts with image_objects.py which helps in importing the images being used in the game
 



## 3.	Class Description
This section describes the changes and enhancements to the existing classes and any other new classes constructed to convert the game from a simple text-based game to a UI-based game.

### 3.1 Changes to existing classes

1.	TextUI.py: this script is removed altogether from the game application as the game is converted from a text-based to a UI-based interface
2.	Room.py - Room class: 
   a.	Added an attribute to get the name of the room to facilitate identification of the rooms elsewhere in the code e.g. while placing items in the room
   b.	Added two methods namely, add_item and remove_item, to add and remove items from a particular room
   c.	Removed unlock_door method
3.	Player.py – Player class: added a method named; viewItems to show the items being held by the character
4.	Inventory.py:
   a.	Bag class: removed methods pickItems and dropItems, moved these to player class instead
   b.	Keys class: modified the key class
5.	Game.py – Game class:
   a.	Modified create_player class to take input from the user interface and create player accordingly
   b.	Removed play method which created the game loop in text-UI game
   c.	Print_welcome, print_help methods now return the messages instead of printing to the console using textUI method. The returned message is used further to display       in the UI
   d.	Removed show_command_words method
   e.	Added some error handling to do_go_command method
   f.	Method process_command moved to main app script as the input is now received as button clicks and not text inputs
   g.	Removed inventory_options method and created an equivalent function in the main app script
   h.	Story method now returns the storylines instead of printing them on the console via TextUI class. The story method also returns the player’s position on the           frame depending on the room where the character is located in. This was added here to avoid duplication of large if else ladder.
