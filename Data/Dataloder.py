from log.applogger import Applogger
import pandas as pd




class data:

    def __init__(self):
        self.log=Applogger()
        self.data_file='Predictionfile_db/Inputfile.csv'



    def get(self):
        try:
            self.file = open('Prediction_Logs/data.txt', 'w')
            csv=pd.read_csv(self.data_file)
            self.log.log(self.file,"File have been sent")
            self.file.close()
            return csv
        except Exception as e:
            self.file = open('Prediction_Logs/data', 'w')
            self.log.log(self.file,str(e))
            self.file.close()

