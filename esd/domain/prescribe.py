from collections.abc import Collection

from .athlete import FitnessProfile
from .session import Workout


def calculate_work_interval_distances(
    workout: Workout, fitness_profiles: Collection[FitnessProfile]
) -> dict[str, float]:
    """Calculate work interval distances for each athlete.

    Args:
        workout: The training variables for the workout.
        fitness_profiles: The fitness profile for each athlete completing the workout.

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
    workout: Workout, fitness_profiles: Collection[FitnessProfile]
) -> dict[str, float]:
    """Calculate rest interval distances for each athlete.

    Args:
        workout: The training variables for the workout.
        fitness_profiles: The fitness profile for each athlete completing the workout.

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
