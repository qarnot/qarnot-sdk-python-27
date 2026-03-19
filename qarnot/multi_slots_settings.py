"""Multi Slots Settings that can be used when creating a pool"""


class MultiSlotsSettings(object):
    """Represents task multi slots settings."""

    _slotsPerNode = None

    def __init__(self, slotsPerNode=None):
        """Create a new :class:`~qarnot.multi_slots_settings.MultiSlotsSettings`.

        :param slotsPerNode: slots per node
        :type slotsPerNode: int
        """
        self._slotsPerNode = slotsPerNode

    @classmethod
    def from_json(cls, json):
        """Create the multi slots settings from json.

        :param dict json: Dictionary representing the multi slots settings
        :returns: The created :class:`~qarnot.multi_slots_settings.MultiSlotsSettings`
        """
        slotsPerNode = json.get("slotsPerNode")
        return MultiSlotsSettings(slotsPerNode)

    def to_json(self):
        """Get a dict ready to be json packed.

        :return: the json elements of the class.
        :rtype: `dict`
        """
        return {
            "slotsPerNode": self._slotsPerNode
        }

    def __eq__(self, other):
        if other is None or not isinstance(other, MultiSlotsSettings):
            return False
        return self._slotsPerNode == other._slotsPerNode

    def __str__(self):
        return "multi slots settings: slotsPerNode {}.".format(self._slotsPerNode)

    def __repr__(self):
        return "multi_slots_settings.MultiSlotsSettings(slotsPerNode: {})".format(self._slotsPerNode)
