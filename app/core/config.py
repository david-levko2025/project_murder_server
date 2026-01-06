from pydantic_settings import BaseSettings, SettingsConfigDict 

class Setting(BaseSettings):
    MYSQL_USER: str 
    MYSQL_PORT: int  
    MYSQL_PASSWORD: str 
    MYSQL_HOST: str 
    MYSQL_DB: str 

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_file_encoding="utf-8"
        )


setting = Setting()