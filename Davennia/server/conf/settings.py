r"""
Evennia settings file.

The available options are found in the default settings file found
here:

z:\mud\evennia\evennia\settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "Davennia"


######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")

######################################################################
# Customized command parser
######################################################################
# May need to set this in future:
#COMMAND_PARSER = "Davennia.commands.cmdparser.cmdparser"

# Single characters to ignore at the beginning of a command. When set, e.g.
# cmd, @cmd and +cmd will all find a command "cmd" or one named "@cmd" etc. If
# you have defined two different commands cmd and @cmd you can still enter
# @cmd to exactly target the second one. Single-character commands consisting
# of only a prefix character will not be stripped. Set to the empty
# string ("") to turn off prefix ignore.
# removed '@' from it
CMD_IGNORE_PREFIXES = "@&/+"

######################################################################
# Web character view 
######################################################################
INSTALLED_APPS += ('web.character',)