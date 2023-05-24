from Prediction_validation.rawfile_validationprediction import prediction_validation
from Prediction_database.Prediction_database import db
from log.applogger import Applogger


class Pred:
    def __init__(self,path):
        self.raw=prediction_validation(path)
        self.log=Applogger()
        self.db=db()

    def predic(self):
        try:
            self.file_object = open("Prediction_Logs/Prediction_Log.txt", 'a+')
            self.log.log(self.file_object, 'Start of Validation on files for prediction!!')
            Length_of_time, length_of_date, num_col, col_name = self.raw.valuesfrom_schema()
            regex = self.raw.manualRegexCreation()
            self.raw.validatefilename(regex, Length_of_time, length_of_date)
            self.raw.valiadtecolumn(num_col)
            self.raw.missingvalue()
            self.log.log(self.file_object, "Raw Data Validation Complete!!")
            self.log.log(self.file_object, "DataTransformation Complete")
            self.log.log(self.file_object, "Creating Prediction_Database and tables on the basis of given schema!!!")
            self.db.table_create(col_name)
            self.log.log(self.file_object, "Table creation Completed!!")
            self.log.log(self.file_object, "Insertion of Data into Table started!!!!")
            self.db.adding_data(col_name)
            self.log.log(self.file_object, "Insertion in Table completed!!!")
            self.log.log(self.file_object, "Deleting Good Data Folder!!!")
            self.raw.delete_goodfolder()
            self.log.log(self.file_object, "Good_Data folder deleted!!!")
            self.log.log(self.file_object, "Moving bad files to Archive and deleting Bad_Data folder!!!")
            self.raw.move_archive()
            self.log.log(self.file_object, "Bad files moved to archive!! Bad folder Deleted!!")
            self.log.log(self.file_object, "Validation Operation completed!!")
            self.log.log(self.file_object, "Extracting csv file from table")
            self.db.filefromdb()
            #self.file_object.close()

        except Exception as e:
            self.file_object = open("Training_Logs/Training_Main_Log.txt", 'a+')
            self.log.log(self.file_object, "error %s" % e)









#c=Pred(r"Prediction_Batch_file")
#c.predic()
