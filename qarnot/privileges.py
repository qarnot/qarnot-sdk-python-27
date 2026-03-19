"""Privileges that can be granted by user to tasks and pools"""


class Privileges(object):
    """Represents task privileges."""

    _exportApiAndStorageCredentialsInEnvironment = False  # Export the Api and Storage credentials to the task/pool environment

    def __init__(self, exportCredentialsInEnv=False):
        """Create a new :class:`~qarnot.privileges.Privileges`.

        :param bool exportCredentialsInEnv: if the task should export its api and storage credentials to its environment. Default is False."""
        self._exportApiAndStorageCredentialsInEnvironment = exportCredentialsInEnv

    @classmethod
    def from_json(cls, json):
        """Create the privileges from json.

        :param dict json: Dictionary representing the privileges
        :returns: The created :class:`~qarnot.privileges.Privileges`
        """
        shouldExportCredentialsInEnvironment = json.get("exportApiAndStorageCredentialsInEnvironment")
        return Privileges(shouldExportCredentialsInEnvironment)

    def to_json(self):
        """Get a dict ready to be json packed.

        :return: the json elements of the class.
        :rtype: `dict`
        """
        return {
            "exportApiAndStorageCredentialsInEnvironment": self._exportApiAndStorageCredentialsInEnvironment
        }

    def __eq__(self, other):
        if other is None:
            return False
        return self._exportApiAndStorageCredentialsInEnvironment == other._exportApiAndStorageCredentialsInEnvironment

    def __str__(self):
        return "privileges: exportCredentialsInEnvironnement {}.".format(self._exportApiAndStorageCredentialsInEnvironment)

    def __repr__(self):
        return "privileges.Privileges(exportCredentialsInEnv: {})".format(self._exportApiAndStorageCredentialsInEnvironment)
