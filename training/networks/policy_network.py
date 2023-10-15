import pytorch

class PolicyNetwork:
    # specify current model weight locations
    def __init__(self, weight_path: str):
        self.weight_path_ = weight_path
        self.network_ = pytorch.load(weight_path)  # TODO: look up equivalent pytorch method

    def refresh(self):
        self.network_ = pytorch.load(self.weight_path_)

