"""
# @teleceport, from evennia commands.default.building
"""

from evennia.commands.default.building import CmdTeleport

class CmdTeleport(CmdTeleport):
    """
    teleport object to another location

    Usage:
      tel/switch [<object> to||=] <target location>

    Examples:
      tel Limbo
      tel/quiet box = Limbo
      tel/tonone box

    Switches:
      quiet  - don't echo leave/arrive messages to the source/target
               locations for the move.
      intoexit - if target is an exit, teleport INTO
                 the exit object instead of to its destination
      tonone - if set, teleport the object to a None-location. If this
               switch is set, <target location> is ignored.
               Note that the only way to retrieve
               an object from a None location is by direct #dbref
               reference. A puppeted object cannot be moved to None.
      loc - teleport object to the target's location instead of its contents

    Teleports an object somewhere. If no object is given, you yourself are
    teleported to the target location.
    """

    key = "tel"
    aliases = "teleport, goto"
    switch_options = ("quiet", "intoexit", "tonone", "loc")
    rhs_split = ("=", " to ")  # Prefer = delimiter, but allow " to " usage.
    locks = "cmd:perm(teleport) or perm(Builder)"
    help_category = "Building"

    def func(self):
        """Performs the teleport"""

        caller = self.caller
        args = self.args
        lhs, rhs = self.lhs, self.rhs
        switches = self.switches

        # setting switches
        tel_quietly = "quiet" in switches
        to_none = "tonone" in switches
        to_loc = "loc" in switches

        if to_none:
            # teleporting to None
            if not args:
                obj_to_teleport = caller
            else:
                obj_to_teleport = caller.search(lhs, global_search=True)
                if not obj_to_teleport:
                    caller.msg("Did not find object to teleport.")
                    return
            if obj_to_teleport.has_account:
                caller.msg(
                    "Cannot teleport a puppeted object "
                    "(%s, puppeted by %s) to a None-location."
                    % (obj_to_teleport.key, obj_to_teleport.account)
                )
                return
            caller.msg("Teleported %s -> None-location." % obj_to_teleport)
            if obj_to_teleport.location and not tel_quietly:
                obj_to_teleport.location.msg_contents(
                    "%s teleported %s into nothingness." % (caller, obj_to_teleport), exclude=caller
                )
            obj_to_teleport.location = None
            return

        # not teleporting to None location
        if not args and not to_none:
            caller.msg("Usage: teleport[/switches] [<obj> =] <target_loc>||home")
            return

        if rhs:
            obj_to_teleport = caller.search(lhs, global_search=True)
            destination = caller.search(rhs, global_search=True)
        else:
            obj_to_teleport = caller
            destination = caller.search(lhs, global_search=True)
        if not obj_to_teleport:
            caller.msg("Did not find object to teleport.")
            return

        if not destination:
            caller.msg("Destination not found.")
            return
        if to_loc:
            destination = destination.location
            if not destination:
                caller.msg("Destination has no location.")
                return
        if obj_to_teleport == destination:
            caller.msg("You can't teleport an object inside of itself!")
            return
        if obj_to_teleport == destination.location:
            caller.msg("You can't teleport an object inside something it holds!")
            return
        if obj_to_teleport.location and obj_to_teleport.location == destination:
            caller.msg("%s is already at %s." % (obj_to_teleport, destination))
            return
        use_destination = True
        if "intoexit" in self.switches:
            use_destination = False

        # try the teleport
        if obj_to_teleport.move_to(
            destination, quiet=tel_quietly, emit_to_obj=caller, use_destination=use_destination
        ):
            if obj_to_teleport == caller:
                caller.msg("Teleported to %s." % destination)
            else:
                caller.msg("Teleported %s -> %s." % (obj_to_teleport, destination))
