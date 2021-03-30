import rpy2
import rpy2.robjects
import rpy2.robjects.packages
import numpy as np
from data_object import soil_object

class soil_analyzer():
    
    def __init__(self):

        # Instantiating SVM Radial Kernel Regression model for Lime Regression
        self.utils_lr = rpy2.robjects.packages.importr('e1071')
        svm_rad_regression = "svm_lime_regression.rds"
        rpy2.robjects.r(f"lime_reg <- readRDS('{svm_rad_regression}')")
        self.lime_regression_model = rpy2.robjects.r["lime_reg"]
        # =============================================================

        # Instantiating _ model for Lime Classification
        svm_rad_class = "svm_lime_classification.rds"
        rpy2.robjects.r(f"lime_class <- readRDS('{svm_rad_class}')")
        self.lime_classification_model = rpy2.robjects.r["lime_class"]
        # =============================================================

        # Instantiating _ model for Cement Regression
        
        # =============================================================

        # Instantiating _ model for Cement Classification

        # =============================================================


    def get_rmatrix(self, soil_sample):
        """Returns a R matrix formatted for use with all four soil analysis methods. 
        Args:
            soil_sample (soil_object): A soil_object with values for exactly one soil sample

        Returns:
            rpy2.robjects: R matrix object for use with rpy2 library
        """
        # TODO: Ask Amit for proper raster data to get std and mean for preprocessing of data
        
        # Pull values from soil_sample into one array
        soil_values = np.array([soil_sample.liquidLimit, soil_sample.plasticIndex, soil_sample.clayPercent, soil_sample.siltPercent, soil_sample.sandPercent, soil_sample.organicContent, soil_sample.limeCementStabilize])

        # Turn numpy array into R-matrix
        r_matrix = rpy2.robjects.r['matrix'](rpy2.robjects.FloatVector(soil_values), nrow=1)

        # Setting column names for R-matrix for use with models. Model predict function will NOT work unless this is done. 
        feature_names = ['x.LL', 'x.PI', 'x.Clay', 'x.Silt', 'x.Sand', 'x.Organic.Content', 'x.Stabilizer']
        r_matrix.colnames = rpy2.robjects.vectors.StrVector(feature_names)

        return r_matrix

    def lime_regression(self, soil_sample):
        """Computes lime regression analysis for given soil sample.
        Utilizes a pretrained SVM Radial Kernel Regression model for prediction.

        Args:
            soil_sample (soil_object): A soil_object with values for exactly one soil sample

        Returns:
            float: Returns lime_regression value
        """
        # Convert soil_sample to R-matrix object
        sample_values = self.get_rmatrix(soil_sample)

        predict = rpy2.robjects.r['predict']
        r_pred = np.array(predict(self.lime_regression_model, sample_values))

        if r_pred[0] < 0: return 0

        return r_pred[0]
    
    def lime_classification(self, soil_sample): 
        """Computes lime classification analysis for given soil sample.
        Utilizes a pretrained SVM Radial Kernel Classifier model for prediction.

        Args:
            soil_sample (soil_object): A soil_object with values for exactly one soil sample

        Returns:
            float: Returns lime_classification class
        """
        # Convert soil_sample to R-matrix object
        sample_values = self.get_rmatrix(soil_sample)

        predict = rpy2.robjects.r['predict']
        r_pred = np.array(predict(self.lime_classification_model, sample_values))

        # TODO: Ask Amit what classes correspond to what output values from SVM classifier.
        if r_pred[0] < 0: return 0

        return r_pred[0]

    def cement_regression(self, soil_sample):
        return None

    def cement_classification(self, soil_sample):
        return None
