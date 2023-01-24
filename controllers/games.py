games = [
    {
        "id": 1,
        "name": "CSGO",
        "release": "2012",
        "genre": "FPS",
        "developer": "Valve",
        "rating": "18+",
        "image": "http://media.steampowered.com/apps/csgo/blog/images/fb_image.png?v=6"
    },
    {
        "id": 2,
        "name": "GTA V",
        "release": "2013",
        "genre": "Action",
        "developer": "Rockstar",
        "rating": "18+",
        "image": "https://media.rockstargames.com/rockstargames/img/global/news/upload/actual_1364906194.jpg"

    },
    {
        "id": 3,
        "name": "Minecraft",
        "release": "2009",
        "genre": "Sandbox",
        "developer": "Mojang",
        "rating": "7+",
        "image": "https://image.api.playstation.com/vulcan/img/cfn/11307x4B5WLoVoIUtdewG4uJ_YuDRTwBxQy0qP8ylgazLLc01PBxbsFG1pGOWmqhZsxnNkrU3GXbdXIowBAstzlrhtQ4LCI4.png"

    },
    {
        "id": 4,
        "name": "PUBG",
        "release": "2017",
        "genre": "Battle Royale",
        "developer": "PUBG Corp",
        "rating": "18+",
        "image": "https://www.vsi.tv/fileadmin/_processed_/8/0/csm_PUBG_ed076bcd70.jpg"

    },
    {
        "id": 5,
        "name": "Zelda Breath of the Wild",
        "release": "2017",
        "genre": "Action",
        "developer": "Nintendo",
        "rating": "7+",
        "image": "https://assets-prd.ignimgs.com/2022/06/14/zelda-breath-of-the-wild-1655249167687.jpg"

    },
    {
        "id": 6,
        "name": "Zelda Ocarina of Time",
        "release": "1998",
        "genre": "Action",
        "developer": "Nintendo",
        "rating": "7+",
        "image": "https://assets1.ignimgs.com/2019/06/04/legend-of-zelda-ocarina-of-time-3d-1559683061479.jpg"

    },
    {
        "id": 7,
        "name": "Mario Kart 8",
        "release": "2014",
        "genre": "Racing",
        "developer": "Nintendo",
        "rating": "7+",
        "image": "https://e.snmc.io/lk/gv/x/4d7bc436fe1e4ee8108bceb9ca3eada8/9212913"
    },
    {  
        "id": 8,
        "name": "Rocket League",
        "release": "2015",
        "genre": "Sports",
        "developer": "Psyonix",
        "rating": "7+",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Rocket_League_coverart.jpg"
    },
    {
        "id": 9,
        "name": "Goat Simulator",
        "release": "2014",
        "genre": "Simulation",
        "developer": "Coffee Stain Studios",
        "rating": "7+",      
        "image": "https://image.api.playstation.com/cdn/EP4415/CUSA02779_00/05UDaF6g0ZyfhUZdSg5xgRRpuNBDep4Q.png"  
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
    data["id"] = games[-1]["id"] + 1
    games.append(data)
    return data, 201

def destroy(request, game_id):
    game = find_by_id(game_id)
    if game:
        games.remove(game)
        return {"message": "Game deleted"}, 204
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
