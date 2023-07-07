class FitnessProfile:
    """Represents an athlete's fitness profile.

    Attributes:
        name: A str of the athlete's name.
        time_trial_time: An int of the time taken to complete the 2km time trial.
        sprint_time: A float of the time taken to complete the 5m sprint.

    Properties:
        max_aerobic_speed: A float representing MAS in meters per second.
        max_sprinting_speed: A float representing MSS in meters per second.
        anaerobic_speed_reserve: A float representing ASR in meters per second.
    """

    TIME_TRIAL_DISTANCE: float = 2000
    """Time trial distance in meters."""

    SPRINT_DISTANCE: float = 5
    """Sprint distance in meters."""

    def __init__(self, name: str, time_trial_time: int, sprint_time: float) -> None:
        """Initializes a new instance of the Athlete class.

        Args:
            name: The name of the athlete.
            time_trial_time: The time taken to complete the 2km time trial.
            sprint_time: The time taken to complete the 5m sprint.
        """
        self.name: str = name
        self.time_trial_time: float = time_trial_time
        self.sprint_time: float = sprint_time

    @property
    def max_aerobic_speed(self) -> float:
        """Maximal Aerobic Speed in m/s (rounded to 2 decimal places)."""
        if self.time_trial_time != 0:
            return round(self.TIME_TRIAL_DISTANCE / self.time_trial_time, 2)
        else:
            return 0

    @property
    def max_sprinting_speed(self) -> float:
        """Maximum Sprinting Speed in m/s (rounded to 2 decimal places)."""
        if self.sprint_time != 0:
            return round(self.SPRINT_DISTANCE / self.sprint_time, 2)
        else:
            return 0

    @property
    def anaerobic_speed_reserve(self) -> float:
        """Anaerobic Speed Reserve in m/s (rounded to 2 decimal places)."""
        if self.max_aerobic_speed == 0 or self.max_sprinting_speed == 0:
            return 0
        else:
            return round(self.max_sprinting_speed - self.max_aerobic_speed, 2)
