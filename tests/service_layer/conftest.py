import pytest

from esd.adapters.in_memory_repository import (
    InMemoryFitnessProfileRepository,
    InMemoryWorkoutRepository,
)
from esd.domain.profile import FitnessProfile
from esd.domain.workout import Workout
from esd.service_layer.service import WorkoutService, FitnessProfileService


@pytest.fixture
def workout_one():
    return Workout(
        workout_type="Passive Long Intervals - Normal",
        work_interval_time=3,
        work_interval_percentage_mas=1.0,
        work_interval_percentage_asr=0.0,
        rest_interval_time=3,
        rest_interval_percentage_mas=0.0,
        rest_interval_percentage_asr=0.0,
    )


@pytest.fixture
def workout_two():
    return Workout(
        workout_type="Passive Long Intervals - Extensive",
        work_interval_time=2,
        work_interval_percentage_mas=1.0,
        work_interval_percentage_asr=0.0,
        rest_interval_time=1,
        rest_interval_percentage_mas=0.0,
        rest_interval_percentage_asr=0.0,
    )


@pytest.fixture
def workout_three():
    return Workout(
        workout_type="Passive Long Intervals - Intensive",
        work_interval_time=2,
        work_interval_percentage_mas=1.0,
        work_interval_percentage_asr=0.0,
        rest_interval_time=1,
        rest_interval_percentage_mas=0.0,
        rest_interval_percentage_asr=0.0,
    )


@pytest.fixture
def in_mem_workout_repository(workout_one, workout_two, workout_three):
    """Return a InMemoryWorkoutRepository."""
    workouts = {
        "Passive Long Intervals - Normal: 3 mins work / 3 mins rest": workout_one,
        "Passive Long Intervals - Extensive: 2 mins work / 1 mins rest": workout_two,
        "Passive Long Intervals - Intensive: 2 mins work / 1 mins rest": workout_three,
    }
    return InMemoryWorkoutRepository(workouts)


@pytest.fixture
def profile_one():
    return FitnessProfile(
        name="John Smith",
        time_trial_distance=2000,
        sprint_distance=5,
        time_trial_time=480,
        sprint_time=0.6,
    )


# profile_one mas = 2000 / 480 = 4.17


@pytest.fixture
def profile_two():
    return FitnessProfile(
        name="Jane Doe",
        time_trial_distance=2000,
        sprint_distance=5,
        time_trial_time=470,
        sprint_time=0.5,
    )


# profile_two mas = 2000 / 470 = 4.26


@pytest.fixture
def profile_three():
    return FitnessProfile(
        name="Joe Bloggs",
        time_trial_distance=2000,
        sprint_distance=5,
        time_trial_time=500,
        sprint_time=0.4,
    )


# profile_three mas = 2000 / 500 = 4.00


@pytest.fixture  #
def profiles(profile_one, profile_two, profile_three):
    return [profile_one, profile_two, profile_three]


@pytest.fixture
def in_mem_fitness_profile_repository(profile_one, profile_two, profile_three):
    """Return a InMemoryFitnessProfileRepository."""
    fitness_profiles = {
        "John Smith": profile_one,
        "Jane Doe": profile_two,
        "Joe Bloggs": profile_three,
    }
    return InMemoryFitnessProfileRepository(fitness_profiles)


@pytest.fixture
def workout_service(in_mem_workout_repository):
    """Return a WorkoutService."""
    return WorkoutService(in_mem_workout_repository)


@pytest.fixture
def fitness_profile_service(in_mem_fitness_profile_repository):
    """Return a FitnessProfileService."""
    return FitnessProfileService(in_mem_fitness_profile_repository)
