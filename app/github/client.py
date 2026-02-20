import requests
from app.core.config import settings

class GitHubClient:
    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json"
        }

    def get_workflow_runs(self,repo):
        url = f"{self.BASE_URL}/repos/{settings.OWNER}/{repo}/actions/runs"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()["workflow_runs"]

    def get_artifacts(self, repo, run_id):
        url = f"{self.BASE_URL}/repos/{settings.OWNER}/{repo}/actions/runs/{run_id}/artifacts"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()["artifacts"]

    def download_artifact(self, repo, artifact_id):
        url = f"{self.BASE_URL}/repos/{settings.OWNER}/{repo}/actions/artifacts/{artifact_id}/zip"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.content
