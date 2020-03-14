"""
General Command Set

These are commands that are available to all players and are either new or edited versions
of the existing ones.

"""

from evennia import default_cmds
from Davennia.commands.account.option import CmdOption

class AccountCommandSet(default_cmds.CharacterCmdSet):
    """
    The `GeneralCmdSet` contains general in-game commands like `look`,
    `get`, etc available on in-game Character objects. It is merged with
    the `AccountCmdSet` when an Account puppets a Character.
    """
    key = "GeneralCharacter"

    def at_cmdset_creation(self):
        """
        Populate command set
        """
        self.add(CmdOption())