from unittest import TestCase

excl_range1_emptyst = Homes(
    ["blank", False,
     [False, "blank", False],
     [False, "blank", False],
     [False, "blank", False],
     [False, "blank", False],
     [False, "blank", False],
     [False, "blank", False],
     [False, "blank", False],
     [False, "blank", False],
     [False, "blank", False],
     [False, "blank", False]]
)

excl_range2 = Homes(
    [1, False,
     [False, [1, "bis"], False],
     [False, "blank", False],
     [False, [2, "bis"], False],
     [False, [2, "bis"], False],
     [False, [2, "bis"], False],
     [False, [2, "bis"], False],
     [False, [2, "bis"], False],
     [False, [2, "bis"], False],
     [False, [2, "bis"], False],
     [False, 2, False]]
)

excl_range3 = Homes(
    [1, False,
     [False, 2, False],
     [False, "blank", False],
     [False, 4, False],
     [False, "blank", False],
     [False, "blank", False],
     [False, 6, False],
     [False, 7, False],
     [False, "blank", False],
     [False, "blank", False],
     [False, "blank", False]]
)

vm_cc1_same = [
    [1, "bis"],
    [1, "bis"],
    [1, "bis"]
]

vm_cc2 = [
    [2, "bis"],
    [5, "bis"],
    [15, "bis"]
]

ps_empty = {"agents": [0, 0, 0, 0, 0, 0], "city-plan-score": ["blank", "blank", "blank"], "refusals": 0, "streets": [{
                                                                                                                         "homes": [
                                                                                                                             "blank",
                                                                                                                             False,
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False]],
                                                                                                                         "parks": 0,
                                                                                                                         "pools": [
                                                                                                                             False,
                                                                                                                             False,
                                                                                                                             False]},
                                                                                                                     {
                                                                                                                         "homes": [
                                                                                                                             "blank",
                                                                                                                             False,
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False]],
                                                                                                                         "parks": 0,
                                                                                                                         "pools": [
                                                                                                                             False,
                                                                                                                             False,
                                                                                                                             False]},
                                                                                                                     {
                                                                                                                         "homes": [
                                                                                                                             "blank",
                                                                                                                             False,
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False],
                                                                                                                             [
                                                                                                                                 False,
                                                                                                                                 "blank",
                                                                                                                                 False]],
                                                                                                                         "parks": 0,
                                                                                                                         "pools": [
                                                                                                                             False,
                                                                                                                             False,
                                                                                                                             False]}],
            "temps": 0}

ps_built_2_at_0_0 = {"agents": [0, 0, 0, 0, 0, 0], "city-plan-score": ["blank", "blank", "blank"], "refusals": 0,
                     "streets": [{"homes": [2, False, [False, "blank", False], [False, "blank", False],
                                            [False, "blank", False], [False, "blank", False], [False, "blank", False],
                                            [False, "blank", False], [False, "blank", False], [False, "blank", False],
                                            [False, "blank", False]], "parks": 0, "pools": [False, False, False]}, {
                                     "homes": ["blank", False, [False, "blank", False], [False, "blank", False],
                                               [False, "blank", False], [False, "blank", False],
                                               [False, "blank", False], [False, "blank", False],
                                               [False, "blank", False], [False, "blank", False],
                                               [False, "blank", False], [False, "blank", False]], "parks": 0,
                                     "pools": [False, False, False]}, {
                                     "homes": ["blank", False, [False, "blank", False], [False, "blank", False],
                                               [False, "blank", False], [False, "blank", False],
                                               [False, "blank", False], [False, "blank", False],
                                               [False, "blank", False], [False, "blank", False],
                                               [False, "blank", False], [False, "blank", False],
                                               [False, "blank", False]], "parks": 0, "pools": [False, False, False]}],
                     "temps": 0}

ps_built_15_at_1_7 = {"agents": [0, 0, 0, 0, 0, 0], "city-plan-score": ["blank", "blank", "blank"], "refusals": 0,
                      "streets": [{"homes": [2, False, [False, "blank", False], [False, "blank", False],
                                             [False, "blank", False], [False, "blank", False], [False, "blank", False],
                                             [False, "blank", False], [False, "blank", False], [False, "blank", False],
                                             [False, "blank", False]], "parks": 0, "pools": [False, False, False]}, {
                                      "homes": ["blank", False, [False, "blank", False], [False, "blank", False],
                                                [False, "blank", False], [False, "blank", False],
                                                [False, "blank", False], [False, "blank", False], [False, 15, False],
                                                [False, "blank", False], [False, "blank", False],
                                                [False, "blank", False]], "parks": 0, "pools": [False, False, False]}, {
                                      "homes": ["blank", False, [False, "blank", False], [False, "blank", False],
                                                [False, "blank", False], [False, "blank", False],
                                                [False, "blank", False], [False, "blank", False],
                                                [False, "blank", False], [False, "blank", False],
                                                [False, "blank", False], [False, "blank", False],
                                                [False, "blank", False]], "parks": 0, "pools": [False, False, False]}],
                      "temps": 0}


class TestGenValidMove(TestCase):
    def test_get_exclusive_range(self):
        self.assertEqual(get_exclusive_range(excl_range1_emptyst, 4), (-1, 18))
        self.assertEqual(get_exclusive_range(excl_range2, 2), (1, 2))
        self.assertEqual(get_exclusive_range(excl_range3, 5), (4, 6))

    def test_vm_construction_card_index(self):
        exc_range1 = get_exclusive_range(excl_range1_emptyst, 4)
        exc_range2 = get_exclusive_range(excl_range2, 2)
        exc_range3 = get_exclusive_range(excl_range3, 5)
        self.assertEqual(vm_construction_card_index(vm_cc1_same, exc_range1), 0)
        self.assertEqual(vm_construction_card_index(vm_cc1_same, exc_range2), -1)
        self.assertEqual(vm_construction_card_index(vm_cc1_same, exc_range3), -1)
        self.assertEqual(vm_construction_card_index(vm_cc2, exc_range1), 0)
        self.assertEqual(vm_construction_card_index(vm_cc2, exc_range2), -1)
        self.assertEqual(vm_construction_card_index(vm_cc2, exc_range3), 1)

    def test_update_ps_w_valid_card(self):
        # update_ps_w_valid_card(cc: list, ps: PlayerState, st_i: int, h_i: int)
        self.assertTrue(update_ps_w_valid_card(vm_cc2,
                                               PlayerState(ps_empty),
                                               0,
                                               0),
                        PlayerState(ps_built_2_at_0_0))
        self.assertTrue(update_ps_w_valid_card(vm_cc2,
                                               PlayerState(ps_empty),
                                               1,
                                               7),
                        PlayerState(ps_built_15_at_1_7))
