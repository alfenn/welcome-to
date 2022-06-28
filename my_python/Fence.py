
class Fence:
    def __init__(self, exists: bool):
        self.exists = exists

    def __eq__(self, other):
        return self.exists == other.exists

    def __str__(self):
        return self.exists
