from typing import Listfrom aiogram.enums import chat_typefrom pydantic_settings import BaseSettings, SettingsConfigDictclass Settings(BaseSettings):    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)    API_KEY: str    BOT_TOKEN: str    PASSWORD: str    PREMIUM_PRICE: int = 25000    HOST_GROUP_PRICE: int = 36000    HOST_GROUP_ID: int = -1002005807005    IMAGE_GEN_GROUP_ID: int = -1002005807005    COMMENTS_GROUP_ID: int = -1002112530699    CHANNEL_ID: int = -1001515179618    SUBSCRIPTION_CHANNEL_ID: int = -4112946370    ERROR_CHANNEL_ID: int = -1001980262190    EVENT_CHANNEL_ID: int = -840987349    ALLOWED_GROUPS: List[int] = [HOST_GROUP_ID, IMAGE_GEN_GROUP_ID]    AVAILABLE_GROUP_TYPES: List[chat_type.ChatType] = [chat_type.ChatType.GROUP,                                                       chat_type.ChatType.SUPERGROUP]    IMAGE_GENERATION_WORDS: List[str] = ["generate", "imagine"]    WEB_URL: str    DB_URL: str    REDIS_URL: str    POSTGRES_DB_USER: str    POSTGRES_DB_PASSWORD: str    REDIS_HOST: str    POSTGRES_TIMEZONE: str = "Asia/Tashkent"settings = Settings()