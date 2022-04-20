from contracts import *

###############################
## Define the Game contracts ##
###############################
valid_construction_card = new_contract('valid_construction_card', lambda c: (isinstance(c, list)
                                                                             and len(c) == 2
                                                                             and check('valid_natural', c[0])
                                                                             and check('valid_effect', c[1])))
valid_effect = new_contract('valid_effect', lambda s: (s == "surveyor"
                                                       or s == "agent"
                                                       or s == "landscaper"
                                                       or s == "pool"
                                                       or s == "temp"
                                                       or s == "bis"))
