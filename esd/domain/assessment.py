from collections.abc import Mapping
from dataclasses import dataclass
from typing import Self


@dataclass
class Assessment:
    """Represents an assessment result.

    Attributes:
        athlete_name: A str of the athlete's name.
        date: A str of the date of the assessment.
        type: A str of the type of assessment.
        distance: An int of the assessment distance in meters.
        time: A float of the time taken to complete the assessment.
    """

    athlete_name: str
    date: str
    type: str
    distance: int
    time: float

    @classmethod
    def from_dict(cls, d: Mapping) -> Self:
        """Create Assessment instance from dictionary.

        Args:
            d: A mapping of Assessment dataclass fields to values

        Returns:
            Self: An instance of the Assessment class
        """
        return cls(**d)
