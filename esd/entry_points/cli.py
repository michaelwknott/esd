from rich.console import Console

from esd.adapters.csv_repository import (
    CsvFitnessProfileRepository,
    CsvWorkoutRepository,
)
from esd.service_layer.cli_service import CLIService
from esd.service_layer.service import WorkoutService


def main():
    """Entry point for the command-line interface (CLI).

    It prompts the user to select a workout from a list of available workouts, and then
    displays a table of work and rest interval distances (for the selected workout)
    customized for each athlete's fitness level.
    """
    workout_repo = CsvWorkoutRepository("data/conditioning_workouts.csv")
    fitness_profile_repo = CsvFitnessProfileRepository("data/fitness_assessments.csv")
    workout_service = WorkoutService(workout_repo, fitness_profile_repo)
    cli_service = CLIService(workout_service)

    workout_names = cli_service.workout_service.get_workout_names()

    console = Console()
    console.print("Available workouts:")
    for i, workout in enumerate(workout_names):
        console.print(f"{i+1}. {workout}")
    selected_workout_index = int(input("Select a workout: ")) - 1

    selected_workout = workout_names[selected_workout_index]
    workout = workout_service.get_selected_workout(selected_workout)

    fitness_profiles = workout_service.get_fitness_profiles()

    cli_service.create_and_display_table(workout, fitness_profiles)


if __name__ == "__main__":
    main()
