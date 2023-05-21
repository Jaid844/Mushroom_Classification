from os import listdir
from log.applogger import Applogger
import pandas as pd


class dataTransform:
    """
              This class shall be used for transforming the Good Raw Training Data before loading it in Database!!.

              Written By: iNeuron Intelligence
              Version: 1.0
              Revisions: None

              """

    def __init__(self):
        self.goodDataPath = "Trainingfiles/Good_file"
        self.logger = Applogger()
    def replace(self):
        log_file = open("Training_Logs/addQuotesToStringValuesInColumn.txt", 'a+')
        try:
            onlyfiles = [f for f in listdir(self.goodDataPath)]
            for file in onlyfiles:
                data = pd.read_csv(self.goodDataPath + "/" + file)
                for column in data.columns:
                   count = data[column][data[column] == '?'].count()
                   if count != 0:
                       data[column] = data[column].replace('?', "'?'")
                   data.to_csv(self.goodDataPath + "/" + file, index=None, header=True)
                   self.logger.log(log_file, " %s: Quotes added successfully!!" % file)
        except Exception as e:
            self.logger.log(log_file, "Data Transformation failed because:: %s" % e)
            # log_file.write("Current Date :: %s" %date +"\t" +"Current time:: %s" % current_time + "\t \t" + "Data Transformation failed because:: %s" % e + "\n")
            log_file.close()
        log_file.close()


