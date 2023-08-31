import pytest

from esd.domain.profile import FitnessProfile
from esd.domain.session import Workout


@pytest.fixture
def profile_one():
    return FitnessProfile(
        name="John Smith",
        time_trial_distance=2000,
        sprint_distance=5,
        time_trial_time=480,
        sprint_time=0.6,
    )


@pytest.fixture
def profile_missing_mas():
    return FitnessProfile(
        name="Anne Other",
        time_trial_distance=2000,
        sprint_distance=5,
        time_trial_time=0,
        sprint_time=0.9,
    )


@pytest.fixture
def profile_missing_mss():
    return FitnessProfile(
        name="Sam Jones",
        time_trial_distance=2000,
        sprint_distance=5,
        time_trial_time=420,
        sprint_time=0,
    )


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
def fitness_profiles(profile_one, profile_missing_mas, profile_missing_mss):
    return [profile_one, profile_missing_mas, profile_missing_mss]
