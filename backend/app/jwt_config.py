from pydantic_settings import BaseSettings, SettingsConfigDict

class JWTSettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str

    model_config = SettingsConfigDict(env_file=".env.jwt", env_file_encoding="utf-8")

jwt_settings = JWTSettings()

