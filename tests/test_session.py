class TestWorkout:
    def test_workout_name_property(self, workout):
        assert (
            workout.name == "Passive Long Intervals - Normal: 3 mins work / 3 mins rest"
        )
