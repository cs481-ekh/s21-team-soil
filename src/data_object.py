class Soil_Object:
    dataFile
    liquidLimit
    plasticIndex
    clayPercent
    siltPercent
    sandPercent
    organicContent
    limeCementStabilize
    limeCementDose
    quantResult
    qualResult

    def __init__(self, dataFile, liquidLimit, plasticIndex, clayPercent, siltPercent, sandPercent, organicContent, limeCementStabilize, limeCementDose, quantResult, qualResult):
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

    def setDataFile(data):
        dataFile = data
        return dataFile

    def getDataFile():

        return dataFile


    def setLiquidLimit(ll):
        liquidLimit = ll
        return liquidLimit

    def getLiquidLimit():

        return liquidLimit


    def setPlasticIndex(pl):
        plasticIndex = pl
        return plasticIndex

    def getPlasticIndex():

        return plasticIndex


    def setClayPercent(cp):
        clayPercent = cp
        return clayPercent

    def getClayPercent():

        return clayPercent


    def setSandPercent(sp):
        sandPercent = sp
        return sandPercent

    def getSandPercent():

        return sandPercent


    def setOrganicContent(oc):
        organicContent = oc
        return organicContent

    def getOrganicContent():

        return organicContent


    def setLimeCementStabilize(lcs):
        limeCementStabilize = lcs
        return limeCementStabilize

    def getLimeCementStabilize():

        return limeCementStabilize


    def setLimeCementDose(lcd):
        limeCementDose = lcd
        return limeCementDose

    def getLimeCementDose():

        return limeCementDose


    def setQuantResult(quantr):
        quantResult = quantr
        return quantResult

    def getQuantResult():

        return quantResult


    def setQualResult(qualr):
        qualResult = qualr
        return qualResult

    def getQualResult():

        return qualResult