import pytest
import app
from controllers import games

@pytest.fixture
def api(monkeypatch):
    mock_games = [
    {
        "id": 1,
        "name": "CSGO",
        "release": "2012",
        "genre": "FPS",
        "developer": "Valve",
        "rating": "18+"
    },
    {
        "id": 2,
        "name": "GTA V",
        "release": "2013",
        "genre": "Action",
        "developer": "Rockstar",
        "rating": "18+"
    }
    ]
    monkeypatch.setattr(games, "games", mock_games)
    api = app.app.test_client()
    return api
