import sys

from my_python.Street import Street
from my_python.House import House

sys.path.append('../../../../')
from my_python.Same import Same

empty_valid = {
    "agents": [0, 0, 0, 0, 0, 0],
    "city-plan-score": ["blank", "blank", "blank"],
    "refusals": 0,
    "streets": [
        {
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
    "agents": [0, 0, 0, 0, 0, 0],
    "city-plan-score": ["blank", "blank", "blank"],
    "refusals": 0,
    "streets": [
        {
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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

# get_total_built_fences_invalid1 = {
#     "agents": [0, 0, 0, 0, 0, 0],
#     "city-plan-score": ["blank", "blank", "blank"],
#     "refusals": 0,
#     "streets": [
#         {
#             "houses": ["blank", False,
#                        [True, "blank", False],
#                        [True, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False]],
#             "parks": 0,
#             "pools": [False, False, False]
#         },
#         {
#             "houses": ["blank", False,
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [True, "blank", False],
#                        [True, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [True, "blank", False]],
#             "parks": 0,
#             "pools": [False, False, False]
#         },
#         {
#             "houses": ["blank", False,
#                        [False, "blank", False],
#                        [True, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False],
#                        [False, "blank", False]],
#             "parks": 0,
#             "pools": [False, False, False]
#         }
#     ],
#     "temps": 0
# }

# misc sum = 1 agent + 3 claimed city plans + 1 pool on third street + 4 temps
#          = 9
# num built houses = 7 on ind0 st. + 1 on ind2 st.
#          = 8
misc_sum_invalid = {
    "agents": [1, 0, 0, 0, 0, 0],
    "city-plan-score": [10, 10, 10],
    "refusals": 1,
    "streets": [
        {
            "houses": [1, False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": [1, False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": [1, False,
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
            "houses": [1, False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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
            "houses": ["blank", False,
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

same_house = House(is_bis=Same(), num=Same(), is_built=Same(), used_in_plan=Same(), l_fence=Same(), r_fence=Same())
all_same_ps = {
    "agents": [Same(), Same(), Same(), Same(), Same(), Same()],
    "city-plan-score": [Same(), Same(), Same()],
    "refusals": Same(),
    "streets": [
        Street(houses=[same_house, same_house, same_house, same_house, same_house, same_house, same_house, same_house,
                       same_house, same_house],
               parks=Same(),
               pools=[Same(), Same(), Same()]),
        Street(houses=[same_house, same_house, same_house, same_house, same_house, same_house, same_house, same_house,
                       same_house, same_house, same_house],
               parks=Same(),
               pools=[Same(), Same(), Same()]),
        Street(houses=[same_house, same_house, same_house, same_house, same_house, same_house, same_house, same_house,
                       same_house, same_house, same_house, same_house],
               parks=Same(),
               pools=[Same(), Same(), Same()])
    ],
    "temps": Same()
}

get_total_built_fences_valid2_empty_valid_sub_ps = {
    "agents": [1, Same(), Same(), Same(), Same(), Same()],
    "city-plan-score": [10, 10, 10],
    "refusals": 1,
    "streets": [
        Street(houses=[House(inp_house=1, used_in_plan=False, l_fence=True, r_fence=False),
                       House(inp_house=[1, "bis"], used_in_plan=False, l_fence=False, r_fence=False),
                       House(inp_house=[1, "bis"], used_in_plan=False, l_fence=False, r_fence=False),
                       House(inp_house=[1, "bis"], used_in_plan=False, l_fence=False, r_fence=False),
                       House(inp_house=[1, "bis"], used_in_plan=False, l_fence=False, r_fence=False),
                       House(inp_house=[1, "bis"], used_in_plan=False, l_fence=False, r_fence=False),
                       House(inp_house=[1, "bis"], used_in_plan=False, l_fence=False, r_fence=False),
                       same_house, same_house, same_house],
               parks=Same(),
               pools=[Same(), Same(), Same()]),
        Street(houses=[same_house, same_house, same_house, same_house, same_house, same_house, same_house, same_house,
                       same_house, same_house, same_house],
               parks=Same(),
               pools=[Same(), Same(), Same()]),
        Street(houses=[same_house, same_house, same_house, same_house, same_house, same_house, same_house, same_house,
                       same_house, same_house,
                       House(inp_house=1, used_in_plan=False, l_fence=False, r_fence=False),
                       same_house],
               parks=Same(),
               pools=[Same(), Same(), True])
    ],
    "temps": 4
}
