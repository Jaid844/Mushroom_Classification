from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from os import listdir
import csv
from log.applogger import Applogger



class db:
     def __init__(self):
         self.path = 'Prediction_Database/'
         self.badFilePath = "Prediction_Raw_Files_Validated/Bad_Raw"
         self.goodFilePath = "Prediction_Raw_Files_Validated/Good_Raw"
         self.log =Applogger()

     def connection(self):
         try:
             self.file = open("Prediction_Logs/DataBaseConnectionLog.txt", 'a+')
             cloud_config = {
                 'secure_connect_bundle': r'Database_cred\secure-connect-ineuron.zip'
             }
             auth_provider = PlainTextAuthProvider('DFuaqgwrhjzNIxpEZZpUpbgx',
                                                   'lBES3bwUE0o2Nk2rfgLteEwSsOi0Zo3vdKpiRuAhMclqWqPwNvp6cLUgYBN-3osp0R8GfKNmBGP3zp7w10owex.Czt-ceCIcsOqlSYzZCKe9WLKPL+s4kGWCP0aHpl5q')
             cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
             session = cluster.connect('ineuron')
             self.log.log(self.file, "connection established")
             return session
         except Exception as e:
             self.file = open("Prediction_Logs/DataBaseConnectionLog.txt", 'a+')
             self.log.log(self.file, "Error happened %s " % e)
             raise e

     def table_create(self, column):
         try:

                 session = self.connection()
                 querry_check = "SELECT table_name FROM system_schema.tables WHERE keyspace_name = 'mushroom' AND table_name = 'predictiontable'"
                 result_set = session.execute(querry_check)
                 if result_set:
                     print("database exist")
                 else:
                     try:
                         querry = "ALTER TABLE predictiontable ADD  ("
                         for key in column.keys():
                             type = column[key]
                             querry += key + " " + type + ", "
                         querry = querry[:-2]
                         session.execute(querry)
                     except:
                         querry = "CREATE TABLE IF NOT EXISTS mushroom.predictiontable ("
                         for key in column.keys():
                             type = column[key]
                             querry += key + " " + type + ", "
                         querry = querry[:-2]
                         querry += ", PRIMARY KEY(bruises,capcolor,capshape,capsurface,gillattachment,gillcolor,gillsize,gillspacing,habitat,odor,population,ringnumber,ringtype,sporeprintcolor,stalkcolorabovering,stalkcolorbelowring,stalkroot,stalkshape,stalksurfaceabovering,stalksurfacebelowring,veilcolor,veiltype))"
                         session.execute(querry)
         except Exception as e:
             file = open("Prediction_logs/DbTableCreateLog.txt", 'a+')
             self.log.log(file, str(e))
             file.close()

     def adding_data(self, col):
         try:
             self.good = "Prediction_Raw_Files_Validated/Good_Raw"
             session = self.connection()
             file = [f for f in listdir("Prediction_Raw_Files_Validated/Good_Raw")]
             column_names = ", ".join(col.keys())
             insert_query = "INSERT INTO mushroom.predictiontable  ({columns}) VALUES"
             formatted_query = insert_query.format(columns=column_names)
             for tile in file:
                 with open(self.good + '/' + tile, 'r') as f:
                     next(f)
                     reader = csv.reader(f, delimiter="\n")
                     for list in enumerate(reader):
                         for l in list[1]:
                             querry = formatted_query + "(" + l + ")"
                             session.execute(querry)

         except Exception as e:
             log_file = open("Prediction_logs/DbInsertLog.txt", 'a+')
             self.log.log(log_file, str(e))
             log_file.close()

     def filefromdb(self):
         self.filename = "Inputfile.csv"
         self.filefromdb = "FileDB"
         # log_file = open("Training_Logs/ExportToCsv.txt", 'a+')
         try:
             session = self.connection()
             keyspace = 'mushroom'
             table = 'predic'
             # querry_row="SELECT * FROM system_schema.columns WHERE keyspace_name = 'mushroom' AND table_name = 'mytable';"
             # querry_row=f"SELECT column_name  FROM system_schema.columns WHERE keyspace_name='{keyspace}' AND table_name='{table}'"
             query = "SELECT * FROM mushroom.predictiontable"
             result = session.execute(query)
             # column_name = ['ringtype','habitat'	,'stalksurfaceabovering','stalkcolorbelowring','stalkroot','capcolor','sporeprintcolor','odor','stalkshape','stalksurfacebelowring','population','bruises','gillspacing','stalkcolorabovering','veilcolor','gillcolor','ringnumber','capsurface','gillsize','veiltype','capshape','gillattachment','class']
             # column_name=[row.column_name for row in result ]
             column_name = result.column_names
             column_data = []
             # query = "SELECT * FROM mushroom.mytable "
             # result = session.execute(query)
             for data in result:
                 column_data.append(data)
             file = open('Predictionfile_db/Inputfile.csv', 'w', newline='')
             csvfile = csv.writer(file, delimiter=',', lineterminator='\r\n', quoting=csv.QUOTE_ALL, escapechar='\\')
             csvfile.writerow(column_name)
             csvfile.writerows(column_data)
             log_file = open("Training_Logs/ExportToCsv.txt", 'a+')
             self.log.log(log_file, "File exported successfully!!!")
             log_file.close()
         except Exception as e:
             raise e
             # log_file = open("Training_Logs/ExportToCsv.txt", 'a+')
             # self.log.log(log_file, "File exporting failed. Error : %s" % e)
             # log_file.close()

#c=db()
#c.connection()

