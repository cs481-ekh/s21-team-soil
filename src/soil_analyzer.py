import rpy2
import rpy2.robjects
import rpy2.robjects.packages
import numpy as np
from data_object import soil_object
from enum import Enum

class model_type(Enum):
    svm = 1
    mlr = 2
    lda = 3

class soil_analyzer():
    
    def __init__(self):
        # Instantiating SVM Radial Kernel Regression model for Lime Regression
        self.utils_lr = rpy2.robjects.packages.importr('e1071')
        svm_rad_regression = "svm_lime_regression.rds"
        rpy2.robjects.r(f"lime_reg <- readRDS('{svm_rad_regression}')")
        self.lime_regression_model = rpy2.robjects.r["lime_reg"]

        # Instantiating _ model for Lime Classification
        svm_rad_class = "svm_lime_classification.rds"
        rpy2.robjects.r(f"lime_class <- readRDS('{svm_rad_class}')")
        self.lime_classification_model = rpy2.robjects.r["lime_class"]

        # Instantiating MLR model for Cement Regression
        mlr_model = "mlr_cement_regression.rds"
        rpy2.robjects.r(f"cement_regression <- readRDS('{mlr_model}')")
        self.cement_regression_model = rpy2.robjects.r["cement_regression"]

        # Instantiating LDA model for Cement Classification
        self.utils_cc = rpy2.robjects.packages.importr('MASS')
        lda_model = "lda_cement_classification.rds"
        rpy2.robjects.r(f"cement_classification <- readRDS('{lda_model}')")
        self.cement_classification_model = rpy2.robjects.r["cement_classification"]

    def get_rmatrix(self, soil_sample, model_t):
        """Returns a R matrix formatted for use with all four soil analysis methods. Returns a properly formatted
        R-object for the given model_type.
        Args:
            soil_sample (soil_object): A soil_object with values for exactly one soil sample

        Returns:
            rpy2.robjects: R matrix object for use with rpy2 library
        """
        # Pull values from soil_sample into one array
        soil_values = np.array([soil_sample.liquidLimit, soil_sample.plasticIndex, soil_sample.clayPercent, soil_sample.siltPercent, soil_sample.sandPercent, soil_sample.organicContent, soil_sample.stabilizer])

        # Turn numpy array into R-matrix
        r_matrix = rpy2.robjects.r['matrix'](rpy2.robjects.FloatVector(soil_values), nrow=1)
        
        if model_t is model_type.mlr:
            r_matrix = rpy2.robjects.r('data.frame')(r_matrix)
        
        
        # Setting column names for R-matrix for use with models.
        if model_t is model_type.svm:
            feature_names = ['x.LL', 'x.PI', 'x.Clay', 'x.Silt', 'x.Sand', 'x.Organic.Content', 'x.Stabilizer']
        else:
            feature_names = ["LL", "PI", "Clay", "Silt", "Sand", "Organic.Content", "Stabilizer"]

            
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
        sample_values = self.get_rmatrix(soil_sample, model_type.svm)

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
        sample_values = self.get_rmatrix(soil_sample, model_type.svm)

        predict = rpy2.robjects.r['predict']
        
        factor_vector = predict(self.lime_classification_model, sample_values)
        pred = int(factor_vector.levels[factor_vector[0] - 1])
        
        # Transcribed from Amit's code
        if pred < 0:
            return 0
        return pred

    def cement_regression(self, soil_sample):
        # MLR model
        sample_values = self.get_rmatrix(soil_sample, model_type.mlr)
        predict = rpy2.robjects.r['predict']
        r_pred = np.array(predict(self.cement_regression_model, sample_values))

        return r_pred[0]

    def cement_classification(self, soil_sample):
        # LDA
        sample_values = self.get_rmatrix(soil_sample, model_type.mlr)
        predict = rpy2.robjects.r['predict']
        r_pred = predict(self.cement_classification_model, sample_values)
        factor_vector = r_pred[0]
        
        # Get item from R vector labels. Switch between R indexing(starts at 1) and Python indexing(starts at 0)
        pred = int(factor_vector.levels[factor_vector[0] - 1])
        
        # Return pass or fail class (0 or 1)
        return pred
