import unittest
from Game import Game

class testGame(unittest.TestCase):
    """
    This is a unit test class which tests the basic functionalities of the game such as movement through the free space,
    and other such fundamental tasks.
     :param- None
     :return - None
    """
    def setUp(self):
        self.game = Game()

    def tearUp(self):
        del self.game

    def test_player(self):
        self.game.create_player("male")
        self.assertEqual("Darryl", self.game.player.username)
        self.assertEqual(60, self.game.player.weightCapacity)
        returnVal = self.game.player.pickItems(self.game.knife1)
        self.assertTrue(returnVal)
        checkKnife = "Sharp surgery knife" in self.game.player.viewItems()
        self.assertTrue(checkKnife)
        returnVal = self.game.player.dropItems(self.game.knife1)
        self.assertTrue(returnVal)
        checkKnife = "Sharp surgery knife" in self.game.player.viewItems()
        self.assertFalse(checkKnife)
        returnVal = self.game.player.dropItems(self.game.knife1)
        self.assertFalse(returnVal)

    def test_game(self):
        """
                Tests movement of player in free space
                :param: None
                :return: None
                """
        self.game.create_player("male")
        self.assertEqual('Go where?', self.game.do_go_command(None)[0])
        self.assertEqual("experimentLab", self.game.current_room.roomName)
        self.game.do_go_command('north')
        self.assertEqual("containmentArea", self.game.current_room.roomName)
        self.assertEqual(90, self.game.player.health)
        self.game.do_go_command('east')
        self.assertEqual("lobbyBasement", self.game.current_room.roomName)
        self.game.do_go_command('east')
        self.assertEqual("staircaseBasement", self.game.current_room.roomName)
        self.game.do_go_command('north')
        self.assertEqual("staircaseBasement", self.game.current_room.roomName)
        self.game.do_go_command('upstairs')
        self.assertEqual("staircaseGround1", self.game.current_room.roomName)
        self.game.do_go_command('west')
        self.assertEqual("corridorGround", self.game.current_room.roomName)
        self.game.do_go_command('north')
        self.assertEqual("corridorGround", self.game.current_room.roomName)
        self.game.do_go_command('west')
        self.game.do_go_command('west')
        self.game.do_go_command('upstairs')
        self.game.do_go_command('east')
        self.assertEqual("corridorFirst", self.game.current_room.roomName)
        self.assertTrue(self.game.securityRoom.isLocked)
        self.assertTrue(self.game.adminOffice.isLocked)

    def test_inventory(self):
        for i in range(10):
            self.assertTrue(self.game.burstgun.shoot()[0])

        self.assertFalse(self.game.burstgun.shoot()[0])

        self.assertTrue(self.game.keysToSecRoom.unlock_door(self.game.securityRoom))
        self.assertFalse(self.game.keysToSecRoom.unlock_door(self.game.adminOffice))

        self.assertTrue(10, self.game.knife1.weight)
        self.assertTrue(self.game.helicopter.isLocked)

    def test_room(self):
        self.assertEqual(2, len(self.game.lobbyBasement.get_exits()))
        self.game.lobbyBasement.add_item(self.game.knife1)
        for i in self.game.lobbyBasement.itemsInRoom:
            if i == self.game.knife1:
                check = True
                break
        self.assertTrue(check)
        self.game.lobbyBasement.remove_item(self.game.knife1)
        check = False
        for i in self.game.lobbyBasement.itemsInRoom:
            if i == self.game.knife1:
                check = True
                break
        self.assertFalse(check)