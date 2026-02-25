import os
from dotenv import load_dotenv

load_dotenv(".config/.env")

class Settings:
    OWNER_TOKEN = os.getenv("OWNER_TOKEN")
    OWNER = os.getenv("OWNER_OWNER")

    REPOS = os.getenv("OWNER_REPOS", "").split(",")

    ARTIFACT_NAME = os.getenv("ARTIFACT_NAME")

settings = Settings()
