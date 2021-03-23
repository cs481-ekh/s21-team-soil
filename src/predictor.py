import numpy as np
import sklearn.svm

import rpy2
import rpy2.robjects
import rpy2.robjects.packages

class predictor():
    def __init__(self):


    def compute_lime_classification(soil_sample):
        # get the model from the saved R file
        AMIT_MODEL = saved_model_file
        # What will this object look like? What fields will it have? Will it match the json fields?


        # Get all the values of the soil sample loaded into a rpy2 object. The values from the soil sample
        # will have to be loaded into some kind of rpy2 object array. This is just example code of what that
        # will look like. Will need to actually find out how to get values into rpy2 array.
        
        # AMIT_MODEL will have these saved fields: x_train, y_train, cost=1.0, epsilon=0.1, gamma=0.01, scale=False
        #
        # x_test will come from the input to the function
        #
        # These will be used in the lines below

        # Might need to create an array of values based around soil_sample fields for np.array.

        # If the data was loaded from file, then use the 'dataFile' field for analysis. If not, use individually input values
        if soil_sample.data_file is not None:
            # What would 'x_test' be in this case? liquitLimit? plasticIndex? clayPercent? sandPercent? organicContent?
            # How would you get this field from the object loaded from file? Can we expect it to have the same fields as the json object?
            #   > Followup question: what do the files being uploaded by field engineers look like?
            SAMPLE_VALUES = rpy2.robjects.r['matrix'](rpy2.robjects.FloatVector(np.array(soil_sample.data_file.organicContent).T.flatten()), nrow = len(soil_sample.data_file.organicContent))
        else:
            # What would 'x_test' be in this case? liquitLimit? plasticIndex? clayPercent? sandPercent? organicContent?
            SAMPLE_VALUES = rpy2.robjects.r['matrix'](rpy2.robjects.FloatVector(np.array(soil_sample.organicContent).T.flatten()), nrow = len(soil_sample.organicContent))

        # run SVM
        predict = rpy2.robjects.r['predict']
        

        soil_pred = np.array(predict(AMIT_MODEL, SAMPLE_VALUES))
        return soil_pred


    def compute_lime_regression(soil_sample):

    def compute_cement_classification(soil_sample):

    def compute_cement_regression(soil_sample):        
