import json
from contracts import *

class PlayerState:
    @contract
    def __init__(self, ps):
        """
            Initialize Player state from a valid player state dictionary.

            :param ps: The dictionary representing the input state
            :type ps: valid_player_state
        """
        self.agents = ps.get("agents")
        self.city_plan_score = ps.get("city-plan-score")
        self.refusals = ps.get("refusals")
        self.streets = []
        for elem in streets:
            self.streets += Street(elem)
        self.temps = ps.get("temps")

        assert streets[0]

    @contract
    def get_agents(self):
        """
            Gets the 'agents' field of the player state.

            :type: None

            :return: List representing agents
            :rtype: valid_agents
        """
        return self.agents

    @contract
    def get_city_plan_score(self):
        """
            Gets the 'city_plan_score' of the player state.

            :type: None

            :return: List representing the city_plan_scores
            :rtype: valid_city_plan_score
        """
        return self.city_plan_score

    @contract
    def get_refusals(self):
        """
            Gets the 'refusals' of the player state.

            :type: None

            :return: Natural
            :rtype: valid_refusals
        """
        return self.refusals

    @contract
    def get_streets(self):
        """
            Gets the 'streets' of the player state.

            :type: None

            :return: List representing the number of streets
            :rtype: valid_streets
        """
        return self.streets

    @contract
    def get_street1(self):
        """
            Gets the first street of the player state.

            :type: None

            :return: Dictionary representing
        :return:
        """

    @contract
    def get_street2(self):
        """
            Gets the second street of the player state.
            
            :type: None
            
            :return: Dictionary representing everything on a street.
            :rtype:
        """

    @contract
    def get_temps(self):
        """
            Returns the 'temps' field of the player state.

            :type: None

            :return: Number representing the number of temps a player has used.
            :rtype: valid_temps
        """
        return self.temps
