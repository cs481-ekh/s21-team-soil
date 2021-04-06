class soil_object:
    """
    "dataFile"
    "liquidLimit"
    "plasticIndex"
    "clayPercent"
    "siltPercent"
    "sandPercent"
    "organicContent"
    "limeStabilize"
    "cementStabilize"
    "limeDose"
    "cementDose"
    "quantResult"
    "qualResult"
    """

    def __init__(self, dataFile, liquidLimit, plasticIndex, clayPercent, siltPercent, sandPercent, organicContent, limeStabilize, cementStabilize, limeDose, cementDose, quantResult, qualResult):
        self.dataFile = dataFile

        # Values needed for soil analysis
        self.liquidLimit = liquidLimit 
        self.plasticIndex = plasticIndex
        self.clayPercent = clayPercent
        self.siltPercent = siltPercent
        self.sandPercent = sandPercent
        self.organicContent = organicContent
        self.limeStabilize = limeStabilize
        self.cementStabilize = cementStabilize

        self.limeDose = limeDose
        self.cementDose = cementDose
        self.quantResult = quantResult
        self.qualResult = qualResult