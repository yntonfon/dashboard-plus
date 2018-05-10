class UsecaseInput:
    def __init__(self, payload=None):
        self.payload = payload or {}

    def get_inputs(self):
        return self.payload
