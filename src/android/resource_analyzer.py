from pathlib import Path
from zipfile import ZipFile


class ResourceAnalyzer:
    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)

    def analyze(self):
        if not self.apk_path.exists():
            raise FileNotFoundError(
                f"APK file not found: {self.apk_path}"
            )

        resources = {
            "xml_files": [],
            "image_files": [],
            "asset_files": [],
        }

        with ZipFile(self.apk_path, "r") as apk:
            for file_name in apk.namelist():

                if file_name.endswith(".xml"):
                    resources["xml_files"].append(file_name)

                elif file_name.lower().endswith(
                    (".png", ".jpg", ".jpeg", ".webp")
                ):
                    resources["image_files"].append(file_name)

                elif file_name.startswith("assets/"):
                    resources["asset_files"].append(file_name)

        return resources