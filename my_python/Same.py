
class Same:
    def __init__(self):
        pass

    def __eq__(self, other):
        return True


def same_or_get_first(obj1, obj2):
    if obj1 == obj2: return Same()
    return obj1
