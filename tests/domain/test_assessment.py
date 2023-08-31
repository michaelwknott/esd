from esd.domain.assessment import Assessment


class TestAssessment:
    def test_assessment_init(self, john_smith_2km_time_trial: Assessment):
        """Test Assessment instance is created as expected."""
        assessment = john_smith_2km_time_trial

        assert assessment.athlete_name == "John Smith"
        assert assessment.date == "01/01/2021"
        assert assessment.type == "2km time trial"
        assert assessment.distance == 2000  # noqa: PLR2004
        assert assessment.time == 480  # noqa: PLR2004

    def test_assessment_from_dict(self, john_smith_2km_time_trial: Assessment):
        """Test Assessment instance is created from dictionary as expected."""
        init_dict = {
            "athlete_name": "John Smith",
            "date": "01/01/2021",
            "type": "2km time trial",
            "distance": 2000,
            "time": 480,
        }
        assessment = Assessment.from_dict(init_dict)

        assert assessment == john_smith_2km_time_trial
