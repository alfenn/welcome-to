from unittest import TestCase
# from contracts import ContractNotRespected
from my_python.archive.a3.PlayerState import *

class TestPlayerState(TestCase):
    empty_valid = {
        "agents": [0,0,0,0,0,0],
        "city-plan-score": ["blank","blank","blank"],
        "refusals": 0,
        "streets": [
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": 0
    }
    # This case has street lens 10,11,11
    street_lens_invalid = {
        "agents": [0,0,0,0,0,0],
        "city-plan-score": ["blank","blank","blank"],
        "refusals": 0,
        "streets": [
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": 0
    }
    city_plan_invalid_score_built_houses = {
        "agents": [0, 0, 0, 0, 0, 0],
        "city-plan-score": [1, "blank", "blank"],
        "refusals": 0,
        "streets": [
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": 0
    }
    agents_invalid_len = {
        "agents": [0, 0, 0, 0, 0, 0, 0],
        "city-plan-score": ["blank", "blank", "blank"],
        "refusals": 0,
        "streets": [
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": 0
    }
    agents_invalid_vals = {
        "agents": [0, 0, 0, 0, 0, "blank"],
        "city-plan-score": ["blank", "blank", "blank"],
        "refusals": 0,
        "streets": [
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": 0
    }
    refusals_invalid_neg1 = {
        "agents": [0, 0, 0, 0, 0, 0],
        "city-plan-score": ["blank", "blank", "blank"],
        "refusals": -1,
        "streets": [
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": 0
    }
    refusals_invalid_four = {
        "agents": [0, 0, 0, 0, 0, 0],
        "city-plan-score": ["blank", "blank", "blank"],
        "refusals": 4,
        "streets": [
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": 0
    }
    temps_too_small = {
        "agents": [0, 0, 0, 0, 0, 0],
        "city-plan-score": ["blank", "blank", "blank"],
        "refusals": 0,
        "streets": [
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": -1
    }
    temps_too_large = {
        "agents": [0, 0, 0, 0, 0, 0],
        "city-plan-score": ["blank", "blank", "blank"],
        "refusals": 0,
        "streets": [
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": 12
    }
    agents_invalid_ind0 = {
        "agents": [2, 0, 0, 0, 0, 0],
        "city-plan-score": ["blank", "blank", "blank"],
        "refusals": 0,
        "streets": [
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": 12
    }
    agents_invalid_ind4 = {
        "agents": [1, 2, 3, 4, 5, 4],
        "city-plan-score": ["blank", "blank", "blank"],
        "refusals": 0,
        "streets": [
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": 12
    }
    city_plan_invalid_geq_zero = {
        "agents": [1, 2, 3, 4, 4, 4],
        "city-plan-score": [1, -1, 10],
        "refusals": 0,
        "streets": [
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": 0
    }

    get_total_built_fences_valid1 = {
        "agents": [0, 0, 0, 0, 0, 0],
        "city-plan-score": ["blank", "blank", "blank"],
        "refusals": 0,
        "streets": [
            {
                "homes": ["blank", False,
                          [True, "blank", False],
                          [True, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [True, "blank", False],
                          [True, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [True, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [True, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": 0
    }
    # misc sum = 1 agent + 3 claimed city plans + 1 pool on third street + 4 temps
    #          = 9
    # num built homes = 7 on ind0 st. + 1 on ind2 st.
    #          = 8
    misc_sum_invalid = {
        "agents": [1, 0, 0, 0, 0, 0],
        "city-plan-score": [10, 10, 10],
        "refusals": 1,
        "streets": [
            {
                "homes": [1, False,
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, 1, False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, True]
            }
        ],
        "temps": 4
    }
    get_total_built_fences_valid2 = {
        "agents": [1, 0, 0, 0, 0, 0],
        "city-plan-score": [10, 10, 10],
        "refusals": 1,
        "streets": [
            {
                "homes": [1, False,
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, 1, False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, True]
            }
        ],
        "temps": 4
    }
    misc_sum_valid = {
        "agents": [1, 0, 0, 0, 0, 0],
        "city-plan-score": [10, 10, 10],
        "refusals": 1,
        "streets": [
            {
                "homes": [1, False,
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [False, [1, "bis"], False],
                          [True, 3, False],
                          [False, "blank", False]],
                "parks": 1,
                "pools": [False, False, False]
            },
            {
                "homes": [1, False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, 1, False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, True]
            }
        ],
        "temps": 4
    }
    misc_sum_invalid_fences = {
        "agents": [0, 0, 0, 0, 0, 0],
        "city-plan-score": ["blank", "blank", "blank"],
        "refusals": 0,
        "streets": [
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [True, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            },
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": 0
    }
    # {"agents": [natural, ...], "city-plan-score": [nb,...3], "refusals": natural, "streets": [street,..
    # .3], "temps": natural}

    def test_contracts(self):
        self.assertTrue(PlayerState(self.empty_valid))
        self.assertRaises(AssertionError, lambda: PlayerState(self.street_lens_invalid))
        self.assertRaises(AssertionError, lambda: PlayerState(self.city_plan_invalid_score_built_houses))
        self.assertRaises(AssertionError, lambda: PlayerState(self.agents_invalid_len))
        self.assertRaises(ContractNotRespected, lambda: PlayerState(self.agents_invalid_vals))
        # note: contracts build from other contracts provide extremely poor error messages--highest level
        #   only. Doesn't show the error call stack.
        self.assertRaises(ContractNotRespected, lambda: PlayerState(self.refusals_invalid_neg1))
        self.assertRaises(AssertionError, lambda: PlayerState(self.refusals_invalid_four))
        self.assertRaises(ContractNotRespected, lambda: PlayerState(self.temps_too_small))
        self.assertRaises(AssertionError, lambda: PlayerState(self.temps_too_large))
        self.assertRaises(AssertionError, lambda: PlayerState(self.agents_invalid_ind0))
        self.assertRaises(AssertionError, lambda: PlayerState(self.agents_invalid_ind4))
        self.assertRaises(ContractNotRespected, lambda: PlayerState(self.city_plan_invalid_geq_zero))
        self.assertRaises(AssertionError, lambda: PlayerState(self.misc_sum_invalid))

    def test_get_total_built_fences(self):
        self.assertEqual(PlayerState(self.get_total_built_fences_valid1).get_total_built_fences(), 12)
        self.assertEqual(PlayerState(self.get_total_built_fences_valid2).get_total_built_fences(), 6)

    def test_validate_num_built_geq_misc(self):
        self.assertRaises(AssertionError, lambda: PlayerState(self.misc_sum_invalid_fences).validate_num_built_houses_geq_misc())
        self.assertRaises(AssertionError, lambda: PlayerState(self.misc_sum_invalid).validate_num_built_houses_geq_misc())
        self.assertTrue(PlayerState(self.misc_sum_valid).validate_num_built_houses_geq_misc())
