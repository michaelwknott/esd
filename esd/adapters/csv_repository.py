import csv
from collections import defaultdict
from pathlib import Path

from esd.domain.profile import FitnessProfile
from esd.domain.session import Workout

from .repository import AbstractRepository, RepositoryError


class CsvFitnessProfileRepository(AbstractRepository[FitnessProfile]):
    """CSV implementation of FitnessProfile repository."""

    def __init__(self, filepath: str):
        """Initialise CsvRepository with fitness profiles.

        Args:
            filepath: The filepath for the fitness assessment CSV files.
        """
        self._filepath = Path(filepath)
        self._fitness_profiles: dict[str, FitnessProfile] = {}
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
                latest_2km: list = max(
                    result
                    for result in athlete_results
                    if result[4] == "2km time trial"
                )
                latest_5m: list = max(
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

                self._fitness_profiles[athlete_name] = profile

    def get(self, id: str) -> FitnessProfile:
        """Get a single entity from the persistence layer."""
        return self._fitness_profiles[id]

    def get_all(self) -> list[FitnessProfile]:
        """Get a sequence of entities from the persistence layer."""
        return list(self._fitness_profiles.values())

    def add(self, entity: FitnessProfile) -> None:
        """Add an entity to the persistence layer."""
        if entity.name in self._fitness_profiles:
            raise RepositoryError(
                f"FitnessProfile with name {entity.name} already exists."
            )
        else:
            self._fitness_profiles[entity.name] = entity

    def update(self, entity: FitnessProfile) -> None:
        """Update an entity in the persistence layer."""
        try:
            self._fitness_profiles[entity.name] = entity
        except KeyError as e:
            raise RepositoryError(f"No FitnessProfile with name {entity.name}.") from e

    def delete(self, entity: FitnessProfile) -> None:
        """Delete an entity from the persistence layer."""
        try:
            del self._fitness_profiles[entity.name]
        except KeyError as e:
            raise RepositoryError(f"No FitnessProfile with name {entity.name}.") from e


class CsvWorkoutRepository(AbstractRepository[Workout]):
    """CSV implementation of Workout repository."""

    def __init__(self, filepath: str):
        """Initialise CsvRepository with workouts.

        Args:
            filepath: The filepath for the workouts CSV file.
        """
        self._file_path = Path(filepath)
        self._workouts: dict[str, Workout] = {}
        self._load()

    def _convert_types(self, record: list[str]) -> list:
        types = [str, int, float, float, int, float, float]
        return [func(val) for func, val in zip(types, record)]

    def _load(self):
        with open(self._file_path) as f:
            reader = csv.reader(f)
            next(reader)  # skip header row

            for record in reader:
                converted = self._convert_types(record)
                workout = Workout(*converted)
                self._workouts[workout.name] = workout

    def get(self, id: str) -> Workout:
        """Get a single entity from the persistence layer."""
        return self._workouts[id]

    def get_all(self) -> list[Workout]:
        """Get a sequence of entities from the persistence layer."""
        return list(self._workouts.values())

    def add(self, entity: Workout) -> None:
        """Add an entity to the persistence layer."""
        if entity.name in self._workouts:
            raise RepositoryError(f"Workout with name {entity.name} already exists.")
        else:
            self._workouts[entity.name] = entity

    def update(self, entity: Workout) -> None:
        """Update an entity in the persistence layer."""
        try:
            self._workouts[entity.name] = entity
        except KeyError as e:
            raise RepositoryError(f"No Workout with name {entity.name}.") from e

    def delete(self, entity: Workout) -> None:
        """Delete an entity from the persistence layer."""
        try:
            del self._workouts[entity.name]
        except KeyError as e:
            raise RepositoryError(f"No Workout with name {entity.name}.") from e
