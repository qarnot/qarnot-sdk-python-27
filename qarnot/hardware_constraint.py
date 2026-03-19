"""Module to handle hardware constraints"""

# Copyright 2017 Qarnot computing
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc


class HardwareConstraint(object):
    """Represents a hardware constraint."""
    _discriminator = None

    @classmethod
    def from_json(cls, json):
        """Create an hardware constraint from json.

        :param qarnot.connection.Connection connection: the cluster connection
        :param dict json: Dictionary representing the constraint
        :returns: The created :class:`~qarnot.hardware_constraint.HardwareConstraint`.
        """

        discriminator = json.get("discriminator")
        if discriminator == MinimumCoreHardware._discriminator:
            minCoreCount = json.get("coreCount")
            return MinimumCoreHardware(minCoreCount)
        elif discriminator == MaximumCoreHardware._discriminator:
            maxCoreCount = json.get("coreCount")
            return MaximumCoreHardware(maxCoreCount)
        elif discriminator == MinimumRamCoreRatioHardware._discriminator:
            minimumMemoryGBCoreRatio = json.get("minimumMemoryGBCoreRatio")
            return MinimumRamCoreRatioHardware(minimumMemoryGBCoreRatio)
        elif discriminator == MaximumRamCoreRatioHardware._discriminator:
            maximumMemoryGBCoreRatio = json.get("maximumMemoryGBCoreRatio")
            return MaximumRamCoreRatioHardware(maximumMemoryGBCoreRatio)
        elif discriminator == MinimumRamHardware._discriminator:
            minimumMemoryMB = json.get("minimumMemoryMB")
            return MinimumRamHardware(minimumMemoryMB)
        elif discriminator == MaximumRamHardware._discriminator:
            maximumMemoryMB = json.get("maximumMemoryMB")
            return MaximumRamHardware(maximumMemoryMB)
        elif discriminator == SpecificHardware._discriminator:
            specificationKey = json.get("specificationKey")
            return SpecificHardware(specificationKey)
        elif discriminator == GpuHardware._discriminator:
            return GpuHardware()
        elif discriminator == NoGpuHardware._discriminator:
            return NoGpuHardware()
        elif discriminator == NoSSDHardware._discriminator:
            return NoSSDHardware()
        elif discriminator == SSDHardware._discriminator:
            return SSDHardware()
        elif discriminator == CpuModelHardware._discriminator:
            cpu_model = json.get("cpuModel")
            return CpuModelHardware(cpu_model)
        else:
            return None

    @abc.abstractmethod
    def to_json(self):
        """Get a dict ready to be json packed.

        :raises NotImplementedError: this is an abstract method, it should be overridden in child classes
        """

    def __str__(self):
        return "hardware constraint {}.".format(self._discriminator)

    def __repr__(self):
        return str(self._discriminator)


class MinimumCoreHardware(HardwareConstraint):
    """Represents an hardware constraint to limit the minimum number of cores"""
    _discriminator = "MinimumCoreHardwareConstraint"

    def __init__(self, coreCount):
        """ Create a new hardware constraint to limit the minimum number of cores the hardware should have.

        :param str ram: the minimum number of cores the hardware should have"""
        self._core_count = coreCount

    def to_json(self):
        """Get a dict ready to be json packed.

        :return: the json elements of the class.
        :rtype: `dict`

        """
        return {
            "discriminator": self._discriminator,
            "coreCount": self._core_count
        }

    def __str__(self):
        return "Minimum core hardware constraint with a minimum of {} cores.".format(self._core_count)

    def __repr__(self):
        return "{}: {} cores".format(self._discriminator, self._core_count)


class MaximumCoreHardware(HardwareConstraint):
    """Represents an hardware constraint to limit the maximum number of cores"""
    _discriminator = "MaximumCoreHardwareConstraint"

    def __init__(self, coreCount):
        """ Create a new hardware constraint to limit the maximum number of cores the hardware should have.

        :param str ram: the maximum number of cores the hardware should have"""
        self._core_count = coreCount

    def to_json(self):
        """Get a dict ready to be json packed.

        :return: the json elements of the class.
        :rtype: `dict`

        """
        return {
            "discriminator": self._discriminator,
            "coreCount": self._core_count
        }

    def __str__(self):
        return "Maximum core hardware constraint with a maximum of {} cores.".format(self._core_count)

    def __repr__(self):
        return "{}: {} cores".format(self._discriminator, self._core_count)


class MinimumRamCoreRatioHardware(HardwareConstraint):
    """Represents an hardware constraint to limit the minimum memory core ratio"""
    _discriminator = "MinimumRamCoreRatioHardwareConstraint"

    def __init__(self, ram):
        """ Create a new hardware constraint to limit the minimum ram/core ratio the hardware should have.

        :param str ram: the minimum memory/core ratio the hardware should have (in GB/core)"""
        self._minimum_memory_gb_core_ratio = ram

    def to_json(self):
        """Get a dict ready to be json packed.

        :return: the json elements of the class.
        :rtype: `dict`

        """
        return {
            "discriminator": self._discriminator,
            "minimumMemoryGBCoreRatio": self._minimum_memory_gb_core_ratio
        }

    def __str__(self):
        return "Minimum Ram core ratio hardware constraint with a minimum of {} GB / core.".format(self._minimum_memory_gb_core_ratio)

    def __repr__(self):
        return "{}: {} GB/cores".format(self._discriminator, self._minimum_memory_gb_core_ratio)


class MaximumRamCoreRatioHardware(HardwareConstraint):
    """Represents an hardware constraint to limit the maximum memory core ratio"""
    _discriminator = "MaximumRamCoreRatioHardwareConstraint"

    def __init__(self, ram):
        """ Create a new hardware constraint to limit the maximum ram/core ratio the hardware should have.

        :param str ram: the maximum memory/core ratio the hardware should have (in GB/core)"""
        self._maximum_memory_gb_core_ratio = ram

    def to_json(self):
        """Get a dict ready to be json packed.

        :return: the json elements of the class.
        :rtype: `dict`

        """
        return {
            "discriminator": self._discriminator,
            "maximumMemoryGBCoreRatio": self._maximum_memory_gb_core_ratio
        }

    def __str__(self):
        return "Maximum Ram core ratio hardware constraint with a maximum of {} GB / core.".format(self._maximum_memory_gb_core_ratio)

    def __repr__(self):
        return "{}: {} GB/cores".format(self._discriminator, self._maximum_memory_gb_core_ratio)


class MinimumRamHardware(HardwareConstraint):
    """Represents an hardware constraint to limit the minimum memory"""
    _discriminator = "MinimumRamHardwareConstraint"

    def __init__(self, ram):
        """ Create a new hardware constraint to limit the minimum ram the hardware should have.

        :param str ram: the minimum memory the hardware should have (in MB)"""
        self._minimum_memory_mb = ram

    def to_json(self):
        """Get a dict ready to be json packed.

        :return: the json elements of the class.
        :rtype: `dict`

        """
        return {
            "discriminator": self._discriminator,
            "minimumMemoryMB": self._minimum_memory_mb
        }

    def __str__(self):
        return "Minimum Ram hardware constraint with a minimum of {}MB.".format(self._minimum_memory_mb)

    def __repr__(self):
        return "{}: {} MB".format(self._discriminator, self._minimum_memory_mb)


class MaximumRamHardware(HardwareConstraint):
    """Represents an hardware constraint to limit the maximum memory"""
    _discriminator = "MaximumRamHardwareConstraint"

    def __init__(self, ram):
        """ Create a new hardware constraint to limit the maximum ram the hardware should have.

        :param str ram: the maximum memory the hardware should have (in MB)"""
        self._maximum_memory_mb = ram

    def to_json(self):
        """Get a dict ready to be json packed.

        :return: the json elements of the class.
        :rtype: `dict`

        """
        return {
            "discriminator": self._discriminator,
            "maximumMemoryMB": self._maximum_memory_mb
        }

    def __str__(self):
        return "Maximum Ram hardware constraint with a maximum of {}MB.".format(self._maximum_memory_mb)

    def __repr__(self):
        return "{}: {} MB".format(self._discriminator, self._maximum_memory_mb)


class SpecificHardware(HardwareConstraint):
    """Represents an hardware constraint to limit to a specific hardware"""
    _discriminator = "SpecificHardwareConstraint"

    def __init__(self, key):
        """ Create a new hardware constraint for a specific hardware using its specification key.

        :param str key: the specification key of the hardware which should be used"""
        self._specification_key = key

    def to_json(self):
        """Get a dict ready to be json packed.

        :return: the json elements of the class.
        :rtype: `dict`

        """
        return {
            "discriminator": self._discriminator,
            "specificationKey": self._specification_key
        }

    def __str__(self):
        return "Specific hardware constraint with key: {}.".format(self._specification_key)

    def __repr__(self):
        return "{}: key {}".format(self._discriminator, self._specification_key)


class GpuHardware(HardwareConstraint):
    """Represents an hardware constraint to limit hardware with gpu"""
    _discriminator = "GpuHardwareConstraint"

    def to_json(self):
        """Get a dict ready to be json packed.

        :return: the json elements of the class.
        :rtype: `dict`

        """
        return {
            "discriminator": self._discriminator
        }

    def __str__(self):
        return "Hardware with graphic card."

    def __repr__(self):
        return self._discriminator


class SSDHardware(HardwareConstraint):
    """Represents an hardware constraint to limit hardware with SSD"""
    _discriminator = "SSDHardwareConstraint"

    def to_json(self):
        """Get a dict ready to be json packed.

        :return: the json elements of the class.
        :rtype: `dict`

        """
        return {
            "discriminator": self._discriminator
        }

    def __str__(self):
        return "Hardware with SSD storage."

    def __repr__(self):
        return self._discriminator


class NoSSDHardware(HardwareConstraint):
    """Represents an hardware constraint to limit hardware without SSD"""
    _discriminator = "NoSSDHardwareConstraint"

    def to_json(self):
        """Get a dict ready to be json packed.

        :return: the json elements of the class.
        :rtype: `dict`

        """
        return {
            "discriminator": self._discriminator
        }

    def __str__(self):
        return "Hardware without SSD storage."

    def __repr__(self):
        return self._discriminator


class NoGpuHardware(HardwareConstraint):
    """Represents an hardware constraint to limit hardware without gpu"""
    _discriminator = "NoGpuHardwareConstraint"

    def to_json(self):
        """Get a dict ready to be json packed.

        :return: the json elements of the class.
        :rtype: `dict`

        """
        return {
            "discriminator": self._discriminator
        }

    def __str__(self):
        return "Hardware without graphic card."

    def __repr__(self):
        return self._discriminator


class CpuModelHardware(HardwareConstraint):
    """Represents a hardware constraint to limit with a specific CPU"""
    _discriminator = "CpuModelHardwareConstraint"

    def __init__(self, cpu_model):
        """ Create a new hardware constraint for a specific cpu model.

        :param str cpu_model: the cpu model which should be used"""
        self._cpu_model = cpu_model

    def to_json(self):
        """Get a dict ready to be json packed.

        :return: the json elements of the class.
        :rtype: `dict`

        """
        return {
            "discriminator": self._discriminator,
            "cpuModel": self._cpu_model,
        }

    def __str__(self):
        return "Hardware with a {} CPU".format(self._cpu_model)

    def __repr__(self):
        return "{}: {} CPU".format(self._discriminator, self._cpu_model)
