from esd.adapters.repository import AbstractRepository
from esd.domain.profile import FitnessProfile
from esd.domain.session import Workout
from esd.domain.prescribe import (
    calculate_work_interval_distances,
    calculate_rest_interval_distances,
)


class WorkoutService:
    """Service class for workout related operations."""

    def __init__(
        self,
        workout_repository: AbstractRepository[Workout],
        fitness_profile_repository: AbstractRepository[FitnessProfile],
    ):
        """Initialise WorkoutService with repositories."""
        self.workout_repository = workout_repository
        self.fitness_profile_repository = fitness_profile_repository

    def get_selected_workout(self, selected_workout: str) -> Workout:
        """Get the selected workout from the repository.

        Args:
            selected_workout: The name of the selected workout.

        Returns:
            A workout.
        """
        return self.workout_repository.get(selected_workout)

    def get_workout_names(self) -> list[str]:
        """Get all workout names from the repository.

        Workout names are displayed to the user to select the required workout.

        Returns:
            A list of workout names.
        """
        workouts = self.workout_repository.get_all()

        return [workout.name for workout in workouts]

    def get_fitness_profiles(self) -> list[FitnessProfile]:
        """Get all fitness profiles from the repository.

        Returns:
            A list of fitness profiles.
        """
        return self.fitness_profile_repository.get_all()

    def calculate_interval_distances(
        self, workout: Workout, fitness_profiles: list[FitnessProfile]
    ) -> tuple[dict[str, float], dict[str, float]]:
        """Calculate work and rest interval distances for each athlete."""
        work_distances = calculate_work_interval_distances(workout, fitness_profiles)
        rest_distances = calculate_rest_interval_distances(workout, fitness_profiles)

        return work_distances, rest_distances
