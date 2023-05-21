from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from os import listdir
import csv
from raw.Rawfile import rawdata
from log.applogger import Applogger
from cassandra.query import SimpleStatement


class db:
     def __init__(self):
         self.path = 'Prediction_Database/'
         self.badFilePath = "Prediction_Raw_Files_Validated/Bad_Raw"
         self.goodFilePath = "Prediction_Raw_Files_Validated/Good_Raw"
         self.log =Applogger()

     def connection(self):
         try:
             cloud_config = {
                 'secure_connect_bundle': r'C:\Users\91639\Downloads\secure-connect-ineuron.zip'
             }
             auth_provider = PlainTextAuthProvider('DFuaqgwrhjzNIxpEZZpUpbgx',
                                                   'lBES3bwUE0o2Nk2rfgLteEwSsOi0Zo3vdKpiRuAhMclqWqPwNvp6cLUgYBN-3osp0R8GfKNmBGP3zp7w10owex.Czt-ceCIcsOqlSYzZCKe9WLKPL+s4kGWCP0aHpl5q')
             cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
             session = cluster.connect('ineuron')
             return session
         except Exception as e:
             self.file = open("Prediction_logs/DataBaseConnectionLog.txt", 'a+')
             self.log.log(self.file, "Error happened %s " % e)
             raise e

     def table_create(self, column):
         try:
             session = self.connection()
             querry_check = "SELECT table_name FROM system_schema.tables WHERE keyspace_name = 'mushroom' AND table_name = 'Prediction'"
             result_set = session.execute(querry_check)
             if result_set:
                 file = open("Prediction_logs/DataBaseConnectionLog.txt", 'a+')
                 self.log.log(file, "Database exist")
             else:
                 try:
                     querry = "ALTER TABLE Prediction ADD  ("
                     for key in column.keys():
                         type = column[key]
                         querry += key + " " + type + ", "
                     querry = querry[:-2]
                     session.execute(querry)
                 except:
                     querry = "CREATE TABLE IF NOT EXISTS mushroom.Prediction ("
                     for key in column.keys():
                         type = column[key]
                         querry += key + " " + type + ", "
                     querry = querry[:-2]
                     querry += ", PRIMARY KEY(bruises,capcolor,capshape,capsurface,class),gillattachment,gillcolor,gillsize,gillspacing,habitat,odor,population,ringnumber,ringtype,sporeprintcolor,stalkcolorabovering,stalkcolorbelowring,stalkroot,stalkshape,stalksurfaceabovering,stalksurfacebelowring,veilcolor,veiltype))"
                     session.execute(querry)
                     file = open("Prediction_logs/DbTableCreateLog.txt", 'a+')
                     self.log.log(file, "Table has been created ")
                     file.close()

         except Exception as e:
             file = open("Prediction_logs/DbTableCreateLog.txt", 'a+')
             self.log.log(file, str(e))
             file.close()
