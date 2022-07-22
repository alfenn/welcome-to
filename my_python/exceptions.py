
###################################################################################
#### Define exceptions to be raised with messages for the three invalid states ####
###################################################################################

class InvalidPlayerState(Exception):
    def __init__(self, m:str):
        super().__init__(m)

class InvalidGameState(Exception):
    def __init__(self, m:str):
        super().__init__(m)

class InvalidMove(Exception):
    def __init__(self, m:str):
        super().__init__(m)

class NetworkDisconnect(Exception):
    def __init__(self, m:str):
        super().__init__(m)
