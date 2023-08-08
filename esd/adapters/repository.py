from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class AbstractRepository(ABC, Generic[T]):
    """Interface for persistence layer."""

    @abstractmethod
    def get(self, id: str) -> T:
        """Get a single entity from the persistence layer."""
        raise NotImplementedError("Persistence layer needs to implement a get method.")

    @abstractmethod
    def get_all(self) -> list[T]:
        """Get a sequence of entities from the persistence layer."""
        raise NotImplementedError(
            "Persistence layer needs to implement a get_all method."
        )
