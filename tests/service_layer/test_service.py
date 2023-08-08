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
