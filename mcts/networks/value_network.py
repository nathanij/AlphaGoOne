import pytorch

class ValueNetwork:
    def __init__(self, weight_address):
        self.address_ = weight_address
        self.model_ = pytorch.load(self.address_)

    def refresh(self):
        self.model_ = pytorch.load(self.address_)

    
    