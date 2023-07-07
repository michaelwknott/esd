from dataclasses import dataclass


@dataclass
class FitnessProfile:
    """Represents an athlete's fitness profile.

    Attributes:
        name: A str of the athlete's name.
        time_trial_distance: An int of the time trial distance in meters.
        sprint_distance: An int of the sprint distance in meters.
        time_trial_time: An int of the time taken to complete the 2km time trial.
        sprint_time: A float of the time taken to complete the 5m sprint.

    Properties:
        max_aerobic_speed: A float representing MAS in meters per second.
        max_sprinting_speed: A float representing MSS in meters per second.
        anaerobic_speed_reserve: A float representing ASR in meters per second.
    """

    name: str
    time_trial_distance: int
    sprint_distance: int
    time_trial_time: int
    sprint_time: float

    @property
    def max_aerobic_speed(self) -> float:
        """Maximal Aerobic Speed in m/s (rounded to 2 decimal places)."""
        if self.time_trial_time != 0:
            return round(self.time_trial_distance / self.time_trial_time, 2)
        else:
            return 0

    @property
    def max_sprinting_speed(self) -> float:
        """Maximum Sprinting Speed in m/s (rounded to 2 decimal places)."""
        if self.sprint_time != 0:
            return round(self.sprint_distance / self.sprint_time, 2)
        else:
            return 0

    @property
    def anaerobic_speed_reserve(self) -> float:
        """Anaerobic Speed Reserve in m/s (rounded to 2 decimal places)."""
        if self.max_aerobic_speed == 0 or self.max_sprinting_speed == 0:
            return 0
        else:
            return round(self.max_sprinting_speed - self.max_aerobic_speed, 2)
