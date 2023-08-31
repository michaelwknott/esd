import csv

import pytest

from esd.adapters.csv_repository import (
    CsvFitnessProfileRepository,
    CsvWorkoutRepository,
)
from esd.domain.profile import FitnessProfile
from esd.domain.session import Workout


@pytest.fixture
def fitness_assessment_csv_filepath(tmp_path):
    filepath = tmp_path / "fitness_assessments.csv"
    with open(filepath, "w") as f:
        writer = csv.writer(f)
        headers = [
            "athlete_name",
            "sport",
            "status",
            "date",
            "time_trial_name",
            "time_trial_distance",
            "time_trial_time",
        ]
        fitness_assessment_results = [
            [
                "John Doe",
                "Boxing",
                "True",
                "2022/05/12",
                "2km time trial",
                "2000",
                "510",
            ],
            [
                "John Doe",
                "Boxing",
                "True",
                "2022/05/13",
                "5m flying sprint",
                "5",
                "0.67",
            ],
            [
                "John Doe",
                "Boxing",
                "True",
                "2022/04/09",
                "2km time trial",
                "2000",
                "520",
            ],
            [
                "John Doe",
                "Boxing",
                "True",
                "2022/04/10",
                "5m flying sprint",
                "5",
                "0.70",
            ],
            [
                "Jane Smith",
                "Boxing",
                "True",
                "2022/05/12",
                "2km time trial",
                "2000",
                "460",
            ],
            [
                "Jane Smith",
                "Boxing",
                "True",
                "2022/05/13",
                "5m flying sprint",
                "5",
                "0.52",
            ],
        ]
        writer.writerow(headers)
        writer.writerows(fitness_assessment_results)
        return filepath


@pytest.fixture
def fitness_profile_repo(fitness_assessment_csv_filepath):
    repo = CsvFitnessProfileRepository(filepath=fitness_assessment_csv_filepath)
    yield repo
    repo._fitness_profiles.clear()


@pytest.fixture
def john_doe_profile():
    return FitnessProfile("John Doe", 2000, 5, 510, 0.67)


@pytest.fixture
def jane_smith_profile():
    return FitnessProfile("Jane Smith", 2000, 5, 460, 0.52)


@pytest.fixture
def workouts_csv_filepath(tmp_path):
    filepath = tmp_path / "conditioning_workouts.csv"
    with open(filepath, "w") as f:
        writer = csv.writer(f)
        headers = [
            "workout_name",
            "workout_interval_time",
            "workout_interval_percentage_mas",
            "work_interval_percentage_asr",
            "rest_interval_time",
            "rest_interval_percentage_mas",
            "rest_interval_percentage_asr",
        ]
        workouts = [
            ["Passive Long Intervals - Normal", 2, 100, 0, 2, 0, 0],
            ["Passive Long Intervals - Extensive", 2, 100, 0, 1, 0, 0],
            ["Passive Long Intervals - Intensive", 2, 100, 0, 3, 0, 0],
        ]
        writer.writerow(headers)
        writer.writerows(workouts)
        return filepath


@pytest.fixture
def workout_profile_repo(workouts_csv_filepath):
    repo = CsvWorkoutRepository(filepath=workouts_csv_filepath)
    yield repo
    repo._workouts.clear()


@pytest.fixture
def workout_one():
    return Workout("Passive Long Intervals - Normal", 2, 100, 0, 2, 0, 0)


@pytest.fixture
def workout_two():
    return Workout("Passive Long Intervals - Extensive", 2, 100, 0, 1, 0, 0)


@pytest.fixture
def workout_three():
    return Workout("Passive Long Intervals - Intensive", 2, 100, 0, 3, 0, 0)
