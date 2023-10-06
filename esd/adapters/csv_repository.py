import csv
from collections import defaultdict
from dataclasses import fields
from pathlib import Path

from esd.domain.profile import FitnessProfile
from esd.domain.workout import Workout

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

    def _load(self):
        with open(self._file_path, newline="") as f:
            reader = csv.DictReader(f)
            for record in reader:
                workout = Workout.from_dict(record)
                self._workouts[workout.name] = workout

    def _save(self):
        """Save workouts to CSV file."""
        with open(self._file_path, "w", newline="") as f:
            fieldnames = [field.name for field in fields(Workout)]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for workout in self._workouts.values():
                writer.writerow(workout.to_dict())

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
        self._workouts[entity.name] = entity
        self._save()

    def update(self, entity: Workout) -> None:
        """Update an entity in the persistence layer."""
        try:
            self._workouts[entity.name] = entity
            self._save()
        except KeyError as e:
            raise RepositoryError(f"No Workout with name {entity.name}.") from e

    def delete(self, entity: Workout) -> None:
        """Delete an entity from the persistence layer."""
        try:
            del self._workouts[entity.name]
            self._save()
        except KeyError as e:
            raise RepositoryError(f"No Workout with name {entity.name}.") from e
