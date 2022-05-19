from unittest import TestCase

input5_team15 = [
    {
        "city-plans": [
            {
                "criteria":[1,1,4],
                "position":1,
                "score1":8,
                "score2":4
            },
            {
                "criteria":[2,3,6],
                "position":2,
                "score1":10,
                "score2":6
            },
            {
                "criteria":[1,5],
                "position":3,
                "score1":7,
                "score2":3
            }],
        "city-plans-won":[False,False,False],
        "construction-cards":[[4,"surveyor"],[5,"pool"],[10,"bis"]],
        "effects":["temp","surveyor","bis"]
    },
    {
        "agents":[0,0,0,0,0,0],
        "city-plan-score":["blank","blank","blank"],
        "refusals":0,
        "streets":[
            {
                "homes":[0,False,[False,1,False],[False,"blank",False],[False,3,False],[True,4,False],[False,5,False],[False,6,False],[False,7,False],[True,8,False],[False,9,False]],
                "parks":0,
                "pools":[False,False,False]
            },
            {
                "homes":[0,False,[False,1,False],[False,2,False],[False,3,False],[False,4,False],[False,5,False],[True,6,False],[False,7,False],[False,8,False],[False,9,False],[False,10,False]],
                "parks":0,
                "pools":[False,False,False]
            },
            {
                "homes":[0,False,[False,1,False],[False,2,False],[False,3,False],[False,4,False],[False,"blank",False],[True,"blank",False],[False,7,False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,11,False]],
                "parks":0,
                "pools":[False,False,False]
            }],
        "temps":0
    }
]
class TestFailingGenValidMove(TestCase):
    print(GenValidMove(GameState(input5_team15[0]), PlayerState(input5_team15[1])))
    # print(Street({
    #             "homes":[0,False,[False,1,False],[False,"blank",False],[False,3,False],[True,4,False],[False,5,False],[False,6,False],[False,7,False],[True,8,False],[False,9,False]],
    #             "parks":0,
    #             "pools":[False,False,False]
    #         }))
    pass

