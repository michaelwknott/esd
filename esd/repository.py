from abc import ABC, abstractmethod
from collections.abc import Sequence

from .athlete import FitnessProfile
from .session import Workout


class AbstractRepository(ABC):
    """Interface for persistence layer."""

    @abstractmethod
    def get_profile(self, id: str) -> FitnessProfile:
        """Get a single FitnessProfile from the persistence layer."""
        raise NotImplementedError(
            "Persistence layer needs to implement a get_profile method."
        )

    @abstractmethod
    def list_profiles(self) -> Sequence[FitnessProfile]:
        """Get a sequence of FitnessProfiles from the persistence layer."""
        raise NotImplementedError(
            "Persistence layer needs to implement a list_profiles method."
        )

    @abstractmethod
    def add_profile(self, profile: FitnessProfile) -> None:
        """Add a single FitnessProfile record to persistence layer."""
        raise NotImplementedError(
            "Persistence layer needs to implement a add_profile method"
        )

    @abstractmethod
    def add_profiles(self, profiles: Sequence[FitnessProfile]) -> None:
        """Add multiple FitnessProfiles to the persistence layer."""
        raise NotImplementedError(
            "Persistence layer needs to implement a add_profiles method"
        )

    @abstractmethod
    def get_workout(self, id: str) -> Workout:
        """Get a single Workout from the persistence layer."""
        raise NotImplementedError(
            "Persistence layer needs to implement a get_workout method"
        )

    @abstractmethod
    def list_workouts(self, id: str) -> Sequence[Workout]:
        """Get muliptle WOrkouts from the persistence layer."""
        raise NotImplementedError(
            "Persistence layer needs to implement a list_workouts method"
        )

    @abstractmethod
    def add_workout(self, workout: Workout) -> None:
        """Add a single Workout to the persistence layer."""
        raise NotImplementedError(
            "Persistence layer needs to implement a add_workout method"
        )

    @abstractmethod
    def add_workouts(self, workouts: Sequence[Workout]) -> None:
        """Add multiple Workouts to the persistence layer."""
        raise NotImplementedError(
            "Persistence layer needs to implement a add_workouts method"
        )
