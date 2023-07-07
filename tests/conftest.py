import pytest

from esd.athlete import FitnessProfile


@pytest.fixture
def athlete_one():
    return FitnessProfile("John Smith", 480, 0.6)
    # mas = 4.17
    # mss = 8.33
    # asr = 4.16


@pytest.fixture
def athlete_missing_mas():
    return FitnessProfile("Anne Other", 0, 0.9)


@pytest.fixture
def athlete_missing_mss():
    return FitnessProfile("Sam Jones", 420, 0)
