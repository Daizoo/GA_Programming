class GA_Settings:
    # 遺伝子長
    genomLength = None
    # 一世代あたりの個体数
    population = None
    # 一世代あたりの最大交換数
    maxChange = None
    # 各遺伝子ごとの突然変異確率
    perMutation_G = None
    # 各個体ごとの突然変異確率
    perMutation_I = None
    # ループの回数
    roopCount = None

    def __init__(self, genomLength, population, maxChange, perMutation_G,
                 perMutation_I, roopCount):
        self.genomLength = genomLength
        self.population = population
        self.maxChange = maxChange
        self.perMutation_G = perMutation_G
        self.perMutation_I = perMutation_I
        self.roopCount = roopCount
