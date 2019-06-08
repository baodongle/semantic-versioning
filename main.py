#!/usr/bin/env python3
"""Semantic Versioning"""
from logging import exception
from typing import Optional, Sequence, Tuple


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
    try:
        component = list(map(int, string.strip().split('.')))
        return tuple(component[:3] + [0 for _ in range(3 - len(component))])
    except ValueError as e:
        exception('Invalid input!\n' + str(e))
        return None


# Waypoint 2:
def compare_versions(this: Tuple[int, int, int], other: Tuple[int, int, int]) \
        -> int:
    """
    Compare Versions.

    Parameters
    ----------
    this : Tuple[str, str, str]
    other : Tuple[str, str, str]
        Both tuples composed of 3 integers (major, minor, patch) each.

    Returns
    -------
        1 if this is above other;
        0 if this equals other;
        -1 if this is below other.

    """
    return -1 if this < other else 0 if this == other else 1


# Waypoint 3:
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

    """

    def __init__(self, major, minor=0, patch=0):
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
    def __repr__(self):
        """Compute "Official" String Representations."""
        return f'Version({self.major}, {self.minor}, {self.patch})'

    # Waypoint 5:
    def __str__(self):
        """Compute "Informal" String Representation."""
        return f'{self.major}.{self.minor}.{self.patch}'

    # Waypoint 6: Compare `Version` Instances
    def __lt__(self, other):
        return compare_versions(self.component, other.component) == -1

    def __le__(self, other):
        return not self > other

    def __eq__(self, other):
        return compare_versions(self.component, other.component) == 0

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return compare_versions(self.component, other.component) == 1

    def __ge__(self, other):
        return not self < other


if __name__ == '__main__':
    print(repr(Version("1.2.8")))
    print(Version(1, 7, 0))
