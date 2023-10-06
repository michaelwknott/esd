import csv

from esd.domain.workout import Workout


class TestCsvFitnessProfileRepository:
    def test_load_fitness_profiles(
        self, fitness_profile_repo, john_doe_profile, jane_smith_profile
    ):
        fitness_profile_repo._load()

        assert fitness_profile_repo._fitness_profiles["John Doe"] == john_doe_profile
        assert (
            fitness_profile_repo._fitness_profiles["Jane Smith"] == jane_smith_profile
        )

    def test_get_fitness_profile(
        self, fitness_profile_repo, john_doe_profile, jane_smith_profile
    ):
        profile_one = fitness_profile_repo.get(john_doe_profile.name)
        profile_two = fitness_profile_repo.get(jane_smith_profile.name)

        assert john_doe_profile == profile_one
        assert jane_smith_profile == profile_two

    def test_get_all_fitness_profiles(
        self, fitness_profile_repo, john_doe_profile, jane_smith_profile
    ):
        profiles = fitness_profile_repo.get_all()

        assert john_doe_profile in profiles
        assert jane_smith_profile in profiles

    def test_add_fitness_profile(self, fitness_profile_repo, anne_other_profile):
        fitness_profile_repo.add(anne_other_profile)

        assert anne_other_profile.name in fitness_profile_repo._fitness_profiles

    def test_update_fitness_profile(self, fitness_profile_repo):
        original_time_trial_result = 460
        updated_time_trial_result = 450

        jane_smith_profile = fitness_profile_repo.get("Jane Smith")
        assert jane_smith_profile.time_trial_time == original_time_trial_result

        jane_smith_profile.time_trial_time = 450
        fitness_profile_repo.update(jane_smith_profile)

        updated_jane_smith_profile = fitness_profile_repo.get("Jane Smith")
        assert updated_jane_smith_profile.time_trial_time == updated_time_trial_result

    def test_delete_fitness_profile(self, fitness_profile_repo):
        jane_smith_profile = fitness_profile_repo.get("Jane Smith")
        assert jane_smith_profile in fitness_profile_repo.get_all()

        fitness_profile_repo.delete(jane_smith_profile)

        assert jane_smith_profile not in fitness_profile_repo.get_all()


class TestCsvWorkoutRepository:
    def test_load_workouts(self, workout_repo):
        workout1 = Workout("Passive Long Intervals - Normal", 2, 100, 0, 2, 0, 0)
        workout2 = Workout("Passive Long Intervals - Extensive", 2, 100, 0, 1, 0, 0)
        workout3 = Workout("Passive Long Intervals - Intensive", 2, 100, 0, 3, 0, 0)

        workout1_name = "Passive Long Intervals - Normal: 2 mins work / 2 mins rest"
        workout2_name = "Passive Long Intervals - Extensive: 2 mins work / 1 mins rest"
        workout3_name = "Passive Long Intervals - Intensive: 2 mins work / 3 mins rest"

        workout_repo._load()

        assert workout_repo._workouts[workout1_name] == workout1
        assert workout_repo._workouts[workout2_name] == workout2
        assert workout_repo._workouts[workout3_name] == workout3

    def test_save_workouts(self, workout_repo):
        workout1 = Workout(
            "Passive Long Intervals - Normal", 3, 100.0, 0.0, 3, 0.0, 0.0
        )
        workout2 = Workout(
            "Passive Long Intervals - Extensive", 3, 100.0, 0.0, 2, 0.0, 0.0
        )
        workout3 = Workout(
            "Passive Long Intervals - Intensive", 3, 100.0, 0.0, 4, 0.0, 0.0
        )

        additional_workouts = {
            "Passive Long Intervals - Normal: 3 mins work / 3 mins rest": workout1,
            "Passive Long Intervals - Extensive: 3 mins work / 2 mins rest": workout2,
            "Passive Long Intervals - Intensive: 3 mins work / 4 mins rest": workout3,
        }

        workout_repo._workouts.update(additional_workouts)
        workout_repo._save()

        with open(workout_repo._file_path) as f:
            reader = csv.reader(f)
            rows = list(reader)
        assert rows == [
            [
                "workout_type",
                "work_interval_time",
                "work_interval_percentage_mas",
                "work_interval_percentage_asr",
                "rest_interval_time",
                "rest_interval_percentage_mas",
                "rest_interval_percentage_asr",
            ],
            ["Passive Long Intervals - Normal", "2", "100.0", "0.0", "2", "0.0", "0.0"],
            [
                "Passive Long Intervals - Extensive",
                "2",
                "100.0",
                "0.0",
                "1",
                "0.0",
                "0.0",
            ],
            [
                "Passive Long Intervals - Intensive",
                "2",
                "100.0",
                "0.0",
                "3",
                "0.0",
                "0.0",
            ],
            [
                "Passive Long Intervals - Normal",
                "3",
                "100.0",
                "0.0",
                "3",
                "0.0",
                "0.0",
            ],
            [
                "Passive Long Intervals - Extensive",
                "3",
                "100.0",
                "0.0",
                "2",
                "0.0",
                "0.0",
            ],
            [
                "Passive Long Intervals - Intensive",
                "3",
                "100.0",
                "0.0",
                "4",
                "0.0",
                "0.0",
            ],
        ]

    def test_get_workout(self, workout_repo):
        workout = Workout("Passive Long Intervals - Normal", 2, 100.0, 0.0, 2, 0.0, 0.0)
        workout_name = "Passive Long Intervals - Normal: 2 mins work / 2 mins rest"

        cond_workout = workout_repo.get(workout_name)

        assert cond_workout == workout

    def test_get_all_workouts(self, workout_repo):
        workout1 = Workout(
            "Passive Long Intervals - Normal", 2, 100.0, 0.0, 2, 0.0, 0.0
        )
        workout2 = Workout(
            "Passive Long Intervals - Extensive", 2, 100.0, 0.0, 1, 0.0, 0.0
        )
        workout3 = Workout(
            "Passive Long Intervals - Intensive", 2, 100.0, 0.0, 3, 0.0, 0.0
        )

        workouts = workout_repo.get_all()

        assert workout1 in workouts
        assert workout2 in workouts
        assert workout3 in workouts

    def test_add_workout(self, workout_repo, workout_four):
        Workout("Passive Long Intervals - Intensive", 3, 100.0, 0.0, 3, 0.0, 0.0)

        workout_repo.add(workout_four)

        assert workout_four.name in workout_repo._workouts

    def test_update_workout(self, workout_repo):
        original_work_interval_percentage_mas = 100
        updated_work_interval_percentage_mas = 110

        workout_name = "Passive Long Intervals - Normal: 2 mins work / 2 mins rest"

        workout = workout_repo._workouts[workout_name]
        assert (
            workout.work_interval_percentage_mas
            == original_work_interval_percentage_mas
        )

        workout.work_interval_percentage_mas = 110
        workout_repo.update(workout)

        updated_workout = workout_repo._workouts[workout_name]
        assert (
            updated_workout.work_interval_percentage_mas
            == updated_work_interval_percentage_mas
        )

    def test_delete_workout(self, workout_repo):
        workout_name = "Passive Long Intervals - Normal: 2 mins work / 2 mins rest"
        workout = workout_repo._workouts[workout_name]

        assert workout in workout_repo._workouts.values()

        workout_repo.delete(workout)

        assert workout not in workout_repo._workouts.values()
