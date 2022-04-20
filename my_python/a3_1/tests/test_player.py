import json
from python.three_one.PlayerState import PlayerState
from python.three_one.Street import Street


def test_valid_player():
    ps = PlayerState(json.load(open("input_valid_blank-player.json", "r")))
    assert ps.get_agents == [0, 0, 0, 0, 0, 0]
    assert ps.get_city_plan_score == ["blank", "blank", "blank"]
    assert ps.get_refusals == 0
    assert ps.get_streets == [Street({"homes": ["blank", False, [False, "blank", False],
                                                [False, "blank", False], [False, "blank", False],
                                                [False, "blank", False], [False, "blank", False],
                                                [False, "blank", False], [False, "blank", False],
                                                [False, "blank", False], [False, "blank", False]],
                                      "parks": 0, "pools": [False, False, False]},
                                     Street({"homes": ["blank", False, [False, "blank", False],
                                                       [False, "blank", False], [False, "blank", False],
                                                       [False, "blank", False], [False, "blank", False],
                                                       [False, "blank", False], [False, "blank", False],
                                                       [False, "blank", False], [False, "blank", False],
                                                       [False, "blank", False]], "parks": 0,
                                             "pools": [False, False, False]}),
                                     Street({"homes": ["blank", False, [False, "blank", False],
                                                       [False, "blank", False], [False, "blank", False],
                                                       [False, "blank", False], [False, "blank", False],
                                                       [False, "blank", False], [False, "blank", False],
                                                       [False, "blank", False], [False, "blank", False],
                                                       [False, "blank", False], [False, "blank", False]],
                                             "parks": 0, "pools": [False, False, False]}))]
    assert ps.get_temps == 0


test_valid_player()
