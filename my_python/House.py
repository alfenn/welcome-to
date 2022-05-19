import sys
sys.path.append('../../')
from my_python.exceptions import InvalidPlayerState
from my_python.contracts import house_contract
from my_python.Fence import Fence
from my_python.Same import same_or_get_first

class House:
    # def __init__(self, inp_house, used_in_plan: bool, l_fence: Fence, r_fence: Fence):
    def __init__(self, **kwargs):
        """House constructor is responsible for validating only inp_house
        input."""
        ## ===================== Standard input ====================
        ### If these arguments are not specified, initialize values to valid
        ### placeholders. This is to pass the validators in the case that we
        ### are setting the class fields directly.
        inp_house = kwargs.get("inp_house", "blank")
        used_in_plan = kwargs.get("used_in_plan", False)
        l_fence = kwargs.get("l_fence", Fence(False))
        r_fence = kwargs.get("r_fence", Fence(False))
        if not house_contract(inp_house): raise InvalidPlayerState("Breaks House contract")
        ### Normal processing of standard inputs.
        self.is_bis = False
        self.num = -1                       # self.num == -1 if house is not built
        self.is_built = False
        self.used_in_plan = used_in_plan
        self.l_fence = l_fence
        self.r_fence = r_fence

        if type(inp_house) == list:         # Case: House is a bis
            self.is_bis = True
            self.num = inp_house[0]
        elif type(inp_house) == int:        # Case: House is not a bis and built
            self.is_bis = False
            self.num = inp_house
        else:                               # Case: Else, House is not a bis and not built
            self.is_bis = False
            self.num = -1
        self.is_built = self.num != -1
        ## ===================== If class fields are specified, set them directly ====================
        try:
            self.is_bis = kwargs["is_bis"]
            self.num = kwargs["num"]  # self.num == -1 if house is not built
            self.is_built = kwargs["is_built"]
            self.used_in_plan = kwargs["used_in_plan"]
            self.l_fence = kwargs["l_fence"]
            self.r_fence = kwargs["r_fence"]
        except KeyError:
            pass

    def load(self):
        """Load the House object into a basic Python type that
        can be converted to a JSON string using json.dumps().

        Note: Only "house" schema is loaded.
        """
        if self.num == -1: return "blank"               # Case: House is not built
        if self.is_bis: return [self.num, "bis"]        # Case: House is a bis
        return self.num                                 # Case: House is not a bis and built

    def __eq__(self, other):
        if type(other) == House:
            return self.is_bis == other.is_bis \
                    and self.num == other.num \
                    and self.is_built == other.is_built \
                    and self.used_in_plan == other.used_in_plan \
                    and self.l_fence == other.l_fence \
                    and self.r_fence == other.r_fence
        return False

    def __sub__(self, other):
        ret = House(is_bis=same_or_get_first(self.is_bis, other.is_bis),
                    num=same_or_get_first(self.num, other.num),
                    is_built=same_or_get_first(self.is_built, other.is_built),
                    used_in_plan=same_or_get_first(self.used_in_plan, other.used_in_plan),
                    l_fence=same_or_get_first(self.l_fence, other.l_fence),
                    r_fence=same_or_get_first(self.r_fence, other.r_fence))
        return ret

