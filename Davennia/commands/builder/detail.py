# for the @detail command we inherit from MuxCommand, since
# we want to make use of MuxCommand's pre-parsing of '=' in the
# argument.
class CmdTutorialSetDetail(default_cmds.MuxCommand):
    """
    sets a detail on a room

    Usage:
        @detail <key> = <description>
        @detail <key>;<alias>;... = description

    Example:
        @detail walls = The walls are covered in ...
        @detail castle;ruin;tower = The distant ruin ...

    This sets a "detail" on the object this command is defined on
    (TutorialRoom for this tutorial). This detail can be accessed with
    the TutorialRoomLook command sitting on TutorialRoom objects (details
    are set as a simple dictionary on the room). This is a Builder command.

    We custom parse the key for the ;-separator in order to create
    multiple aliases to the detail all at once.
    """

    key = "@detail"
    locks = "cmd:perm(Builder)"
    help_category = "TutorialWorld"

    def func(self):
        """
        All this does is to check if the object has
        the set_detail method and uses it.
        """
        if not self.args or not self.rhs:
            self.caller.msg("Usage: @detail key = description")
            return
        if not hasattr(self.obj, "set_detail"):
            self.caller.msg("Details cannot be set on %s." % self.obj)
            return
        for key in self.lhs.split(";"):
            # loop over all aliases, if any (if not, this will just be
            # the one key to loop over)
            self.obj.set_detail(key, self.rhs)
        self.caller.msg("Detail set: '%s': '%s'" % (self.lhs, self.rhs))