
class soil_object:
    """dataFile
    liquidLimit
    plasticIndex
    clayPercent
    siltPercent
    sandPercent
    organicContent
    limeCementStabilize
    limeCementDose
    quantResult - boolean
    qualResult - boolean """

    def __init__(self, dataFile, liquidLimit, plasticIndex, clayPercent, siltPercent, sandPercent,
                organicContent, limeCementStabilize, limeCementDose, quantResult, qualResult):
        self.dataFile = dataFile

        # Values needed for soil analysis
        self.liquidLimit = liquidLimit 
        self.plasticIndex = plasticIndex
        self.clayPercent = clayPercent
        self.siltPercent = siltPercent
        self.sandPercent = sandPercent
        self.organicContent = organicContent
        self.limeCementStabilize = limeCementStabilize


        self.limeCementDose = limeCementDose
        self.quantResult = quantResult
        self.qualResult = qualResult