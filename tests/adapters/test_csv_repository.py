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
    fitness_profile_repo, john_doe_profile, jane_smith_profile
):
    profile_one = fitness_profile_repo.get(john_doe_profile.name)
    profile_two = fitness_profile_repo.get(jane_smith_profile.name)

    assert john_doe_profile == profile_one
    assert jane_smith_profile == profile_two


def test_get_all_fitness_profiles(
    fitness_profile_repo, john_doe_profile, jane_smith_profile
):
    profiles = fitness_profile_repo.get_all()

    assert john_doe_profile in profiles
    assert jane_smith_profile in profiles


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


def test_get_workout(workout_profile_repo, workout_one, workout_two, workout_three):
    cond_workout_one = workout_profile_repo.get(workout_one.name)
    cond_workout_two = workout_profile_repo.get(workout_two.name)
    cond_workout_three = workout_profile_repo.get(workout_three.name)

    assert cond_workout_one == workout_profile_repo._workouts[workout_one.name]
    assert cond_workout_two == workout_profile_repo._workouts[workout_two.name]
    assert cond_workout_three == workout_profile_repo._workouts[workout_three.name]


def test_get_all_workouts(
    workout_profile_repo, workout_one, workout_two, workout_three
):
    workouts = workout_profile_repo.get_all()

    assert workout_one in workouts
    assert workout_two in workouts
    assert workout_three in workouts
