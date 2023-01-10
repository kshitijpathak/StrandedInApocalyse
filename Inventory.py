"""
This class will hold information about the players inventory.
Following is the list of items and the description:
1. Item: The parent class for some items

Other class names are self-explanatory with the following attributes:
weight, description, capacity (bag) etc.
"""


class Item:
    """
    An abstract class used to create other object
    :param: weight, description
    :return: None
    """

    def __init__(self, weight, description):
        self.weight = weight
        self.description = description


class Bag(Item):
    """
    Class to instantiate bag object. Bag increases weight carrying capacity of the player
    :param: capacity: the weight capacity of the bag
    :param: weight: bag's weight
    :param: description
    :return: None
    """
    def __init__(self, capacity, weight, description):
        super().__init__(weight, description)
        self.itemNos = 0
        self.capacity = capacity
        self.weight = weight
        self.itemList = []


class Gun(Item):
    """
        Used to instantiate gun objects within the game. Parent class of automatic gun class
        :param: remainingBullets: number of bullets remaining in the gun
        :param: magSize: magazine size of the gun
        :param: weight: gun weight
        :param: description
        :return: the remaining bullets after reloading
        """
    def __init__(self, remainingBullets, magSize, weight, description):
        super().__init__(weight, description)
        self.remainingBullets = remainingBullets if remainingBullets <= magSize else magSize
        self.magSize = magSize

    def shoot(self):
        """
        function to shoot gun. Reduces bullet number by one
        :return: True if bullet available False otherwise
        """
        try:
            if self.remainingBullets > 0:
                self.remainingBullets -= 1
                return True, '!!!....B A N G....!!!'
            else:
                return False, 'No bullets. Please reload.'
        except:
            print("That should not have happened..!!")

    def reload(self, bullets):
        """
        function to reload a gun
        :param bullets:
        :return: number bullets reloaded
        """
        try:
            if self.remainingBullets < self.magSize:
                self.remainingBullets = min(self.magSize, self.remainingBullets + bullets.count)
                # Returning remaining bullet counts
                if bullets.count > (self.magSize - self.remainingBullets):
                    return bullets.count - (self.magSize - self.remainingBullets), "!!..Ready for Battle..!!"
                else:
                    return 0, "Reloaded..Use bullets wisely..you're out of bullets..!!"
            else:
                return False, "Magazine at capacity."
        except:
            print("That should not have happened..!!")


class Bullets(Item):
    """
    Used to instantiate Bullets objects within the game.
        :param: count: number of bullets
        :param: weight: bullet's weight
        :param: description
        :return: the remaining bullets after reloading
    """
    def __init__(self, count, weight, description):
        super().__init__(weight, description)
        self.count = count

    def updateCount(self, newCount):
        self.count = newCount


class AutomaticGun(Gun):
    """
        Used to instantiate gun objects within the game.
        :param: remainingBullets: number of bullets remaining in the gun
        :param: magSize: magazine size of the gun
        :param: weight: gun weight
        :param: description
        """

    def __init__(self, remainingBullets, magSize, weight, description):
        super().__init__(remainingBullets, magSize, weight, description)
        self.remainingBullets = remainingBullets if remainingBullets <= magSize else magSize

    def shoot(self):
        """
        function to shoot gun. Reduces bullet number by one
        :return: True if bullet available False otherwise
        """
        try:
            if self.remainingBullets > 2:
                self.remainingBullets -= 3
                return True, '!!!....*** B A N G B O O M ***....!!!'
            else:
                return False, 'No bullets. Please reload.'
        except:
            print("That should not have happened..!!")


class Keys(Item):
    """
    Class to instantiate the keys to open doors etc.
    :param: keyOpens: the room's description which the key opens
    :param: weight: key's weight
    :param: description
    :return: True if unlocking is successful
    """

    def __init__(self, weight, description, keyOpens):
        super().__init__(weight, description)
        self.keyOpens = keyOpens

    def unlock_door(self, place):
        """
        function to unlock the door
        :param room, helicopter:
        :return: True if opened, false otherwise
        """
        try:
            if place.description == self.keyOpens:
                place.isLocked = False
                return True
            else:
                return False
        except AttributeError as msg:
            print(msg)


class Clothes(Item):
    """
    Class to instantiate clothes
    :param: weight, description
    :return: None
    """

    def __init__(self, weight, description):
        super().__init__(weight, description)


class Helicopter:
    """
    Class to instantiate helicopter
    :param: description, isLocked
    :return: None
    """

    def __init__(self, description, isLocked=True):
        self.isLocked = isLocked
        self.description = description

    def fly(self):
        """
        function to fly helicopter. Final function. If run the user wins game.
        :return:
        """
        if not self.isLocked:
            text = f"Chop..Chop..Chop..Chop..Chop..Chop..Chop..Chop..Chop..Chop..Chop..!!!\n" \
                   f"****** YAY YOU WON..!! You might just save the world..!!"
            return text
        else:
            return "Can not fly before unlocking..!!"


class Baby(Item):
    """
    Class to instantiate the baby
    :param: weight, description
    :return: None
    """
    def __init__(self, weight, description):
        super().__init__(weight, description)


class Knife(Item):
    """
    Class to instantiate knife object.
    :param: weight, description
    :return: None
    """

    def __init__(self, weight, description):
        super().__init__(weight, description)

    def cut(self):
        """
        function allows to use knife
        :return: text
        """
        return "S L A S H..!! **---** S L A S H..!!"
