import zipfile
import io
import os

class ArtifactService:

    @staticmethod
    def extract_zip(content, extract_to="artifacts"):
        os.makedirs(extract_to, exist_ok=True)
        with zipfile.ZipFile(io.BytesIO(content)) as z:
            z.extractall(extract_to)
        return extract_to
