class TestAthlete:
    def test_athlete_init(self, athlete_john_smith):
        athlete = athlete_john_smith

        assert athlete.forename == "John"
        assert athlete.surname == "Smith"
        assert athlete.name == "John Smith"
        assert athlete.date_of_birth == "01/01/2000"
        assert athlete.sport == "Boxing"
        assert athlete.assessments == set()

    def test_can_assign_assessment(self, athlete_john_smith, john_smith_2km_time_trial):
        athlete = athlete_john_smith
        assessment = john_smith_2km_time_trial

        assert athlete.can_assign_assessment(assessment)

    def test_cannot_assign_assessment(
        self, athlete_john_smith, anne_other_2km_time_trial
    ):
        athlete = athlete_john_smith
        assessment = anne_other_2km_time_trial

        assert not athlete.can_assign_assessment(assessment)

    def test_assign_assessment(self, athlete_john_smith, john_smith_2km_time_trial):
        athlete = athlete_john_smith
        assessment = john_smith_2km_time_trial

        athlete.assign_assessment(assessment)

        assert assessment in athlete.assessments

    def cannot_assign_assessment_if_names_do_not_match(
        self, athlete_john_smith, anne_other_2km_time_trial
    ):
        athlete = athlete_john_smith
        assessment = anne_other_2km_time_trial

        athlete.assign_assessment(assessment)

        assert assessment not in athlete.assessments
