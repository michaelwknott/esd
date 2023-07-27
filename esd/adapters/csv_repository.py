import csv
from collections import defaultdict
from collections.abc import Sequence
from pathlib import Path

from domain.athlete import FitnessProfile
from domain.session import Workout
from repository import AbstractRepository


class CsvFitnessProfileRepository(AbstractRepository[FitnessProfile]):
    """CSV implementation of FitnessProfile repository."""

    def __init__(self, folder: str):
        """Initialise CsvRepository with fitness profiles.

        Args:
            folder: The directory path for the folder containing the CSV files.
        """
        self._filepath = Path(folder) / "fitness_assessments.csv"
        self._fitness_profiles: list[FitnessProfile] = []
        self._load()

    def _load(self):
        with open(self._filepath) as f:
            reader = csv.reader(f)
            next(reader)  # skip header row

            # group reader by name
            athlete_records = defaultdict(list)
            for record in reader:
                athlete_records[record[0]].append(record)

            # find latest 2km and 5m for each athlete
            for athlete_name, athlete_results in athlete_records.items():
                latest_2km = max(
                    result
                    for result in athlete_results
                    if result[4] == "2km time trial"
                )
                latest_5m = max(
                    result
                    for result in athlete_results
                    if result[4] == "5m flying sprint"
                )

                # create FitnessProfile for each athlete
                profile = FitnessProfile(
                    name=athlete_name,
                    time_trial_distance=int(latest_2km[5]),
                    sprint_distance=int(latest_5m[5]),
                    time_trial_time=int(latest_2km[6]),
                    sprint_time=float(latest_5m[6]),
                )

                self._fitness_profiles.append(profile)

    def get(self, id: str) -> FitnessProfile:
        """Get a single entity from the persistence layer."""
        pass

    def get_all(self) -> Sequence[FitnessProfile]:
        """Get a sequence of entities from the persistence layer."""
        pass

    def add(self, entity: FitnessProfile) -> None:
        """Add a single entity record to persistence layer."""
        pass


class CsvWorkoutRepository(AbstractRepository[Workout]):
    """CSV implementation of  Workout repository."""

    def __init__(self, folder: str):
        """Initialise CsvRepository with workouts.

        Args:
            folder: The directory path for the folder containing the CSV files.
        """
        self._file_path = Path(folder) / "conditioning_workouts.csv"
        self._workouts: list[Workout] = []
        self._load()

    def _load(self):
        with open(self._file_path) as f:
            reader = csv.reader(f)
            next(reader)  # skip header row

    def get(self, id: str) -> Workout:
        """Get a single entity from the persistence layer."""
        pass

    def get_all(self) -> Sequence[Workout]:
        """Get a sequence of entities from the persistence layer."""
        pass

    def add(self, entity: Workout) -> None:
        """Add a single entity record to persistence layer."""
        pass


if __name__ == "__main__":
    repo = CsvFitnessProfileRepository("data")
