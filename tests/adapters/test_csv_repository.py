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
    def test_load_workouts(
        self, workout_profile_repo, workout_one, workout_two, workout_three
    ):
        workout_profile_repo._load()

        workout_one_name = "Passive Long Intervals - Normal: 2 mins work / 2 mins rest"
        workout_two_name = (
            "Passive Long Intervals - Extensive: 2 mins work / 1 mins rest"
        )
        workout_three_name = (
            "Passive Long Intervals - Intensive: 2 mins work / 3 mins rest"
        )

        assert workout_profile_repo._workouts[workout_one_name] == workout_one
        assert workout_profile_repo._workouts[workout_two_name] == workout_two
        assert workout_profile_repo._workouts[workout_three_name] == workout_three

    def test_get_workout(
        self, workout_profile_repo, workout_one, workout_two, workout_three
    ):
        cond_workout_one = workout_profile_repo.get(workout_one.name)
        cond_workout_two = workout_profile_repo.get(workout_two.name)
        cond_workout_three = workout_profile_repo.get(workout_three.name)

        assert cond_workout_one == workout_profile_repo._workouts[workout_one.name]
        assert cond_workout_two == workout_profile_repo._workouts[workout_two.name]
        assert cond_workout_three == workout_profile_repo._workouts[workout_three.name]

    def test_get_all_workouts(
        self, workout_profile_repo, workout_one, workout_two, workout_three
    ):
        workouts = workout_profile_repo.get_all()

        assert workout_one in workouts
        assert workout_two in workouts
        assert workout_three in workouts

    def test_add_workout(self, workout_profile_repo, workout_four):
        workout_profile_repo.add(workout_four)

        assert workout_four.name in workout_profile_repo._workouts

    def test_update_workout(self, workout_profile_repo):
        original_work_interval_percentage_mas = 100
        updated_work_interval_percentage_mas = 110

        workout_name = "Passive Long Intervals - Normal: 2 mins work / 2 mins rest"

        workout_one = workout_profile_repo.get(workout_name)
        assert (
            workout_one.work_interval_percentage_mas
            == original_work_interval_percentage_mas
        )

        workout_one.work_interval_percentage_mas = 110
        workout_profile_repo.update(workout_one)

        updated_workout_one = workout_profile_repo.get(workout_name)
        assert (
            updated_workout_one.work_interval_percentage_mas
            == updated_work_interval_percentage_mas
        )

    def test_delete_workout(self, workout_profile_repo):
        workout_name = "Passive Long Intervals - Normal: 2 mins work / 2 mins rest"

        workout_one = workout_profile_repo.get(workout_name)
        assert workout_one in workout_profile_repo.get_all()

        workout_profile_repo.delete(workout_one)

        assert workout_one not in workout_profile_repo.get_all()
