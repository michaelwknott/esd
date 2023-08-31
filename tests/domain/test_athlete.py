from esd.domain.athlete import Athlete


class TestAthlete:
    def test_athlete_init(self, athlete_john_smith: Athlete):
        athlete = athlete_john_smith

        assert athlete.forename == "John"
        assert athlete.surname == "Smith"
        assert athlete.name == "John Smith"
        assert athlete.date_of_birth == "01/01/2000"
        assert athlete.sport == "Boxing"

    def test_athlete_from_dict(self, athlete_john_smith: Athlete):
        init_dict = {
            "forename": "John",
            "surname": "Smith",
            "date_of_birth": "01/01/2000",
            "sport": "Boxing",
        }

        athlete = Athlete(**init_dict)

        assert athlete == athlete_john_smith
