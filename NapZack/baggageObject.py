class baggage:

    weight = None
    value = None

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def getWeight(self):
        return self.weight

    def getValue(self):
        return self.value
