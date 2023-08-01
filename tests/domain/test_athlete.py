class TestAthleteProfile:
    ATHLETE_ONE_MAS = 4.17
    ATHLETE_ONE_MSS = 8.33
    ATHLETE_ONE_ASR = 4.16

    def test_max_aerobic_speed_property(self, athlete_one):
        assert athlete_one.max_aerobic_speed == TestAthleteProfile.ATHLETE_ONE_MAS

    def test_max_sprinting_speed_property(self, athlete_one):
        assert athlete_one.max_sprinting_speed == TestAthleteProfile.ATHLETE_ONE_MSS

    def test_anaerobic_speed_reserve_property(self, athlete_one):
        assert athlete_one.anaerobic_speed_reserve == TestAthleteProfile.ATHLETE_ONE_ASR

    def test_missing_max_aerobic_speed(self, athlete_missing_mas):
        assert athlete_missing_mas.max_aerobic_speed == 0

    def test_missing_max_sprinting_speed(self, athlete_missing_mss):
        assert athlete_missing_mss.max_sprinting_speed == 0

    def test_missing_max_aerobic_speed_on_anaerobic_speed_reserve(
        self, athlete_missing_mas
    ):
        assert athlete_missing_mas.anaerobic_speed_reserve == 0

    def test_missing_max_sprinting_speed_on_anaerobic_speed_reserve(
        self, athlete_missing_mss
    ):
        assert athlete_missing_mss.anaerobic_speed_reserve == 0
