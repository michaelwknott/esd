from datetime import datetime

from rich.console import Console
from rich.table import Table

from esd.domain.athlete import FitnessProfile
from esd.domain.session import Workout
from esd.service_layer.service import WorkoutService


class CLIService:
    """Service class for CLI related operations."""

    def __init__(self, workout_service: WorkoutService):
        """Initialise CLIService with WorkoutService."""
        self.workout_service = workout_service

    def create_and_display_table(
        self, workout: Workout, fitness_profiles: list[FitnessProfile]
    ) -> Table:
        """Print a table of names, work interval and rest interval distances.

        Args:
            workout: The training variables for the workout.
            fitness_profiles: The fitness profile for each athlete completing the
                workout.
        """
        work_distances = self.workout_service.calculate_work_interval_distances(
            workout, fitness_profiles
        )
        rest_distances = self.workout_service.calculate_rest_interval_distances(
            workout, fitness_profiles
        )

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
