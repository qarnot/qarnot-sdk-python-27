class ForcedConstantAccess(object):
    ReadWrite = "readWrite"
    ReadOnly = "readOnly"


class ForcedConstant(object):
    """Forced Constant Information

    .. note:: For internal usage only
    """

    def __init__(self, forced_value, force_export_in_environment=None, access=None):
        self.forced_value = forced_value
        """:type: :class:`str`

        Forced value for the constant."""

        self.force_export_in_environment = force_export_in_environment
        """:type: :class:`bool`

        Whether the constant should be forced in the execution environment or not."""

        self.access = access
        """:type: :class:`~qarnot.forced_constant.ForcedConstantAccess`

        The access level of the constant: ReadOnly or ReadWrite."""

    def to_json(self, name):
        result = {
            "constantName": name,
            "forcedValue": self.forced_value,
        }

        if self.force_export_in_environment is not None:
            result["forceExportInEnvironment"] = self.force_export_in_environment

        if self.access is not None:
            result["access"] = self.access

        return result
