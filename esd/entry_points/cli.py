from rich.console import Console
from rich.table import Table

from esd.adapters.csv_repository import (
    CsvFitnessProfileRepository,
    CsvWorkoutRepository,
)
from esd.domain.session import Workout
from esd.service_layer.service import WorkoutService

from datetime import datetime


def create_and_display_table(
    workout: Workout, work_distances: dict[str, float], rest_distances: dict[str, float]
) -> Table:
    """Create and display a table of work and rest interval distances.

    Args:
        workout: The training variables for the workout.
        work_distances: A dictionary of athlete names mapped to work interval
            distances.
        rest_distances: A dictionary of athlete names mapped to rest interval
            distances.


    Returns:
        A table of work and rest interval distances.
    """
    console = Console()
    date = datetime.now().strftime("%d/%m/%Y")
    table = Table(title=f"{workout.name} - {date}")
    table.add_column("Athlete Name", justify="left")
    table.add_column("Work Distance (m)", justify="center")
    table.add_column("Rest Distance (m)", justify="center")

    for athlete in work_distances:
        table.add_row(
            athlete,
            f"{work_distances[athlete]}m",
            f"{rest_distances[athlete]}m",
        )
    console.print(table)
    return table


def cli():
    """Entry point for the command-line interface (CLI).

    It prompts the user to select a workout from a list of available workouts, and then
    displays a table of work and rest interval distances (for the selected workout)
    customized for each athlete's fitness level.
    """
    workout_repo = CsvWorkoutRepository("data/conditioning_workouts.csv")
    fitness_profile_repo = CsvFitnessProfileRepository("data/fitness_assessments.csv")
    workout_service = WorkoutService(workout_repo, fitness_profile_repo)

    workout_names = workout_service.get_workout_names()

    console = Console()
    console.print("Available workouts:")
    for i, workout in enumerate(workout_names):
        console.print(f"{i+1}. {workout}")
    selected_workout_index = int(input("Select a workout: ")) - 1

    selected_workout = workout_names[selected_workout_index]
    workout = workout_service.get_selected_workout(selected_workout)

    fitness_profiles = workout_service.get_fitness_profiles()

    work_distances, rest_distances = workout_service.calculate_interval_distances(
        workout, fitness_profiles
    )

    create_and_display_table(workout, work_distances, rest_distances)


if __name__ == "__main__":
    cli()
