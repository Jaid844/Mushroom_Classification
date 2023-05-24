from log.applogger import Applogger
import pandas as pd
from Dataingestion.Datafolder import Data
import random
import numpy as np
from imblearn.under_sampling import RandomUnderSampler
import os
from imblearn.under_sampling import ClusterCentroids


class preprocess:
    def __init__(self):
        self.log=Applogger()
        self.data=Data()


    def removecolumn(self,data,column):
        self.column=column
        self.data=data
        try:
            self.file = open('Training_Logs/Preprocess', 'w')
            usefuldata=self.data.drop(self.column,axis=1)
            self.log.log(self.file,"Column have been removed")
            self.file.close()
            return  usefuldata
        except Exception as e:
            self.file = open('Training_Logs/Preprocess', 'w')
            self.log.log(self.file,str(e))
            self.file.close()


    def sepratelabelandfeature(self, data, columns):
       self.data = data
       self.column = columns
       try:
           self.file = open('Training_Logs/Preprocess', 'w')
           self.X = self.data.drop(labels=self.column, axis=1)
           self.Y = self.data[self.column]
           self.log.log(self.file, "label and fetaure have been sent")
           self.file.close()
           return self.X, self.Y
       except Exception as e:
           self.file = open('Training_Logs/Preprocess', 'w')
           self.log.log(self.file, str(e))
           self.file.close()

    def dropUnnecessaryColumns(self, data, columnNameList):
        """


                                """
        data = data.drop(columnNameList, axis=1)
        return data


    def imputemissingvalue(self,data,col):
        self.data=data
        self.col=col
        try:
            self.file = open('Training_Logs/Preprocess', 'w')
           # imputer=SimpleImputer(strategy="most_frequent")
            for i in self.col:
                self.data[i].fillna(self.data[i].mode()[0], inplace=True)
            self.log.log(self.file,"Encoded succesfulyy")
            self.file.close()
            return self.data
        except Exception as e:
            self.file = open('Training_Logs/Preprocess', 'w')
            self.log.log(self.file,str(e))
            self.file.close()


    def null_present(self,data):
        self.data=data
        self.columns_with_missing_value=[]
        self.state=False
        self.cols=data.columns
        try:
             self.file = open('Training_Logs/Preprocess', 'w')
             self.null_count=self.data.isna().sum()
             for i in range(len(self.null_count)):
                 if self.null_count[i]>0:
                     self.state=True
                     self.columns_with_missing_value.append(self.cols[i])
             self.log.log(self.file,"Sent the file of missing value , and the state")
             self.file.close()
             return self.state,self.columns_with_missing_value
        except Exception as e:
            self.file = open('Training_Logs/Preprocess', 'w')
            self.log.log(self.file,str(e))
            self.file.close()



    def replaceInvalidValuesWithNull(self,data):

        for column in data.columns:
            count = data[column][data[column] == '?'].count()
            if count != 0:
                data[column] = data[column].replace('?', np.nan)
        return data


    def encodeCategoricalValues(self,data):

        data["class"] = data["class"].map({'p': 1, 'e': 2})

        for column in data.drop(['class'],axis=1).columns:
               data = pd.get_dummies(data, columns=[column])

        return data

    def encodeCategoricalValuesPrediction(self,data):


        for column in data.columns:
            data = pd.get_dummies(data, columns=[column])

        return data

    def imb(self,X,Y):
        rus = RandomUnderSampler(random_state=42)
        X_resampled, y_resampled = rus.fit_resample(X, Y)
        balanced_data = pd.concat([X_resampled, y_resampled], axis=1)
        target_column = balanced_data['class'].tolist()
        random.shuffle(target_column)
        balanced_data['class'] = target_column
        return balanced_data

    def deletePredictionFile(self):

        if os.path.exists('Prediction_Output_File/Predictions.csv'):
            os.remove('Prediction_Output_File/Predictions.csv')



    def randomer(self,data):
        for columns in data.columns:
            column_data=data[columns]
            randomized_data = column_data.sample(frac=1, random_state=42)
            data[columns]=randomized_data.values
        return data



