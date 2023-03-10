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


![ClassDiagram](https://user-images.githubusercontent.com/46666736/211586517-3a30a7d9-628e-4930-aa8c-1ab34e11a3cb.png)

