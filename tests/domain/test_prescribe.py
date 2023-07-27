class TestPrescribe:
    # names
    ATHLETE_ONE_NAME = "John Smith"
    ATHLETE_MISSING_MAS_NAME = "Anne Other"
    ATHLETE_MISSING_MSS_NAME = "Sam Jones"

    # Work interval distance in meters (% mas * work interval time in seconds)
    ATHLETE_ONE_WORK_DISTANCE = 751
    ATHLETE_MISSING_MAS_WORK_DISTANCE = 0
    ATHLETE_MISSING_MSS_WORK_DISTANCE = 857

    # Rest interval distance in meters (% mas * work interval time in seconds)
    ATHLETE_ONE_REST_DISTANCE = 0
    ATHLETE_MISSING_MAS_REST_DISTANCE = 0
    ATHLETE_MISSING_MSS_REST_DISTANCE = 0

    def test_calculate_work_interval_distance(self, mas_work_distances):
        assert (
            mas_work_distances[TestPrescribe.ATHLETE_ONE_NAME]
            == TestPrescribe.ATHLETE_ONE_WORK_DISTANCE
        )
        assert (
            mas_work_distances[TestPrescribe.ATHLETE_MISSING_MAS_NAME]
            == TestPrescribe.ATHLETE_MISSING_MAS_WORK_DISTANCE
        )
        assert (
            mas_work_distances[TestPrescribe.ATHLETE_MISSING_MSS_NAME]
            == TestPrescribe.ATHLETE_MISSING_MSS_WORK_DISTANCE
        )

    def test_calculate_rest_interval_distance(self, mas_rest_distances):
        assert (
            mas_rest_distances[TestPrescribe.ATHLETE_ONE_NAME]
            == TestPrescribe.ATHLETE_ONE_REST_DISTANCE
        )
        assert (
            mas_rest_distances[TestPrescribe.ATHLETE_MISSING_MAS_NAME]
            == TestPrescribe.ATHLETE_MISSING_MAS_REST_DISTANCE
        )
        assert (
            mas_rest_distances[TestPrescribe.ATHLETE_MISSING_MSS_NAME]
            == TestPrescribe.ATHLETE_MISSING_MSS_REST_DISTANCE
        )
