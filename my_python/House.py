import sys

sys.path.append('../../')
from my_python.exceptions import InvalidPlayerState
from my_python.contracts import house_contract
from my_python.Fence import Fence
from my_python.Same import Same
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
        self.is_roundabout = False
        self.is_bis = False
        self.num = -1  # self.num == -1 if house is not built
        self.is_built = False
        self.used_in_plan = used_in_plan
        self.l_fence: Fence = l_fence
        self.r_fence: Fence = r_fence
        if type(inp_house) == list:  # Case: House is a bis
            self.is_bis = True
            self.num = inp_house[0]
        elif type(inp_house) == int:  # Case: House is not a bis and built
            self.is_bis = False
            self.num = inp_house
        else:  # Case: Else, House is not built or is a roundabout
            if inp_house == "roundabout":
                self.is_roundabout = True
            self.is_bis = False
            self.num = -1
        self.is_built = self.num != -1
        ## Check: house cannot be built and used in plan
        self._check_built_used_in_plan()
        ## ===================== If class fields are specified, set them directly ====================
        try:
            self.is_bis = kwargs["d_is_bis"]
            self.num = kwargs["d_num"]  # self.num == -1 if house is not built
            self.is_built = kwargs["d_is_built"]
            self.used_in_plan = kwargs["d_used_in_plan"]
            self.l_fence = kwargs["d_l_fence"]
            self.r_fence = kwargs["d_r_fence"]
        except KeyError:
            pass

    def _check_built_used_in_plan(self) -> None:
        # Add first condition bc when subtracting, we initialize a PlayerState with fields that are Same,
        #   which fails the second condition of this if.
        if (not (type(self.is_built) == Same or type(self.used_in_plan) == Same)) \
                and (not self.is_built) and self.used_in_plan:
            raise InvalidPlayerState("House cannot be built and used in plan.")

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
        ret = House(d_is_bis=same_or_get_first(self.is_bis, other.is_bis),
                    d_num=same_or_get_first(self.num, other.num),
                    d_is_built=same_or_get_first(self.is_built, other.is_built),
                    d_used_in_plan=same_or_get_first(self.used_in_plan, other.used_in_plan),
                    d_l_fence=same_or_get_first(self.l_fence, other.l_fence),
                    d_r_fence=same_or_get_first(self.r_fence, other.r_fence))
        return ret

    def return_literal(self):
        if not self.is_built:
            if not self.is_roundabout:   # Not built and not roundabout
                return "blank"
            else:
                return "roundabout"
        elif not self.is_bis:           # House is built -> not a bis -> print normal house
            return self.num
        else:                           # House is built -> is a bis -> print bis house
            return [self.num, "bis"]

    def __str__(self):
        return str(self.return_literal())
