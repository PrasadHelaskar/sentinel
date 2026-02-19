import os
from dotenv import load_dotenv

load_dotenv(".config/.env")

class Settings:
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    OWNER = os.getenv("GITHUB_OWNER")

    REPOS = os.getenv("GITHUB_REPOS", "").split(",")

    ARTIFACT_NAME = os.getenv("ARTIFACT_NAME")

settings = Settings()
