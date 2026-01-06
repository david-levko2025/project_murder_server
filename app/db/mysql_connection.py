import mysql.connector
from mysql.connector.errors import Error 
from core.config import setting 


class DBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connection = None 
            cls._instance._connect()
            
        return cls._instance 

    def _connect(self):
        try:
            self._connection = mysql.connector.connect(
                host=setting.MYSQL_HOST,
                user=setting.MYSQL_USER,
                port=setting.MYSQL_PORT,
                database=setting.MYSQL_DB,
                password=setting.MYSQL_PASSWORD
            )
            if self._connection.is_connected():
                print("succesfully connecting to db")

        except Error as e:
            print("Error: can't connect to db", e) 

    def get_connection(self):
        if self._connection is None or not self._connection.is_connected():
            self._connect()
        return self._connection  
    
    def close_connection(self):
        if self._connection and self._connection.is_connected():
            self._connection.close()
            self._connection = None 
            DBConnection._instance = None 

