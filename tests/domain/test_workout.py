from esd.domain.workout import Workout


class TestWorkout:
    def test_workout_from_dict(self):
        workout_dict = {
            "workout_type": "Passive Long Intervals - Normal",
            "work_interval_time": 2,
            "work_interval_percentage_mas": 100.0,
            "work_interval_percentage_asr": 0.0,
            "rest_interval_time": 2,
            "rest_interval_percentage_mas": 0.0,
            "rest_interval_percentage_asr": 0.0,
        }
        workout = Workout.from_dict(workout_dict)
        assert workout == Workout(
            "Passive Long Intervals - Normal", 2, 100.0, 0.0, 2, 0.0, 0.0
        )

    def test_workout_to_dict(self):
        workout = Workout("Passive Long Intervals - Normal", 2, 100.0, 0.0, 2, 0.0, 0.0)
        workout_dict = workout.to_dict()
        assert workout_dict == {
            "workout_type": "Passive Long Intervals - Normal",
            "work_interval_time": 2,
            "work_interval_percentage_mas": 100.0,
            "work_interval_percentage_asr": 0.0,
            "rest_interval_time": 2,
            "rest_interval_percentage_mas": 0.0,
            "rest_interval_percentage_asr": 0.0,
        }

    def test_workout_name_property(self):
        workout = Workout(
            workout_type="Passive Long Intervals - Normal",
            work_interval_time=3,
            work_interval_percentage_mas=1.0,
            work_interval_percentage_asr=None,
            rest_interval_time=3,
            rest_interval_percentage_mas=0.0,
            rest_interval_percentage_asr=None,
        )

        assert (
            workout.name == "Passive Long Intervals - Normal: 3 mins work / 3 mins rest"
        )
