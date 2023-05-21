from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from os import listdir
import csv
from raw.Rawfile import rawdata
from log.applogger import Applogger
from cassandra.query import SimpleStatement



class db:
    """
          This class shall be used for handling all the cassandra operations.

          Written By: zaid
          Version: 1.0
          Revisions: None

          """
    def __init__(self):
        self.path = 'Training_Database/'
        self.good = "Training_file/Good_file/"
        self.bad = "Trainingfile/Bad_file/"
        self.log = Applogger()
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
            self.file = open("Training_Logs/DataBaseConnectionLog.txt", 'a+')
            self.log.log(self.file,"Error happened %s " % e)
            raise e


    def table_create(self,column):
        try:
            session = self.connection()
            querry_check = "SELECT table_name FROM system_schema.tables WHERE keyspace_name = 'mushroom' AND table_name = 'Train'"
            result_set = session.execute(querry_check)
            if result_set:
                file = open("Training_Logs/DataBaseConnectionLog.txt", 'a+')
                self.log.log(file,"Database exist")
            else:
                 try:
                     querry = "ALTER TABLE Train ADD  ("
                     for key in column.keys():
                         type = column[key]
                         querry += key + " " + type + ", "
                     querry = querry[:-2]
                     session.execute(querry)
                 except :
                        querry = "CREATE TABLE IF NOT EXISTS mushroom.Train ("
                        for key in column.keys():
                            type = column[key]
                            querry += key + " " + type + ", "
                        querry = querry[:-2]
                        querry += ", PRIMARY KEY(bruises,capcolor,capshape,capsurface,class),gillattachment,gillcolor,gillsize,gillspacing,habitat,odor,population,ringnumber,ringtype,sporeprintcolor,stalkcolorabovering,stalkcolorbelowring,stalkroot,stalkshape,stalksurfaceabovering,stalksurfacebelowring,veilcolor,veiltype))"
                        session.execute(querry)
                        file = open("Training_Logs/DbTableCreateLog.txt", 'a+')
                        self.log.log(file,"Table has been created ")
                        file.close()

        except Exception as e:
            file = open("Training_Logs/DbTableCreateLog.txt", 'a+')
            self.log.log(file, str(e))
            file.close()



    def adding_data(self,col):
        try:
            self.good = "Training_file/Good_file"
            session = self.connection()
            file = [f for f in listdir("Training_file/Good_file")]
            column_names = ", ".join(col.keys())
            insert_query = "INSERT INTO mushroom.Train ({columns}) VALUES"
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
            log_file = open("Training_Logs/DbInsertLog.txt", 'a+')
            self.log.log(log_file, str(e))
            log_file.close()


    def filefromdb(self):
        self.filename = "Inputfile.csv"
        self.filefromdb = "FileDB"
        #log_file = open("Training_Logs/ExportToCsv.txt", 'a+')
        try:
            session = self.connection()
            keyspace = 'mushroom'
            table = 'mytable'
            #querry_row="SELECT * FROM system_schema.columns WHERE keyspace_name = 'mushroom' AND table_name = 'mytable';"
            #querry_row=f"SELECT column_name  FROM system_schema.columns WHERE keyspace_name='{keyspace}' AND table_name='{table}'"
            query = "SELECT * FROM mushroom.mytable "
            result=session.execute(query)
            #column_name = ['ringtype','habitat'	,'stalksurfaceabovering','stalkcolorbelowring','stalkroot','capcolor','sporeprintcolor','odor','stalkshape','stalksurfacebelowring','population','bruises','gillspacing','stalkcolorabovering','veilcolor','gillcolor','ringnumber','capsurface','gillsize','veiltype','capshape','gillattachment','class']
            #column_name=[row.column_name for row in result ]
            column_name=result.column_names
            column_data=[]
            #query = "SELECT * FROM mushroom.mytable "
            #result = session.execute(query)
            for data in result:
               column_data.append(data)
            file = open('Trainingfiledb/Inputfile.csv', 'w', newline='')
            csvfile = csv.writer(file, delimiter=',', lineterminator='\r\n', quoting=csv.QUOTE_ALL, escapechar='\\')
            csvfile.writerow(column_name)
            csvfile.writerows(column_data)

            #log_file = open("Training_Logs/ExportToCsv.txt", 'a+')
            #self.log.log(log_file, "File exported successfully!!!")
            #log_file.close()
        except Exception as e:
              raise  e
              #log_file = open("Training_Logs/ExportToCsv.txt", 'a+')
              #self.log.log(log_file, "File exporting failed. Error : %s" % e)
              #log_file.close()

















d=db()
r=rawdata(r'C:\Users\91639\Desktop\Mushroom\Training_Batch_Files')
length_of_time,length_of_date,no_of_col,col_name=r.valuesfromschem()
#d.table_create(col_name)
#d.adding_data(col_name)
d.filefromdb()
#d.t()











