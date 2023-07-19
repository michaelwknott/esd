from abc import ABC, abstractmethod
from collections.abc import Sequence
from enum import Enum

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
        raise NotImplementedError("Persistence layer needs to implement an add method.")
