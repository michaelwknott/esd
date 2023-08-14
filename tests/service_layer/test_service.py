from datetime import datetime

import pytest


class TestWorkoutService:
    @pytest.mark.parametrize(
        "workout_name, expected_workout",
        [
            (
                "Passive Long Intervals - Normal: 3 mins work / 3 mins rest",
                "workout_one",
            ),
            (
                "Passive Long Intervals - Extensive: 2 mins work / 1 mins rest",
                "workout_two",
            ),
            (
                "Passive Long Intervals - Intensive: 2 mins work / 1 mins rest",
                "workout_three",
            ),
        ],
    )
    def test_get_workout(
        self, workout_service, workout_name, expected_workout, request
    ):
        """Test get_workout method."""
        name = workout_service.get_workout(workout_name)
        expected = request.getfixturevalue(expected_workout)
        assert name == expected

    def test_get_fitness_profiles(self, workout_service, profiles):
        """Test get_fitness_profile method."""
        fitness_profile = workout_service.get_fitness_profiles()
        assert fitness_profile == profiles

    def test_calculate_work_interval_distances(
        self, workout_service, profiles, workout_one
    ):
        """Test calculate_work_interval_distances method."""
        work_distances = workout_service.calculate_work_interval_distances(
            workout_one, profiles
        )
        expected_work_distances = {
            "John Smith": 751,
            "Jane Doe": 767,
            "Joe Bloggs": 720,
        }
        assert work_distances == expected_work_distances

    def test_calculate_rest_interval_distances(
        self, workout_service, profiles, workout_one
    ):
        """Test calculate_rest_interval_distances method."""
        rest_distances = workout_service.calculate_rest_interval_distances(
            workout_one, profiles
        )
        expected_rest_distances = {
            "John Smith": 0.0,
            "Jane Doe": 0.0,
            "Joe Bloggs": 0.0,
        }
        assert rest_distances == expected_rest_distances

    def test_print_workout_table(
        self,
        workout_service,
        profiles,
    ):
        """Test print_workout_table method."""
        date = datetime.now().strftime("%d/%m/%Y")
        workout = workout_service.get_workout(
            "Passive Long Intervals - Normal: 3 mins work / 3 mins rest"
        )
        profiles = workout_service.get_fitness_profiles()

        table = workout_service.print_workout_table(workout, profiles)

        assert table.title == f"{workout.name} - {date}"
        assert table.columns[0].header == "Athlete Name"
        assert table.columns[1].header == "Work Distance (m)"
        assert table.columns[2].header == "Rest Distance (m)"

        assert list(table.columns[0].cells) == ["John Smith", "Jane Doe", "Joe Bloggs"]
        assert list(table.columns[1].cells) == ["751.0m", "767.0m", "720.0m"]
        assert list(table.columns[2].cells) == ["0.0m", "0.0m", "0.0m"]
