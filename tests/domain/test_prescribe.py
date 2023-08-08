from esd.domain.prescribe import (
    calculate_rest_interval_distances,
    calculate_work_interval_distances,
)


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

    def test_calculate_work_interval_distance(self, workout, fitness_profiles):
        work_distances = calculate_work_interval_distances(workout, fitness_profiles)

        assert (
            work_distances[TestPrescribe.ATHLETE_ONE_NAME]
            == TestPrescribe.ATHLETE_ONE_WORK_DISTANCE
        )
        assert (
            work_distances[TestPrescribe.ATHLETE_MISSING_MAS_NAME]
            == TestPrescribe.ATHLETE_MISSING_MAS_WORK_DISTANCE
        )
        assert (
            work_distances[TestPrescribe.ATHLETE_MISSING_MSS_NAME]
            == TestPrescribe.ATHLETE_MISSING_MSS_WORK_DISTANCE
        )

    def test_calculate_rest_interval_distance(self, workout, fitness_profiles):
        rest_distances = calculate_rest_interval_distances(workout, fitness_profiles)

        assert (
            rest_distances[TestPrescribe.ATHLETE_ONE_NAME]
            == TestPrescribe.ATHLETE_ONE_REST_DISTANCE
        )
        assert (
            rest_distances[TestPrescribe.ATHLETE_MISSING_MAS_NAME]
            == TestPrescribe.ATHLETE_MISSING_MAS_REST_DISTANCE
        )
        assert (
            rest_distances[TestPrescribe.ATHLETE_MISSING_MSS_NAME]
            == TestPrescribe.ATHLETE_MISSING_MSS_REST_DISTANCE
        )
