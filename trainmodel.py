import pandas as pd
from raw.Rawfile import rawdata
from log.applogger import Applogger
from Dataingestion.Datafolder import Data
from Preprocessing.Preprocessing_file import preprocess
from Preprocessing.clustering import Cluster
from best_mode_finder.tuner import model_finder
from file_operation.file_operation import file_op
from sklearn.model_selection import  train_test_split



class training:
    def __init__(self):
        self.data=Data()
        self.preporocess=preprocess()
        self.file_op=file_op()
        self.model=model_finder()
        self.cluster=Cluster()
        self.log=Applogger()
        self.raw=rawdata('path')


    def train(self):
        try:
            self.file_object=open('Training_Logs/Training_Main_Log.txt','a+')
            self.raw.delete_modelfolder()
            data = self.data.datgetter()
            data=self.preporocess.dropUnnecessaryColumns(data,['veiltype'])
            #data=self.preporocess.replaceInvalidValuesWithNull(data)
            is_null_present, cols_with_missing_values=self.preporocess.null_present(data)
            if is_null_present:
                data=self.preporocess.imputemissingvalue(data,cols_with_missing_values)
            data=self.preporocess.encodeCategoricalValues(data)
            #data=self.preporocess.randomer(data)
            X,Y=self.preporocess.sepratelabelandfeature(data,columns='class')
            self.log.log(self.file_object,"X.shape before imb "+str(X.shape))
            data=self.preporocess.imb(X,Y)
            X, Y = self.preporocess.sepratelabelandfeature(data, columns='class')
            X_data=pd.DataFrame(X,columns=X.columns)
            X_data.to_csv("'preprocessing_data/null_values.csv",index=False)
            self.log.log(self.file_object, "X.shape after imb " + str(X.shape))
            number_of_cluster=self.cluster.elbowplot(X)
            X=self.cluster.create_cluster(X,number_of_cluster)
            X['Labels'] = Y
            list_of_clusters = X['Cluster'].unique()
            for i in list_of_clusters:
               cluster_data = X[X['Cluster'] == i]
               cluster_features = cluster_data.drop(['Labels', 'Cluster'], axis=1)
               cluster_label = cluster_data['Labels']
               x_train, x_test, y_train, y_test = train_test_split(cluster_features, cluster_label, shuffle=False,stratify=None,test_size=1/3,
                                                            random_state=45)
               best_model_name, best_model=self.model.get_best_model(x_train,y_train,x_test,y_test)
               save_model=self.file_op.save_model(best_model,best_model_name+str(i))
            self.log.log(self.file_object, 'Successful End of Training')
            self.file_object.close()

        except Exception as e:
           self.log.log(self.file_object,str(e))
           self.file_object.close()
           raise Exception





#c=training()
#c.train()












