from pydantic_settings import BaseSettings 

class Setting(BaseSettings):
    MYSQL_USER: str 
    MYSQL_PORT: int  
    MYSQL_PASSWORD: str 
    MYSQL_HOST: str 
    MYSQL_DB: str 


setting = Setting()