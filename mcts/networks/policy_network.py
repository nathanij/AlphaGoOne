import numpy as np
import pytorch

class PolicyNetwork:
    # specify current model weight locations
    def __init__(self, weight_location):
        self.network_ = pytorch.load(weight_location)  # or equivalent function in pytorch

