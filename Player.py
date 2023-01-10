"""
This is the Player class which defines the Players states (attributes) and behaviour (Actions).

> Player method
1. PickItems
2. dropItems

> Player attributes
1. Username: automatically allocated based on user choice
2. weightCapacity: amount of weight the character can carry
"""
class Player:
    """
    Class to instantiate the player.
    :param: username: name of player
    :param: weightCapacity: weight carrying capacity
    :return: True- if the player was able to pick up/drop an object, false otherwise
    """
    def __init__(self, username, weightCapacity):
        self.health = 100
        self.username = username
        self.weightCapacity = weightCapacity
        self.inventory = []
        self.itemNetWeight = 0

    def viewItems(self):
        if len(self.inventory) == 0:
            lines = f"!!..Inventory Empty..!!\n"
        else:
            lines = f"Available items:\n\n" \
                    f"{[item.description for item in self.inventory]}"
        return lines

    def pickItems(self, item):
        """
        function to pick items
        :param item: item to pick
        :return: true if picked false otherwise
        """
        try:
            if self.itemNetWeight < self.weightCapacity:
                if item.__class__.__name__ == "Bag":
                    self.weightCapacity += item.capacity
                self.itemNetWeight += item.weight
                self.inventory.append(item)
                return True
            else:
                return False  # print("!!..Max Load exceeded..!!")
        except NameError as msg:
            print(msg)
        except:
            print("That should not have happened...!!")

    def dropItems(self, item):
        """
        function to drop items
        :param item: item to drop
        :return: None
        """
        try:
            if self.itemNetWeight > 0:
                if item.__class__.__name__ == "Bag":
                    self.weightCapacity -= item.capacity
                self.itemNetWeight -= item.weight
                self.inventory.remove(item)
                return True
            else:
                return False  # print("!!..Inventory Empty..!!")
        except NameError as msg:
            print(msg)
        except:
            print("That should not have happened...!!")









