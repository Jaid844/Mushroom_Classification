import pandas
from file_operation.file_operation import file_op
from Preprocessing.Preprocessing_file import preprocess
from Prediction_validation.rawfile_validationprediction import prediction_validation
from Data.Dataloder import data
from log.applogger import Applogger
import pandas as pd



class predictfrom_model:

    def __init__(self,path):
        self.log=Applogger()
        self.p=preprocess()
        self.preprocess=prediction_validation(path)
        self.data=data()
        self.file=file_op()
    def predict(self):
        try:
            self.file_object = open("Prediction_Logs/Prediction_Log.txt", 'a+')
            self.p.deletePredictionFile()
            self.log.log(self.file_object, 'Start of Prediction')
            data=self.data.get()
            data.drop('veiltype',axis=1,inplace=True)
            #data=pd.DataFrame(data,columns=data.columns)
            #data.to_csv("'preprocessing_data/null_values3.csv", index=False)
           # data=self.p.randomer(data)
            is_null_present, cols_with_missing_values=self.p.null_present(data)
            if is_null_present:
                data=self.p.imputemissingvalue(data,cols_with_missing_values)
            data=self.p.encodeCategoricalValuesPrediction(data)
            #X_data = pd.DataFrame(data, columns=data.columns)
            #X_data.drop('veiltype_p',axis=1,inplace=True)
            #X_data.to_csv("'preprocessing_data/null_values2.csv", index=False)
            kmeans=self.file.load_model('KMeans')
            cluster=kmeans.predict(data)
            data['cluster']=cluster
            cluster=data['cluster'].unique()
            result=[]
            for i in cluster:
                 cluster_data = data[data['cluster'] == i]
                 cluster_data = cluster_data.drop(['cluster'], axis=1)
                 model_name = self.file.find_correct_model(i)
                 model=self.file.load_model(model_name)
                 result_from=model.predict(cluster_data)
                 for val in result_from:
                     if val==1:
                         result.append('e')
                     else:
                         result.append('p')
            result=pandas.DataFrame(result,columns=['Prediction'])
            path = "Prediction_Output_File/Predictions.csv"
            result.to_csv("Prediction_Output_File/Predictions.csv", header=True)
            self.log.log(self.file_object, 'End of Prediction')
        except Exception as ex:
            self.log.log(self.file_object, 'Error occured while running the prediction!! Error:: %s' % ex)
            raise ex
        return path









#c=predictfrom_model('path')
#c.predict()














