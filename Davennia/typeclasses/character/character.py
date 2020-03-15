from Davennia.typeclasses.characters import Character
from evennia.utils import ansi

class ColorableCharacter(Character):
    def at_object_creation(self):
        # set a color config value
        # self.db.config_color = True
        super().at_object_creation()
        pass

