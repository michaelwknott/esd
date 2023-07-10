from dataclasses import dataclass


@dataclass
class Workout:
    """Workout type and it's associated training variables."""

    workout_type: str
    work_interval_time: int
    work_interval_percentage_mas: float
    work_interval_percentage_asr: float | None
    rest_interval_time: int
    rest_interval_percentage_mas: float
    rest_interval_percentage_asr: float | None

    @property
    def name(self) -> str:
        """Name and description of workout.

        Returns:
            A string containing workout name and description.
        """
        return (
            f"{self.workout_type}: "
            f"{self.work_interval_time} mins work / "
            f"{self.rest_interval_time} mins rest"
        )


if __name__ == "__main__":
    w = Workout(
        workout_type="Passive Long Intervals - Normal",
        work_interval_time=3,
        work_interval_percentage_mas=100,
        work_interval_percentage_asr=None,
        rest_interval_time=3,
        rest_interval_percentage_mas=100,
        rest_interval_percentage_asr=None,
    )
