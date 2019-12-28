import pandas as pd
import pyodbc


class Query:
    _data = pd.DataFrame()

    def __init__(self, server, database, query, startup_query=True):
        self.server = server
        self.database = database
        self.query = query
        self.__sql_connection_string = 'DRIVER={SQL Server};Server=' + self.server + \
                                       ';DATABASE=' + self.database + \
                                       ';Trusted_Connection=yes'
        if startup_query:
            self.getsql()

    def getsql(self):
        sql_connection = pyodbc.connect(self.__sql_connection_string)
        sql_connection.timeout = 60
        self._data = pd.read_sql_query(self.query, sql_connection)
        return self._data
