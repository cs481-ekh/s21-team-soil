class soil_object:
    """
    "dataFile"
    "liquidLimit"
    "plasticIndex"
    "clayPercent"
    "siltPercent"
    "sandPercent"
    "organicContent"
    "stabilizer"
    "limeDose"
    "cementDose"
    "quantResult"
    "qualResult"
    """

    def __init__(self, dataFile, liquidLimit, plasticIndex, clayPercent, siltPercent, sandPercent, organicContent, stabilizer, limeDose, cementDose, quantResult, qualResult):
        self.dataFile = dataFile

        # Values needed for soil analysis
        self.liquidLimit = liquidLimit 
        self.plasticIndex = plasticIndex
        self.clayPercent = clayPercent
        self.siltPercent = siltPercent
        self.sandPercent = sandPercent
        self.organicContent = organicContent
        self.stabilizer = stabilizer

        self.limeDose = limeDose
        self.cementDose = cementDose
        self.quantResult = quantResult
        self.qualResult = qualResult