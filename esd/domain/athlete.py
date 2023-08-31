from esd.domain.assessment import Assessment


class Athlete:
    """Represents an athlete and their identifying information.

    Attributes:
        forename: A str of the athlete's forename.
        surname: A str of the athlete's surname.
        name: A str of the athlete's full name.
        date_of_birth: A str of the athlete's date of birth.
        sport: A str of the athlete's sport.
        assessments: A set of Assessment instances.
    """

    def __init__(self, forename: str, surname: str, date_of_birth: str, sport: str):
        """Initialize Athlete instance.

        Args:
            forename: A str of the athlete's forename.
            surname: A str of the athlete's surname.
            date_of_birth: A str of the athlete's date of birth.
            sport: A str of the athlete's sport.
        """
        self.forename = forename
        self.surname = surname
        self.name = f"{forename} {surname}"
        self.date_of_birth = date_of_birth
        self.sport = sport
        self.assessments: set = set()

    def can_assign_assessment(self, assessment: Assessment) -> bool:
        """Check if athlete can be assigned an assessment.

        Args:
            assessment: An Assessment instance

        Returns:
            bool: True if athlete can be assigned assessment, else False
        """
        return assessment.athlete_name == self.name

    def assign_assessment(self, assessment: Assessment) -> None:
        """Assign an assessment to athlete.

        Args:
            assessment: An Assessment instance
        """
        if self.can_assign_assessment(assessment):
            self.assessments.add(assessment)
