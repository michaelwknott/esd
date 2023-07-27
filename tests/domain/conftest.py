import pytest
from domain.athlete import FitnessProfile
from domain.prescribe import (
    calculate_rest_interval_distances,
    calculate_work_interval_distances,
)
from domain.session import Workout


@pytest.fixture
def athlete_one():
    return FitnessProfile(
        name="John Smith",
        time_trial_distance=2000,
        sprint_distance=5,
        time_trial_time=480,
        sprint_time=0.6,
    )
    # mas = 4.17
    # mss = 8.33
    # asr = 4.16


@pytest.fixture
def athlete_missing_mas():
    return FitnessProfile(
        name="Anne Other",
        time_trial_distance=2000,
        sprint_distance=5,
        time_trial_time=0,
        sprint_time=0.9,
    )


@pytest.fixture
def athlete_missing_mss():
    return FitnessProfile(
        name="Sam Jones",
        time_trial_distance=2000,
        sprint_distance=5,
        time_trial_time=420,
        sprint_time=0,
    )
    # mas = 4.76


@pytest.fixture
def workout():
    return Workout(
        workout_type="Passive Long Intervals - Normal",
        work_interval_time=3,
        work_interval_percentage_mas=1.0,
        work_interval_percentage_asr=None,
        rest_interval_time=3,
        rest_interval_percentage_mas=0,
        rest_interval_percentage_asr=None,
    )


@pytest.fixture
def fitness_profiles(athlete_one, athlete_missing_mas, athlete_missing_mss):
    return [athlete_one, athlete_missing_mas, athlete_missing_mss]


@pytest.fixture
def mas_work_distances(workout, fitness_profiles):
    return calculate_work_interval_distances(workout, fitness_profiles)


@pytest.fixture
def mas_rest_distances(workout, fitness_profiles):
    return calculate_rest_interval_distances(workout, fitness_profiles)
