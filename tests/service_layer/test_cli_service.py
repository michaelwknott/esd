from datetime import datetime


class TestCLIService:
    def test_print_workout_table(
        self,
        cli_service,
        profiles,
    ):
        """Test print_workout_table method."""
        date = datetime.now().strftime("%d/%m/%Y")
        workout = cli_service.workout_service.get_selected_workout(
            "Passive Long Intervals - Normal: 3 mins work / 3 mins rest"
        )
        profiles = cli_service.workout_service.get_fitness_profiles()

        table = cli_service.create_and_display_table(workout, profiles)

        assert table.title == f"{workout.name} - {date}"
        assert table.columns[0].header == "Athlete Name"
        assert table.columns[1].header == "Work Distance (m)"
        assert table.columns[2].header == "Rest Distance (m)"

        assert list(table.columns[0].cells) == ["John Smith", "Jane Doe", "Joe Bloggs"]
        assert list(table.columns[1].cells) == ["751.0m", "767.0m", "720.0m"]
        assert list(table.columns[2].cells) == ["0.0m", "0.0m", "0.0m"]
