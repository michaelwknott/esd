import csv
from abc import ABC, abstractmethod
from collections.abc import Sequence
from enum import Enum
from pathlib import Path

from .athlete import FitnessProfile
from .session import Workout


class EntityType(Enum):
    """Represent the type of entity to be retrieved from persistence layer."""

    FITNESS_PROFILE = "fitness_profile"
    WORKOUT = "workout"


class AbstractRepository(ABC):
    """Interface for persistence layer."""

    @abstractmethod
    def get(self, id: str, entity_type: EntityType) -> FitnessProfile | Workout:
        """Get a single entity from the persistence layer."""
        raise NotImplementedError("Persistence layer needs to implement a get method.")

    @abstractmethod
    def get_all(self, entity_type: EntityType) -> Sequence[FitnessProfile | Workout]:
        """Get a sequence of entities from the persistence layer."""
        raise NotImplementedError("Persistence layer needs to implement a list method.")

    @abstractmethod
    def add(self, entity_type: EntityType, entity: FitnessProfile | Workout) -> None:
        """Add a single entity record to persistence layer."""
        raise NotImplementedError("Persistence layer needs to implement an add method")


class CsvRepository(AbstractRepository):
    """CSV implementation of repository."""

    def __init__(self, folder: str):
        """Initialise CsvRepository with fitness profiles and workouts.

        Args:
            folder: The directory path for the folder containing the CSV files.
        """
        self._fitness_profiles_path = Path(folder) / "fitness_assessments.csv"
        self._workouts_path = Path(folder) / "conditioning_workouts.csv"
        self._fitness_profiles: list[FitnessProfile] = []
        self._workouts: list[Workout] = []
        self._load()

    def _load(self):
        with open("data/fitness_assessments3.csv") as f:
            reader = csv.reader(f)
            next(reader)  # skip header row
            sorted_records = sorted(reader, key=lambda record: record[0])

        print(sorted_records)
        results = self.group_results_by_name(sorted_records)
        print(results)

    def get(self, id: str, entity_type: EntityType) -> FitnessProfile | Workout:
        """Get a single entity from the persistence layer."""
        pass

    def get_all(self, entity_type: EntityType) -> Sequence[FitnessProfile | Workout]:
        """Get a sequence of entities from the persistence layer."""
        pass

    def add(self, entity_type: EntityType, entity: FitnessProfile | Workout) -> None:
        """Add a single entity record to persistence layer."""
        pass

        # rows = list(rows)
        #         latest_2km = max(
        #             (Workout(*row) for row in rows if row[1] == "2km"),
        #             default=None,
        #             key=attrgetter("date"),
        #         )
        #         latest_5m = max(
        #             (Workout(*row) for row in rows if row[1] == "5m"),
        #             default=None,
        #             key=attrgetter("date"),
        #         )
        #         profile = FitnessProfile(athlete_id, latest_2km, latest_5m)
        #         self._fitness_profiles.append(profile)

        # with open(f"{self._workouts_path}") as f:
        #     reader = csv.reader(f)
        #     next(reader)  # skip header row
        #     for row in reader:
        #         self._workouts.append(Workout(*row))


if __name__ == "__main__":
    repo = CsvRepository("data")
