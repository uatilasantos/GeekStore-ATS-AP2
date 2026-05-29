import pytest
from database import init_db


@pytest.fixture(autouse=True)
def setup_database():

    init_db()

    yield