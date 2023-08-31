from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Self


@dataclass
class Athlete:
    """Represents an athlete and their identifying information."""

    forename: str
    surname: str
    name: str = field(init=False)
    date_of_birth: str
    sport: str

    def __post_init__(self) -> None:  # noqa: D105
        self.name = f"{self.forename} {self.surname}"

    @classmethod
    def from_dict(cls, mapping: Mapping) -> Self:
        """Create Athlete instance from dictionary.

        Args:
            mapping: A mapping of Athlete dataclass fields to values

        Returns:
            Self: An instance of the Athlete class
        """
        return cls(**mapping)
