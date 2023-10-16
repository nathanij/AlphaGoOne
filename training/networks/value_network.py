import pytorch

class ValueNetwork:
    # Network evaluates the probability of a white win from the given situation
    def __init__(self, weight_path: str):
        self.weight_path_ = weight_path
        self.model_ = pytorch.load(self.address_)  # TODO: correct method

    def refresh(self):
        self.model_ = pytorch.load(self.address_)

    