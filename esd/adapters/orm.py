import os

from dotenv import load_dotenv
from sqlalchemy import Table, Column, Float, Integer, String, create_engine
from sqlalchemy.orm import registry, sessionmaker

from esd.domain.profile import FitnessProfile
from esd.domain.session import Workout

load_dotenv()
DATABASE_URL = os.environ["DATABASE_URL"]
session_factory = sessionmaker(bind=create_engine(DATABASE_URL, echo=True))


def create_tables_and_mappers():
    """Create tables and mappers for the database."""
    mapper_registry = registry()

    fitness_profile_table = Table(
        "fitness_profile",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String(50)),
        Column("time_trial_distance", Integer),
        Column("sprint_distance", Integer),
        Column("time_trial_time", Integer),
        Column("sprint_time", Float),
    )

    workouts_table = Table(
        "workouts",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("workout_type", String(50)),
        Column("work_interval_time", Integer),
        Column("work_interval_percentage_mas", Float),
        Column("work_interval_percentage_asr", Float, nullable=True),
        Column("rest_interval_time", Integer),
        Column("rest_interval_percentage_mas", Float),
        Column("rest_interval_percentage_asr", Float, nullable=True),
    )

    mapper_registry.map_imperatively(FitnessProfile, fitness_profile_table)
    mapper_registry.map_imperatively(Workout, workouts_table)
