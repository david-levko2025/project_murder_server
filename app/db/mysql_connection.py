from core.config import setting
import mysql.connector
from mysql.connector.errors import Error


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
                password=setting.MYSQL_PASSWORD,
                port=setting.MYSQL_PORT,
                database=setting.MYSQL_DB
            )
            if self._connection.is_connected():
                print("successfuly connect to database")
        except Error as e:
            print("Error: can't match to database", e)

    def get_connection(self):
        if self._connection is None or not self._connection.is_connected():
            self._connect()
        return self._connection
     
    def close_connection(self):
        if self._connection and self._connection.is_connected():
            self._connection.close()
            self._connection = None
            DBConnection._instance = None