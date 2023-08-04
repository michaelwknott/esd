from esd.adapters.repository import AbstractRepository
from esd.domain.athlete import FitnessProfile
from esd.domain.session import Workout


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

    def get_workouts(self) -> list[Workout]:
        """Get all workouts from the repository.

        Returns:
            A list of workouts.
        """
        return self.workout_repository.get_all()

    def get_fitness_profiles(self) -> list[FitnessProfile]:
        """Get all fitness profiles from the repository.

        Returns:
            A list of fitness profiles.
        """
        return self.fitness_profile_repository.get_all()

    def calculate_work_interval_distances(
        self, workout: Workout, fitness_profiles: list[FitnessProfile]
    ) -> dict[str, float]:
        """Calculate work interval distances for each athlete.

        Args:
            workout: The training variables for the workout.
            fitness_profiles: The fitness profile for each athlete completing the
                workout.

        Returns:
            A dictionary of athlete names mapped to work interval distances.
        """
        work_distances = {}
        for profile in fitness_profiles:
            work_interval_mas = (
                profile.max_aerobic_speed * workout.work_interval_percentage_mas
            )
            work_interval_distance = round(
                work_interval_mas * workout.work_interval_time, 0
            )
            work_distances[profile.name] = work_interval_distance
        return work_distances

    def calculate_rest_interval_distances(
        self, workout: Workout, fitness_profiles: list[FitnessProfile]
    ) -> dict[str, float]:
        """Calculate rest interval distances for each athlete.

        Args:
            workout: The training variables for the workout.
            fitness_profiles: The fitness profile for each athlete completing the
                workout.

        Returns:
            A dictionary of athlete names mapped to rest interval distances.
        """
        rest_distances = {}
        for profile in fitness_profiles:
            rest_interval_mas = (
                profile.max_aerobic_speed * workout.rest_interval_percentage_mas
            )
            rest_interval_distance = round(
                rest_interval_mas * workout.rest_interval_time, 0
            )
            rest_distances[profile.name] = rest_interval_distance
        return rest_distances