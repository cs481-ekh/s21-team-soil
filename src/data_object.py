
"""

"""
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
    quantResult
    qualResult"""

    def __init__(self, dataFile, liquidLimit, plasticIndex, clayPercent, siltPercent, sandPercent,
                organicContent, limeCementStabilize, limeCementDose, quantResult, qualResult):
        self.dataFile = dataFile
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

    def setDataFile(self, data):
        self.dataFile = data
        return self.dataFile

    def getDataFile(self):

        return self.dataFile


    def setLiquidLimit(self, ll):
        self.liquidLimit = ll
        return self.liquidLimit

    def getLiquidLimit(self):

        return self.liquidLimit


    def setPlasticIndex(self, pl):
        self.plasticIndex = pl
        return self.plasticIndex

    def getPlasticIndex(self):

        return self.plasticIndex


    def setClayPercent(self, cp):
        self.clayPercent = cp
        return self.clayPercent

    def getClayPercent(self):

        return self.clayPercent


    def setSandPercent(self, sp):
        self.sandPercent = sp
        return self.sandPercent

    def getSandPercent(self):

        return self.sandPercent


    def setOrganicContent(self, oc):
        self.organicContent = oc
        return self.organicContent

    def getOrganicContent(self):

        return self.organicContent


    def setLimeCementStabilize(self, lcs):
        self.limeCementStabilize = lcs
        return self.limeCementStabilize

    def getLimeCementStabilize(self):

        return self.limeCementStabilize


    def setLimeCementDose(self, lcd):
        self.limeCementDose = lcd
        return self.limeCementDose

    def getLimeCementDose(self):

        return self.limeCementDose


    def setQuantResult(self, quantr):
        self.quantResult = quantr
        return self.quantResult

    def getQuantResult(self):

        return self.quantResult


    def setQualResult(self, qualr):
        self.qualResult = qualr
        return self.qualResult

    def getQualResult(self):

        return self.qualResult
