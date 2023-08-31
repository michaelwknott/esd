from esd.adapters.repository import AbstractRepository
from esd.domain.profile import FitnessProfile
from esd.domain.session import Workout


class FakeFitnessProfileRepository(AbstractRepository[FitnessProfile]):
    """Fake implementation of FitnessProfile repository."""

    def __init__(self, fitness_profiles: dict[str, FitnessProfile]):
        """Initialise FakeFitnessProfileRepository with fitness profiles."""
        self._fitness_profiles = fitness_profiles

    def get(self, id: str) -> FitnessProfile:
        """Get a single entity from the persistence layer."""
        return self._fitness_profiles[id]

    def get_all(self) -> list[FitnessProfile]:
        """Get all entities from the persistence layer."""
        return list(self._fitness_profiles.values())


class FakeWorkoutRepository(AbstractRepository[Workout]):
    """Fake implementation of Workout repository."""

    def __init__(self, workouts: dict[str, Workout]):
        """Initialise FakeWorkoutRepository with workouts."""
        self._workouts = workouts

    def get(self, id: str) -> Workout:
        """Get a single entity from the persistence layer."""
        return self._workouts[id]

    def get_all(self) -> list[Workout]:
        """Get all entities from the persistence layer."""
        return list(self._workouts.values())
