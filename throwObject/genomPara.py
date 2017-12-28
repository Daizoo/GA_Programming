class genom:

    genom_data = None
    evaluation = None

    def __init__(self, genom_data, evaluation):
        self.genom_data = genom_data
        self.evaluation = evaluation

    def getData(self):
        return self.genom_data

    def getEval(self):
        return self.evaluation

    def setData(self, genom_data):
        self.genom_data = genom_data

    def setEval(self, evaluation):
        self.evaluation = evaluation
