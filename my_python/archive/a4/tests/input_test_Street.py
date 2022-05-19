import sys
sys.path.append('../../../../')
from my_python.Same import Same
from my_python.House import House

valid_num_houses1 = {
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
}

valid_num_houses2 = {
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

invalid_num_houses1 = {
    "homes": ["blank", False,
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 0,
    "pools": [False, False, False]
}

invalid_num_houses2 = {
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
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 0,
    "pools": [False, False, False]
}

valid_parks1 = {
    "homes": ["blank", False,
          [False, 1, False],
          [False, "blank", False],
          [False, 2, False],
          [False, 3, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 3,
    "pools": [False, False, False]
}

valid_parks2 = {
    "homes": ["blank", False,
          [False, 1, False],
          [False, 2, False],
          [False, 3, False],
          [False, 4, False],
          [False, [4, "bis"], False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 4,
    "pools": [False, False, False]
}

valid_parks3 = {
    "homes": ["blank", False,
          [False, 3, False],
          [False, 4, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, 6, False],
          [False, 7, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, 10, False],
          [False, 11, False]],
    "parks": 5,
    "pools": [False, False, False]
}

valid_parks4 = {
    "homes": ["blank", False,
          [False, 3, False],
          [False, 4, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, 6, False],
          [False, 7, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, 10, False],
          [False, 11, False]],
    "parks": 2,
    "pools": [False, False, False]
}

invalid_parks1 = {
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
    "parks": 4,
    "pools": [False, False, False]
}

invalid_parks2 = {
    "homes": ["blank", False,
          [False, 3, False],
          [False, [3, "bis"], False],
          [False, [3, "bis"], False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 5,
    "pools": [False, False, False]
}

invalid_parks3 = {
    "homes": ["blank", False,
          [False, 3, False],
          [False, [3, "bis"], False],
          [False, [3, "bis"], False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False]],
    "parks": -10,
    "pools": [False, False, False]
}

pool_0_1_valid = {
    "homes": ["blank", False,
          [False, "blank", False],
          [False, 1, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 0,
    "pools": [True, False, False]
}

pool_0_1_invalid = {
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
    "pools": [True, False, False]
}

pool_0_1_invalid_bis = {
    "homes": ["blank", False,
          [False, "blank", False],
          [False, [1, "bis"], False],
          [False, 1, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 0,
    "pools": [True, False, False]
}

pool_2_2_valid = {
    "homes": ["blank", False,
              [False, "blank", False],
              [False, [1, "bis"], False],
              [False, 1, False],
              [False, "blank", False],
              [False, "blank", False],
              [False, 2, False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False]],
    "parks": 0,
    "pools": [False, True, False]
}

pool_2_2_invalid = {
    "homes": ["blank", False,
              [False, "blank", False],
              [False, [1, "bis"], False],
              [False, 1, False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False]],
    "parks": 0,
    "pools": [False, True, False]
}

pool_1_3_valid = {
    "homes": [1, False,
              [False, "blank", False],
              [False, "blank", False],
              [False, 2, False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, 3, False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False]],
    "parks": 0,
    "pools": [True, True, True]
}

pool_1_3_invalid = {
    "homes": ["blank", False,
              [False, 1, False],
              [False, 2, False],
              [False, "blank", False],
              [False, 3, False],
              [False, 4, False],
              [False, 5, False],
              [False, "blank", False],
              [False, 6, False],
              [False, 7, False],
              [False, 8, False]],
    "parks": 0,
    "pools": [True, True, True]
}

num_estates_0_valid = {
    "homes": ["blank", False,
          [False, "blank", False],
          [True, 1, False],
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

num_estates_0_1_valid = {
    "homes": ["blank", False,
          [False, "blank", False],
          [True, 1, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, 2, True]],
    "parks": 0,
    "pools": [False, False, False]
}

num_estates_1_valid = {
    "homes": ["blank", False,
          [False, "blank", False],
          [True, 1, False],
          [False, "blank", False],
          [False, 2, False],
          [True, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [True, 3, False]],
    "parks": 0,
    "pools": [False, False, False]
}

num_estates_2_valid = {
    "homes": ["blank", False,
          [False, "blank", False],
          [True, 1, False],
          [False, 2, False],
          [False, 3, False],
          [True, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [True, 4, False]],
    "parks": 0,
    "pools": [False, False, False]
}

num_estates_3_valid = {
    "homes": ["blank", False,
          [False, "blank", False],
          [True, 1, False],
          [True, 2, False],
          [False, 3, False],
          [True, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [True, 4, False]],
    "parks": 0,
    "pools": [False, False, False]
}

num_estates_46_valid = {
    "homes": [1, False,
          [False, 2, False],
          [False, 3, False],
          [False, 4, False],
          [True, 5, False],
          [False, 6, False],
          [False, 7, False],
          [False, 8, False],
          [False, 9, False],
          [False, 10, False]],
    "parks": 0,
    "pools": [False, False, False]
}

num_estates_0_2_valid = {
    "homes": [1, False,
          [False, 2, False],
          [False, 3, False],
          [False, 4, False],
          [False, 5, False],
          [False, 6, False],
          [False, 7, False],
          [False, 8, False],
          [False, 9, False],
          [False, 10, False]],
    "parks": 0,
    "pools": [False, False, False]
}


same_house = House(is_bis=Same(),
                   num=Same(),
                   is_built=Same(),
                   used_in_plan=Same(),
                   l_fence=Same(),
                   r_fence=Same())

all_same_street_len10 = {
    "homes": [same_house for i in range(10)],
    "parks": Same(),
    "pools": [Same() for i in range(3)]
}

all_same_street_len11 = {
    "homes": [same_house for i in range(11)],
    "parks": Same(),
    "pools": [Same() for i in range(3)]
}

all_same_street_len12 = {
    "homes": [same_house for i in range(12)],
    "parks": Same(),
    "pools": [Same() for i in range(3)]
}

valid_num_houses1_2 = {
    "homes": ["blank", False,
          [False, 1, False],
          [False, [1, "bis"], False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 1,
    "pools": [False, False, False]
}


