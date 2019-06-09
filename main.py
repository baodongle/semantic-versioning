#!/usr/bin/env python3
"""Semantic Versioning"""
from __future__ import annotations

from functools import total_ordering
from logging import exception
from typing import Any, Optional, Sequence, Tuple

# Type annotation for Tuple of Semantic Versioning:
VersionTuple = Tuple[int, int, int]


# Waypoint 1:
def convert_string_to_version_component_numbers(string: str) \
        -> Optional[Sequence[int]]:
    """
    Convert a Semantic Versioning Component Number String to a Tuple.

    Parameters
    ----------
    string : str
        A semantic versioning 3-component number (at least 1).

    Returns
    -------
    Sequence[int]
        A tuple composed of 3 integers (major, minor, patch).

    """

    def _get_valid_version(number: str) -> int:
        """Get positive version from the number string."""
        version = int(number)
        if version >= 0:
            return version
        raise ValueError("Each number version must be positive!")

    try:
        component = list(map(_get_valid_version, string.strip().split('.')))
        return tuple(component[:3] + [0 for _ in range(3 - len(component))])
    except ValueError as e:
        exception(f'Invalid input: {string}\n' + str(e))
        return None


# Waypoint 2:
def compare_versions(this: VersionTuple, other: VersionTuple) -> int:
    """
    Compare Versions.

    Parameters
    ----------
    this : VersionTuple
    other : VersionTuple
        Both tuples composed of 3 integers (major, minor, patch) each.

    Returns
    -------
        1 if this is above other;
        0 if this equals other;
        -1 if this is below other.

    """
    return -1 if this < other else 0 if this == other else 1


# Waypoint 3:
@total_ordering
class Version:
    """
    Class that hold a semantic versioning 3-component number.

    Attributes
    ----------
    major : int
        The major version.
    minor : int
        The minor version.
    patch : int
        The patch version.
    component : VersionTuple
        A tuple composed of 3 integers (major, minor, patch).

    """

    def __init__(self, major: Any, minor: int = 0, patch: int = 0) -> None:
        self.major = 0
        self.minor = 0
        self.patch = 0
        if all(isinstance(x, int) for x in (major, minor, patch)):
            self.major = major
            self.minor = minor
            self.patch = patch
        elif isinstance(major, str):
            self.major, self.minor, self.patch = \
                convert_string_to_version_component_numbers(major)
        elif isinstance(major, tuple):
            self.major, self.minor, self.patch = \
                tuple(list(major)[:3] + [0 for _ in range(3 - len(major))])
        self.component = (self.major, self.minor, self.patch)

    # Waypoint 4:
    def __repr__(self) -> str:
        """Compute "Official" String Representations."""
        return f'Version({self.major}, {self.minor}, {self.patch})'

    # Waypoint 5:
    def __str__(self) -> str:
        """Compute "Informal" String Representation."""
        return f'{self.major}.{self.minor}.{self.patch}'

    # Waypoint 6: Compare `Version` Instances
    def __lt__(self, other: Version) -> bool:
        return compare_versions(self.component, other.component) == -1

    def __eq__(self, other: Version) -> bool:
        return not compare_versions(self.component, other.component)


if __name__ == '__main__':
    # print(repr(Version("1.2.8")))
    # print(Version(1, 7, 0))
    print(Version("1.2.8") > Version("2.4.5"))
    print(Version("2.4.5") > Version("1.2.8"))
    print(Version("1.2.8") < Version("2.4.5"))
    print(Version("2.4.5") < Version("1.2.8"))
    print(Version("2.4.5") == Version("1.2.8"))
    print(Version("2.4.5") == Version("2.4.5"))
    print(Version("2.4.5") != Version("2.4.5"))
    print(Version("2.4.5") != Version("1.2.8"))
    print(Version("2.4.5") >= Version("2.4.5"))
    print(Version("2.4.5") >= Version("1.2.8"))
    print(Version("2.4.5") <= Version("2.4.5"))
    print(Version("2.4.5") <= Version("1.2.8"))
