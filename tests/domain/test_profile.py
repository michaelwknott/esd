class TestProfile:
    PROFILE_ONE_MAS = 4.17
    PROFILE_ONE_MSS = 8.33
    PROFILE_ONE_ASR = 4.16

    def test_max_aerobic_speed_property(self, profile_one):
        assert profile_one.max_aerobic_speed == TestProfile.PROFILE_ONE_MAS

    def test_max_sprinting_speed_property(self, profile_one):
        assert profile_one.max_sprinting_speed == TestProfile.PROFILE_ONE_MSS

    def test_anaerobic_speed_reserve_property(self, profile_one):
        assert profile_one.anaerobic_speed_reserve == TestProfile.PROFILE_ONE_ASR

    def test_missing_max_aerobic_speed(self, profile_missing_mas):
        assert profile_missing_mas.max_aerobic_speed == 0

    def test_missing_max_sprinting_speed(self, profile_missing_mss):
        assert profile_missing_mss.max_sprinting_speed == 0

    def test_missing_max_aerobic_speed_on_anaerobic_speed_reserve(
        self, profile_missing_mas
    ):
        assert profile_missing_mas.anaerobic_speed_reserve == 0

    def test_missing_max_sprinting_speed_on_anaerobic_speed_reserve(
        self, profile_missing_mss
    ):
        assert profile_missing_mss.anaerobic_speed_reserve == 0
