games = [
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
    },
    {
        "id": 3,
        "name": "Minecraft",
        "release": "2009",
        "genre": "Sandbox",
        "developer": "Mojang",
        "rating": "7+"
    },
    {
        "id": 4,
        "name": "PUBG",
        "release": "2017",
        "genre": "Battle Royale",
        "developer": "PUBG Corp",
        "rating": "18+"
    },
    {
        "id": 5,
        "name": "Zelda Breath of the Wild",
        "release": "2017",
        "genre": "Action",
        "developer": "Nintendo",
        "rating": "7+"
    },
    {
        "id": 6,
        "name": "Zelda Ocarina of Time",
        "release": "1998",
        "genre": "Action",
        "developer": "Nintendo",
        "rating": "7+"
    },
    {
        "id": 7,
        "name": "Mario Kart 8",
        "release": "2014",
        "genre": "Racing",
        "developer": "Nintendo",
        "rating": "7+"
    },
    {  
        "id": 8,
        "name": "Rocket League",
        "release": "2015",
        "genre": "Sports",
        "developer": "Psyonix",
        "rating": "7+"
    },
    {
        "id": 9,
        "name": "Goat Simulator",
        "release": "2014",
        "genre": "Simulation",
        "developer": "Coffee Stain Studios",
        "rating": "7+"        
    }
]

def index(request):
    return [g for g in games], 200

def get_game(request, game_name):
    for g in games:
        if g["name"] == game_name:
            return g, 200
    return {"error": "Game not found"}, 404

def show(request, game_id):
    game = find_by_id(game_id)
    if game:
        return game, 200
    return {"error": "Game not found"}, 404

def create(request):
    data = request.get_json()
    games.append(data)
    return data, 201

def destroy(request, game_id):
    game = find_by_id(game_id)
    if game:
        games.remove(game)
        return {"message": "Game deleted"}, 200
    return {"error": "Game not found"}, 404

def update(request, game_id):
    game = find_by_id(game_id)
    if game:
        data = request.get_json()
        game.update(data)
        return game, 200
    return {"error": "Game not found"}, 404
    



def find_by_id(id):
    for g in games:
        if g["id"] == id:
            return g
    return False
