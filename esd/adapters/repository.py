from abc import ABC, abstractmethod
from typing import Generic, TypeVar


class RepositoryError(Exception):
    """Base class for exceptions in this module."""

    pass


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

    @abstractmethod
    def add(self, entity: T) -> None:
        """Add an entity to the persistence layer."""
        raise NotImplementedError("Persistence layer needs to implement an add method.")

    @abstractmethod
    def update(self, entity: T) -> None:
        """Update an entity in the persistence layer."""
        raise NotImplementedError(
            "Persistence layer needs to implement an update method."
        )

    @abstractmethod
    def delete(self, entity: T) -> None:
        """Delete an entity from the persistence layer."""
        raise NotImplementedError(
            "Persistence layer needs to implement a delete method."
        )
