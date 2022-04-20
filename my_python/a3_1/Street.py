from contracts import *
from Homes import *

class Street:
    @contract
    def __init__(self, st):
        """
            Initialize street object.

            :param st: Dictionary input representing a street
            :type st: valid_street
        """
        self.homes = Homes(st.get("homes"))
        self.parks = st.get("parks")
        self.pools = st.get("pools")

    @contract
    def get_parks(self):
        """
            Get the number of parks in the street

            :type: None

            :return: A natural representing the number of parks
            :rtype: valid_parks
        """
        return self.parks

    @contract
    def get_pools(self):
        """
            Get the number of "active" pools in the street

            :type: None

            :return: List of Booleans representing which pools are "activated"
            :rtype: valid_pools
        """
        return self.pools
