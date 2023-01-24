import json

class TestAPICase:
    def test_api_base(self, api):
        response = api.get("/")
        assert response.status_code == 200
        print(response)
        assert response.json['message'] == "Welcome to the game API"

    def test_api_game_route(self, api):
        response = api.get("/games")
        assert response.status_code == 200
        assert response.json == [  
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
    
    def test_api_game_route_id(self, api):
        response = api.get("/games/1")
        assert response.status_code == 200
        assert response.json == {      
                "id": 1,
                "name": "CSGO",
                "release": "2012",
                "genre": "FPS",
                "developer": "Valve",
                "rating": "18+"
            }

    def test_api_game_post(self, api):

        mock_data=json.dumps({
            "name": "Valorant",
            "release": "2020",
            "genre": "FPS",
            "developer": "Riot",
            "rating": "18+"
        })
        mock_headers={ 'Content-Type': 'application/json'}
        response = api.post("/games", data = mock_data, headers=mock_headers)
        assert response.status_code == 201
        assert response.json == {
            "id": 3,
            "name": "Valorant",
            "release": "2020",
            "genre": "FPS",
            "developer": "Riot",
            "rating": "18+"
        }

    
    def test_api_game_delete(self, api):
        response = api.delete("/games/2")
        assert response.status_code == 204
    
    def test_api_game_patch(self, api):
        mock_data=json.dumps({
            "name": "Counter Strike: Global Offensive",
        })
        mock_headers={ 'Content-Type': 'application/json'}
        response = api.patch("/games/1", data = mock_data, headers=mock_headers)
        assert response.status_code == 200
        assert response.json == {
            "id": 1,
            "name": "Counter Strike: Global Offensive",
            "release": "2012",
            "genre": "FPS",
            "developer": "Valve",
            "rating": "18+"
        }
