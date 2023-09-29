from esd.domain.prescribe import (
    calculate_work_interval_distances,
    calculate_rest_interval_distances,
)


class TestPrescribe:
    def test_calculate_work_interval_distances(self, fitness_profiles, workout):
        """Test calculate_work_interval_distances method."""
        work_distances = calculate_work_interval_distances(workout, fitness_profiles)
        expected_work_distances = {
            "John Smith": 751,
            "Anne Other": 0,
            "Sam Jones": 857,
        }
        assert work_distances == expected_work_distances

    def test_calculate_rest_interval_distances(self, fitness_profiles, workout):
        """Test calculate_rest_interval_distances method."""
        rest_distances = calculate_rest_interval_distances(workout, fitness_profiles)
        expected_rest_distances = {
            "John Smith": 0.0,
            "Anne Other": 0.0,
            "Sam Jones": 0.0,
        }
        assert rest_distances == expected_rest_distances
