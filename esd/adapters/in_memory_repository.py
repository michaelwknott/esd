from esd.adapters.repository import AbstractRepository
from esd.domain.profile import FitnessProfile
from esd.domain.session import Workout


class InMemoryFitnessProfileRepository(AbstractRepository[FitnessProfile]):
    """In memory implementation of FitnessProfile repository."""

    def __init__(self, fitness_profiles: dict[str, FitnessProfile]):
        """Initialise InMemoryFitnessProfileRepository with fitness profiles."""
        self._fitness_profiles = fitness_profiles

    def get(self, id: str) -> FitnessProfile:
        """Get a single entity from the persistence layer."""
        return self._fitness_profiles[id]

    def get_all(self) -> list[FitnessProfile]:
        """Get all entities from the persistence layer."""
        return list(self._fitness_profiles.values())

    def add(self, entity: FitnessProfile) -> None:
        """Add an entity to the persistence layer."""
        self._fitness_profiles[entity.name] = entity

    def update(self, entity: FitnessProfile) -> None:
        """Update an entity in the persistence layer."""
        self._fitness_profiles[entity.name] = entity

    def delete(self, entity: FitnessProfile) -> None:
        """Delete an entity from the persistence layer."""
        del self._fitness_profiles[entity.name]


class InMemoryWorkoutRepository(AbstractRepository[Workout]):
    """In memory implementation of Workout repository."""

    def __init__(self, workouts: dict[str, Workout]):
        """Initialise InMemoryWorkoutRepository with workouts."""
        self._workouts = workouts

    def get(self, id: str) -> Workout:
        """Get a single entity from the persistence layer."""
        return self._workouts[id]

    def get_all(self) -> list[Workout]:
        """Get all entities from the persistence layer."""
        return list(self._workouts.values())

    def add(self, entity: Workout) -> None:
        """Add an entity to the persistence layer."""
        self._workouts[entity.name] = entity

    def update(self, entity: Workout) -> None:
        """Update an entity in the persistence layer."""
        self._workouts[entity.name] = entity

    def delete(self, entity: Workout) -> None:
        """Delete an entity from the persistence layer."""
        del self._workouts[entity.name]
