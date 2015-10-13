__author__ = 'alessior@kth.se'


import sqlite3
# DBInterface is  an interface class done to ease the communication with the underlying database system
#
#Variables:
#-connectionName: string specifying the uri of the database
#-connection: connection object, check sqlite3
#-cursor: cursor object, check sqllite3
#x
#Functions:
#init(connectionName): starts the connection with the database, the database is found at the filename/uri specified by connectionName
#getConnectionName(): returns connectionName(check init)
#isConnectionOk(): return true if the connection with the database is ok, 0 otherwise
#
#
#


class DBInterface:
    def __init__(self, connectionName):
        self.connectionName = connectionName
        self.connection = sqlite3.connect(self.connectionName)
        if (self.connection != None):
            self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def getConnectionName(self):
        return self.connectionName

    def isConnectionOk(self):
        #actually it doesn't check if the connection is ok when it is invoked
        return  0  if  self.connection == None else 1





